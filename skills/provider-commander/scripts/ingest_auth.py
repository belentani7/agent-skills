#!/usr/bin/env python3
"""Ingesta las llaves de ~/.local/share/opencode/auth.json a secrets.local.json.
Valida cada una. Nunca imprime valores completos."""
import json, os, urllib.request, urllib.error, hashlib
from pathlib import Path

AUTH = Path(os.path.expanduser("~/.local/share/opencode/auth.json"))
SEC = Path(os.path.expanduser("~/.config/opencode/commander/secrets.local.json"))

MAP = {
    "opencode":    "OPENCODE_ZEN_KEY",
    "deepseek":    "DEEPSEEK_API_KEY_2",
    "openrouter":  "OPENROUTER_KEY_4",
    "zai":         "Z_AI_API_KEY_2",
    "huggingface": "HF_TOKEN",
}
CHECK = {
    "opencode":   "https://opencode.ai/zen/v1/models",
    "deepseek":   "https://api.deepseek.com/v1/models",
    "openrouter": "https://openrouter.ai/api/v1/key",
    "zai":        "https://api.z.ai/api/coding/paas/v4/models",
    "huggingface":"https://huggingface.co/api/models?limit=1",
}

def mask(v): return v[:7] + "..." + v[-4:]
def h(v): return hashlib.sha256(v.encode()).hexdigest()[:8]

def validate(prov, key):
    req = urllib.request.Request(CHECK[prov], headers={"Authorization": f"Bearer {key}", "User-Agent": "ingest/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return True, r.status
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}"
    except Exception as e:
        return False, str(e)[:70]

def main():
    auth = json.loads(AUTH.read_text(encoding="utf-8"))
    secrets = json.loads(SEC.read_text(encoding="utf-8")) if SEC.exists() else {}
    added = 0
    for prov, var in MAP.items():
        key = (auth.get(prov) or {}).get("key")
        if not key:
            print(f"  -- {prov}: sin llave en auth.json"); continue
        ok, info = validate(prov, key)
        print(f"  {'OK ' if ok else 'XX '} {prov:12} {h(key)}  {mask(key)}  -> {info}")
        if ok:
            secrets.setdefault(prov, {})[var] = key
            added += 1
    SEC.parent.mkdir(parents=True, exist_ok=True)
    SEC.write_text(json.dumps(secrets, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nañadidas: {added}  ->  {SEC}")
    for p, d in secrets.items():
        print(f"  {p}: {list(d.keys())}")

if __name__ == "__main__":
    main()
