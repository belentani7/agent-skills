#!/usr/bin/env python3
"""provider-commander orchestrator v2.

Capacidades (segun spec):
  - Secretos fuera del prompt: las llaves solo viven en env; nunca se imprimen ni se
    pasan al texto. Enmascarado de salida por si un proveedor devuelve algo con forma de key.
  - Throttling por proveedor (rpm) con ventana deslizante.
  - Rotacion de llaves del mismo proveedor (round-robin).
  - Circuit breaker por llave y por proveedor (fallo consecutivo -> cooldown).
  - Reintentos con backoff exponencial.
  - Fallback en cadena por tipo de tarea.
  - Tracking de uso y coste estimado.
  - Modo mock (--dry-run) sin gastar creditos.

Uso:
  python orchestrator.py --dry-run --tasks tasks.json
  python orchestrator.py --tasks tasks.json
  python orchestrator.py --compare "prompt" --providers groq,zai,openrouter
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from collections import deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).parent
REG = json.loads((HERE / "registry.json").read_text(encoding="utf-8"))
USAGE_PATH = HERE.parent / "references" / "usage.json"
LAST_PATH = HERE.parent / "references" / "last_run.json"

# secretos locales (fuera del repo): ~/.config/opencode/commander/secrets.local.json
SECRETS_PATH = HERE.parent.parent.parent / "commander" / "secrets.local.json"

def _load_local():
    try:
        return json.loads(SECRETS_PATH.read_text(encoding="utf-8")) if SECRETS_PATH.exists() else {}
    except Exception:
        return {}

LOCAL = _load_local()

def _key_values(provider: str) -> dict:
    """env var name -> valor. Prioriza entorno; completa con secretos locales."""
    out = {}
    local = LOCAL.get(provider, {})
    for v in REG["providers"][provider].get("env", []):
        val = os.environ.get(v) or local.get(v)
        if val:
            out[v] = val
    for v, val in local.items():
        if val and v not in out:
            out[v] = val
    return out

# ---------------------------------------------------------------- secret masking
_SECRETS = []
for _p in REG["providers"]:
    for _val in _key_values(_p).values():
        if _val and len(_val) > 12:
            _SECRETS.append(_val)
_KEY_RX = re.compile(r"(sk-or-v1-|sk-ant-|nvapi-|gsk_|csk-|sk-proj-|sk-KOM|nfp_|AIza|gho_|ghp_)[A-Za-z0-9_\-\.]{6,}")

def mask(text: str) -> str:
    if not text:
        return text
    for s in _SECRETS:
        if s in text:
            text = text.replace(s, s[:6] + "****" + s[-3:])
    return _KEY_RX.sub(lambda m: m.group(1) + "****", text)

# ---------------------------------------------------------------- state
_lock = threading.Lock()
_states: dict[str, dict] = {}     # "provider:env" -> state
_usage: dict[str, dict] = {}

def _state(provider, env_var):
    k = f"{provider}:{env_var}"
    with _lock:
        if k not in _states:
            _states[k] = {"hits": deque(), "fails": 0, "open_until": 0.0, "rr": 0}
        return _states[k]

def _usage_slot(provider, env_var):
    k = f"{provider}:{env_var}"
    with _lock:
        return _usage.setdefault(k, {"calls": 0, "ok": 0, "fail": 0, "in_tok": 0, "out_tok": 0, "cost_usd": 0.0})

def keys_of(provider):
    return list(_key_values(provider).keys())

def available(provider) -> bool:
    cfg = REG["providers"].get(provider, {})
    if cfg.get("disabled"):
        return False
    now = time.time()
    for v in keys_of(provider):
        st = _state(provider, v)
        if st["open_until"] <= now:
            return True
    return False

def _throttle(provider, env_var):
    cfg = REG["providers"][provider]
    rpm = cfg.get("rpm", 30)
    rph = cfg.get("rph")
    st = _state(provider, env_var)
    while True:
        now = time.time()
        while st["hits"] and now - st["hits"][0] > 3600:
            st["hits"].popleft()
        last_min = [t for t in st["hits"] if now - t <= 60]
        if rpm and len(last_min) >= rpm:
            time.sleep(max(0.2, 60 - (now - last_min[0])))
            continue
        if rph and len(st["hits"]) >= rph:
            time.sleep(max(0.5, 3600 - (now - st["hits"][0])))
            continue
        st["hits"].append(now)
        return

def _pick_key(provider):
    now = time.time()
    ks = keys_of(provider)
    if not ks:
        return None
    st0 = _state(provider, "pool")
    for i in range(len(ks)):
        v = ks[(st0["rr"] + i) % len(ks)]
        if _state(provider, v)["open_until"] <= now:
            with _lock:
                st0["rr"] = (st0["rr"] + i + 1) % len(ks)
            return v
    return None

# ---------------------------------------------------------------- call
def _post(url, headers, body, timeout):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "ignore"))

def call(provider, model, prompt, max_tokens=2048, system=None, timeout=120, retries=2, dry_run=False):
    cfg = REG["providers"].get(provider, {})
    if cfg.get("disabled"):
        return {"provider": provider, "model": model, "ok": False, "error": f"disabled: {cfg.get('reason')}"}
    env_var = _pick_key(provider)
    if not env_var:
        return {"provider": provider, "model": model, "ok": False, "error": "circuit_open_or_no_key"}
    if dry_run:
        return {"provider": provider, "model": model, "key_var": env_var, "ok": True,
                "text": f"[MOCK] {model} would answer ({len(prompt)} chars)", "mock": True}
    key = _key_values(provider)[env_var]
    _throttle(provider, env_var)
    if cfg["api"] == "anthropic":
        url = f"{cfg['base']}/messages"
        body = {"model": model, "max_tokens": max_tokens, "messages": [{"role": "user", "content": prompt}]}
        if system: body["system"] = system
        headers = {"x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json", "User-Agent": "orchestrator/2"}
    else:
        url = f"{cfg['base']}/chat/completions"
        msgs = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": prompt}]
        body = {"model": model, "messages": msgs, "max_tokens": max_tokens}
        headers = {"Authorization": f"Bearer {key}", "content-type": "application/json", "User-Agent": "orchestrator/2"}
        if provider == "openrouter":
            headers["HTTP-Referer"] = "https://local.orchestrator"; headers["X-Title"] = "provider-commander"

    st = _state(provider, env_var); us = _usage_slot(provider, env_var)
    last_err = ""
    for attempt in range(retries + 1):
        try:
            j = _post(url, headers, body, timeout)
            if cfg["api"] == "anthropic":
                text = "".join(b.get("text", "") for b in j.get("content", []))
                u = j.get("usage", {})
            else:
                m = j["choices"][0]["message"]
                text = m.get("content") or ("[reasoning] " + (m.get("reasoning_content") or "")[:800])
                u = j.get("usage", {})
            with _lock:
                st["fails"] = 0; us["calls"] += 1; us["ok"] += 1
                us["in_tok"] += int(u.get("prompt_tokens", 0) or 0)
                us["out_tok"] += int(u.get("completion_tokens", 0) or 0)
                c = cfg.get("cost", {"in": 0, "out": 0})
                us["cost_usd"] += (u.get("prompt_tokens", 0) or 0) / 1e6 * c.get("in", 0) + (u.get("completion_tokens", 0) or 0) / 1e6 * c.get("out", 0)
            return {"provider": provider, "model": j.get("model", model), "key_var": env_var, "ok": True, "text": mask(text)}
        except urllib.error.HTTPError as e:
            code = e.code
            last_err = f"HTTP {code}"
            if code in (401, 402, 403, 429, 500, 502, 503, 504):
                with _lock:
                    st["fails"] += 1; us["calls"] += 1; us["fail"] += 1
                    if st["fails"] >= 2:
                        st["open_until"] = time.time() + 60
                        last_err += " (circuit open 60s)"
            else:
                with _lock:
                    us["calls"] += 1; us["fail"] += 1
        except Exception as e:
            last_err = str(e)[:120]
            with _lock:
                st["fails"] += 1; us["calls"] += 1; us["fail"] += 1
                if st["fails"] >= 3:
                    st["open_until"] = time.time() + 60
        if attempt < retries:
            time.sleep(2 ** attempt)
    return {"provider": provider, "model": model, "key_var": env_var, "ok": False, "error": mask(last_err)}

def call_with_fallback(candidates, prompt, max_tokens=2048, system=None, dry_run=False):
    tried = []
    for provider, model in candidates:
        if not available(provider):
            tried.append(f"{provider}(unavailable)"); continue
        r = call(provider, model, prompt, max_tokens=max_tokens, system=system, dry_run=dry_run)
        r["tried"] = tried + [f"{provider}/{model}"]
        if r.get("ok"):
            return r
        tried.append(f"{provider}({r.get('error')})")
    return {"provider": None, "model": None, "ok": False, "error": "all_failed", "tried": tried}

# ---------------------------------------------------------------- routing
KIND_PATTERNS = [
    ("judge",    r"\b(audita|auditoria|security|seguridad|vulnerabilidad|pentest|revisa critico)\b"),
    ("reason",   r"\b(arquitectura|architecture|disena|planifica|razona|reason|analiza a fondo|estrategia|demuestra)\b"),
    ("edit",     r"\b(edita|edit|patch|aplica|apply|diff|multi-archivo|refactor)\b"),
    ("classify", r"\b(clasifica|etiqueta|extrae|json|tabla|lista|resume|resumen)\b"),
    ("trivial",  r"\b(renombra|rename|formatea|formato|traduce|traducir|hola|ping|pong)\b"),
]

def infer_kind(prompt):
    t = prompt.lower()
    for k, rx in KIND_PATTERNS:
        if re.search(rx, t):
            return k
    return "code"

def run_task(task, dry_run=False):
    kind = task.get("kind") or infer_kind(task["prompt"])
    if task.get("provider") and task.get("model"):
        cands = [[task["provider"], task["model"]]]
    else:
        cands = REG["routing"].get(kind, REG["routing"]["code"])
    t0 = time.time()
    r = call_with_fallback(cands, task["prompt"], max_tokens=task.get("max_tokens", 2048),
                           system=task.get("system"), dry_run=dry_run)
    r.update({"id": task.get("id", task["prompt"][:24]), "kind": kind, "elapsed_s": round(time.time() - t0, 1)})
    return r

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tasks"); ap.add_argument("--compare"); ap.add_argument("--providers", default="groq,zai,openrouter")
    ap.add_argument("--mode", default="split", choices=["split", "compare"])
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--max-tokens", type=int, default=2048)
    args = ap.parse_args()

    if args.compare:
        tasks = []
        for prov in [p.strip() for p in args.providers.split(",") if p.strip()]:
            model = {"openrouter": "openrouter/auto", "zai": "glm-4.5-flash", "morph": "morph-dsv41flash",
                     "groq": "openai/gpt-oss-120b", "nvidia": "nvidia/nemotron-3-super-120b-a12b",
                     "opencode": "big-pickle", "deepseek": "deepseek-v4-pro"}.get(prov, "openai/gpt-oss-120b")
            tasks.append({"id": prov, "prompt": args.compare, "provider": prov, "model": model, "kind": "compare"})
    else:
        raw = args.tasks
        if raw and Path(raw).exists():
            raw = Path(raw).read_text(encoding="utf-8")
        tasks = json.loads(raw) if raw else []
        tasks = [{"prompt": t} if isinstance(t, str) else t for t in tasks]
    if not tasks:
        print("sin tareas"); return 2

    print(f"orchestrator: {len(tasks)} tarea(s)  workers={args.workers}  dry_run={args.dry_run}")
    print(f"cadena: {' -> '.join(REG['chain'])}")
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = [ex.submit(run_task, t, args.dry_run) for t in tasks]
        for f in as_completed(futs):
            r = f.result(); results.append(r)
            mark = "OK " if r.get("ok") else "XX "
            head = (r.get("text") or r.get("error") or "")[:100].replace("\n", " ")
            print(f"{mark}[{r['id']:14}] {(r.get('provider') or '-'):11} {(r.get('model') or '-'):30} {r['elapsed_s']:5}s  {head}")

    LAST_PATH.parent.mkdir(parents=True, exist_ok=True)
    LAST_PATH.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    USAGE_PATH.write_text(json.dumps(_usage, indent=2, ensure_ascii=False), encoding="utf-8")
    ok = sum(1 for r in results if r.get("ok"))
    cost = sum(u["cost_usd"] for u in _usage.values())
    print(f"\n{ok}/{len(results)} OK  |  coste estimado acumulado: ${cost:.4f}  |  {USAGE_PATH}")
    return 0 if ok == len(results) else 1

if __name__ == "__main__":
    sys.exit(main())
