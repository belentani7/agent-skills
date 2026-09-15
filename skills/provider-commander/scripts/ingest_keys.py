#!/usr/bin/env python3
"""Ingesta de llaves Groq desde un archivo de texto.
Valida cada llave (GET /models), deduplica y las guarda en
~/.config/opencode/commander/secrets.local.json (local, no en repo).
Nunca imprime el valor completo.
"""
import hashlib, json, os, re, sys, urllib.request, urllib.error
from pathlib import Path

SRC = Path(r"C:\Users\USER\Desktop\groq_keys.txt")
SECRETS = Path.home() / ".config" / "opencode" / "commander" / "secrets.local.json"
PROV = "groq"
BASE = "https://api.groq.com/openai/v1/models"
RX = re.compile(r"^gsk_[A-Za-z0-9]{40,}$")

def mask(v): return v[:7] + "..." + v[-4:]
def h(v): return hashlib.sha256(v.encode()).hexdigest()[:8]

def validate(key):
    req = urllib.request.Request(BASE, headers={"Authorization": f"Bearer {key}", "User-Agent": "ingest/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            j = json.loads(r.read().decode("utf-8", "ignore"))
            return True, len(j.get("data", []))
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}"
    except Exception as e:
        return False, str(e)[:80]

def load_secrets():
    if SECRETS.exists():
        try: return json.loads(SECRETS.read_text(encoding="utf-8"))
        except Exception: return {}
    return {}

def main():
    if not SRC.exists():
        print("no existe", SRC); return 2
    lines = [l.strip() for l in SRC.read_text(encoding="utf-8", errors="ignore").splitlines()]
    keys = [l for l in lines if l and not l.startswith("#") and RX.match(l)]
    if not keys:
        print("no encontre llaves validas en el archivo (formato gsk_...)"); return 2

    secrets = load_secrets()
    existing = set(secrets.get(PROV, {}).values())
    existing.add(os.environ.get("GROQ_API_KEY", ""))
    n = 1
    added = 0
    print(f"llaves encontradas en archivo: {len(keys)}")
    for k in keys:
        if k in existing:
            print(f"  DUPLICADA  {h(k)}  {mask(k)}")
            continue
        ok, info = validate(k)
        tag = "OK " if ok else "XX "
        print(f"  {tag} {h(k)}  {mask(k)}  ->  {info}")
        if ok:
            while f"GROQ_API_KEY_{n}" in secrets.get(PROV, {}) or n == 1:
                n += 1
            secrets.setdefault(PROV, {})[f"GROQ_API_KEY_{n}"] = k
            existing.add(k); added += 1; n += 1
    SECRETS.parent.mkdir(parents=True, exist_ok=True)
    SECRETS.write_text(json.dumps(secrets, indent=2, ensure_ascii=False), encoding="utf-8")
    total = len(secrets.get(PROV, {}))
    print(f"\nañadidas: {added}  |  total Groq en rotacion: {total}  |  {SECRETS}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
