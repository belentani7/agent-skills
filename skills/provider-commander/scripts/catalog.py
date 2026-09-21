#!/usr/bin/env python3
"""Sondea cada llave distinta: estado, saldo y modelos gratis disponibles AHORA.
Escribe ~/.config/opencode/commander/catalog.json (sin secretos)."""
import json
import os
import pathlib
import urllib.error
import urllib.request

OUT = pathlib.Path.home() / ".config" / "opencode" / "commander" / "catalog.json"
UA = {"User-Agent": "Mozilla/5.0 commander/1.0", "Accept": "application/json"}

def get(url, key=None, extra=None):
    h = dict(UA)
    if key:
        h["Authorization"] = f"Bearer {key}"
    if extra:
        h.update(extra)
    req = urllib.request.Request(url, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return r.status, json.loads(r.read().decode("utf-8", "ignore"))
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception as e:
        return 0, {"err": str(e)[:120]}

def env(k):
    return os.environ.get(k, "")

# (provider, env_var, base)
OPENROUTER = [("openrouter", v) for v in
              ["OPENROUTER_API_KEY", "OPENROUTER_KEY_2", "OPENROUTER_KEY_3", "OPENROUTER_DEMO_KEY"]]
NVIDIA = [("nvidia", v) for v in ["NVIDIA_API_KEY", "NVIDIA_ALT_KEY"]]
SIMPLE = [
    ("groq",      "GROQ_API_KEY",      "https://api.groq.com/openai/v1/models"),
    ("deepseek",  "DEEPSEEK_API_KEY",  "https://api.deepseek.com/v1/models"),
    ("morph",     "MORPH_API_KEY",     "https://api.morphllm.com/v1/models"),
    ("zai",       "Z_AI_API_KEY",      "https://api.z.ai/api/coding/paas/v4/models"),
    ("cerebras",  "CEREBRAS_API_KEY",  "https://api.cerebras.ai/v1/models"),
    ("anthropic", "ANTHROPIC_API_KEY", "https://api.anthropic.com/v1/models"),
    ("openai",    "OPENAI_API_KEY",    "https://api.openai.com/v1/models"),
]

catalog = {"generated_by": "commander/catalog.py", "providers": {}}

def note(prov, var, status, extra=None):
    e = catalog["providers"].setdefault(prov, {})
    e[var] = {"status": status, **(extra or {})}
    return e[var]

# --- OpenRouter: saldo por llave + modelos gratis ---
st, models = get("https://openrouter.ai/api/v1/models")
free_ids = []
if isinstance(models, dict) and "data" in models:
    for m in models["data"]:
        pr = m.get("pricing", {})
        if pr.get("prompt") in ("0", "0.0", 0) and pr.get("completion") in ("0", "0.0", 0):
            free_ids.append(m["id"])
free_ids.sort()
for prov, var in OPENROUTER:
    key = env(var)
    if not key:
        note(prov, var, "SKIP"); continue
    ks, kj = get("https://openrouter.ai/api/v1/key", key)
    bal = None
    if isinstance(kj, dict) and "data" in kj:
        d = kj["data"]
        bal = {"label": d.get("label"), "limit_remaining": d.get("limit_remaining"),
               "usage": d.get("usage"), "is_free_tier": d.get("is_free_tier")}
    note(prov, var, ks, {"balance": bal, "free_models": len(free_ids)})
catalog["providers"].setdefault("openrouter", {})["_free_model_ids"] = free_ids

# --- NVIDIA ---
for prov, var in NVIDIA:
    key = env(var)
    if not key:
        note(prov, var, "SKIP"); continue
    st, j = get("https://integrate.api.nvidia.com/v1/models", key)
    n = len(j.get("data", [])) if isinstance(j, dict) else 0
    note(prov, var, st, {"models": n})

# --- Simples ---
for prov, var, url in SIMPLE:
    key = env(var)
    if not key:
        note(prov, var, "SKIP"); continue
    extra = {"anthropic-version": "2023-06-01"} if prov == "anthropic" else None
    st, j = get(url, key, extra)
    n = len(j.get("data", [])) if isinstance(j, dict) else 0
    note(prov, var, st, {"models": n})

# --- DeepSeek balance ---
key = env("DEEPSEEK_API_KEY")
if key:
    st, j = get("https://api.deepseek.com/user/balance", key)
    if isinstance(j, dict):
        catalog["providers"]["deepseek"][key and "DEEPSEEK_API_KEY"]["balance"] = j.get("balance_infos")

# --- Google ---
key = env("GOOGLE_API_KEY")
if key:
    st, j = get(f"https://generativelanguage.googleapis.com/v1beta/models?key={key}")
    note("google", "GOOGLE_API_KEY", st, {"models": len(j.get("models", [])) if isinstance(j, dict) else 0})

# --- OpenZen (base desconocida; probar 2) ---
key = env("OPENZEN_API_KEY")
if key:
    for base in ["https://api.openzen.ai/v1/models", "https://openzen.ai/api/v1/models"]:
        st, _ = get(base, key)
        if st:
            note("openzen", "OPENZEN_API_KEY", st, {"base": base}); break
    else:
        note("openzen", "OPENZEN_API_KEY", 0, {"base": "none-resolved"})

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(catalog, indent=2, ensure_ascii=False), encoding="utf-8")

print("=== CATALOGO ===")
for prov, keys in catalog["providers"].items():
    if prov == "openrouter":
        print(f"openrouter: {len(free_ids)} modelos gratis")
        for var, d in keys.items():
            if var.startswith("_"): continue
            b = d.get("balance") or {}
            print(f"   {var:22} status={d['status']} saldo={b.get('limit_remaining')} label={b.get('label')}")
    elif isinstance(keys, dict):
        for var, d in keys.items():
            print(f"{prov:10} {var:22} status={d.get('status')} {('models='+str(d.get('models'))) if d.get('models') is not None else ''}")
print(f"\nsaved: {OUT}")
print("ejemplos gratis openrouter:", ", ".join(free_ids[:8]))
