"""Providers OpenAI-compatible verificados. Resuelve keys desde env en runtime (no guarda secretos).
Rotacion automatica cuando hay varias keys del mismo proveedor."""
import os, json, itertools, urllib.request, urllib.error

# provider -> {base, env vars (orden = rotacion), tipo api, notas}
PROVIDERS = {
    "openrouter": {
        "base": "https://openrouter.ai/api/v1",
        "env": ["OPENROUTER_API_KEY", "OPENROUTER_KEY_2", "OPENROUTER_KEY_3"],
        "api": "openai",
        "free": ["openrouter/auto"],  # + cualquier id :free del catalogo
    },
    "groq": {
        "base": "https://api.groq.com/openai/v1",
        "env": ["GROQ_API_KEY"],
        "api": "openai",
        "free": ["openai/gpt-oss-20b", "openai/gpt-oss-120b", "groq/compound", "groq/compound-mini"],
    },
    "nvidia": {
        "base": "https://integrate.api.nvidia.com/v1",
        "env": ["NVIDIA_API_KEY", "NVIDIA_ALT_KEY"],
        "api": "openai",
        "free": ["nvidia/nemotron-3-super-120b-a12b", "nvidia/nemotron-3.5-lightning-30b-a3b"],
    },
    "morph": {
        "base": "https://api.morphllm.com/v1",
        "env": ["MORPH_API_KEY"],
        "api": "openai",
        "free": [],
    },
    "deepseek": {
        "base": "https://api.deepseek.com/v1",
        "env": ["DEEPSEEK_API_KEY"],
        "api": "openai",
        "free": [],
    },
    "zai": {
        "base": "https://api.z.ai/api/coding/paas/v4",
        "env": ["Z_AI_API_KEY"],
        "api": "openai",
        "free": ["glm-4.5-flash"],
    },
    "anthropic": {
        "base": "https://api.anthropic.com/v1",
        "env": ["ANTHROPIC_API_KEY"],
        "api": "anthropic",
        "free": [],
    },
}

# asignacion por tipo de tarea (gratis primero)
ASSIGN = {
    "trivial":    ("groq", "openai/gpt-oss-20b"),
    "code":       ("groq", "openai/gpt-oss-120b"),
    "classify":   ("zai", "glm-4.5-flash"),
    "edit":       ("morph", "morph-dsv41flash"),
    "reason":     ("morph", "morph-glm52-744b"),
    "judge":      ("anthropic", "claude-sonnet-4-5"),
}

_rot = {p: itertools.cycle(c["env"]) for p, c in PROVIDERS.items()}

def key_for(provider):
    for _ in range(len(PROVIDERS[provider]["env"])):
        var = next(_rot[provider])
        k = os.environ.get(var, "")
        if k:
            return var, k
    return None, None

def chat(provider, model, prompt, max_tokens=2048, system=None, timeout=120):
    cfg = PROVIDERS[provider]
    var, key = key_for(provider)
    if not key:
        return {"provider": provider, "model": model, "ok": False, "error": f"no key for {provider}"}
    if cfg["api"] == "anthropic":
        url = f"{cfg['base']}/messages"
        body = {"model": model, "max_tokens": max_tokens,
                "messages": [{"role": "user", "content": prompt}]}
        if system:
            body["system"] = system
        headers = {"x-api-key": key, "anthropic-version": "2023-06-01",
                   "content-type": "application/json", "User-Agent": "commander/1.0"}
    else:
        url = f"{cfg['base']}/chat/completions"
        msgs = ([{"role": "system", "content": system}] if system else []) + \
               [{"role": "user", "content": prompt}]
        body = {"model": model, "messages": msgs, "max_tokens": max_tokens}
        headers = {"Authorization": f"Bearer {key}", "content-type": "application/json",
                   "User-Agent": "commander/1.0"}
        if provider == "openrouter":
            headers["HTTP-Referer"] = "https://local.commander"
            headers["X-Title"] = "provider-commander"
    data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            j = json.loads(r.read().decode("utf-8", "ignore"))
        if cfg["api"] == "anthropic":
            txt = "".join(b.get("text", "") for b in j.get("content", []))
        else:
            msg = j["choices"][0]["message"]
            txt = msg.get("content") or ""
            if not txt and msg.get("reasoning_content"):
                txt = "[reasoning] " + msg["reasoning_content"][:800]
        return {"provider": provider, "model": j.get("model", model), "key_var": var,
                "ok": True, "text": txt}
    except urllib.error.HTTPError as e:
        return {"provider": provider, "model": model, "key_var": var, "ok": False,
                "error": f"HTTP {e.code}: {e.read(200).decode('utf-8','ignore')[:160]}"}
    except Exception as e:
        return {"provider": provider, "model": model, "key_var": var, "ok": False,
                "error": str(e)[:160]}
