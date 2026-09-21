#!/usr/bin/env python3
"""Descubrimiento estatico de llaves en un repo/carpeta. NO imprime valores completos.
Uso: python discover.py --path C:\\ruta\\repo [--out inventory.json]"""
import argparse
import hashlib
import json
import re
from pathlib import Path

PATTERNS = [
    ("openrouter", re.compile(r"sk-or-v1-[0-9a-z]{40,}")),
    ("nvidia",     re.compile(r"nvapi-[A-Za-z0-9_\-]{40,}")),
    ("groq",       re.compile(r"gsk_[A-Za-z0-9]{40,}")),
    ("cerebras",   re.compile(r"csk-[a-z0-9]{40,}")),
    ("anthropic",  re.compile(r"sk-ant-[A-Za-z0-9_\-]{40,}")),
    ("google",     re.compile(r"AIza[A-Za-z0-9_\-]{30,}")),
    ("github",     re.compile(r"(?:gho_|ghp_|github_pat_)[A-Za-z0-9_]{30,}")),
    ("netlify",    re.compile(r"nfp_[A-Za-z0-9]{30,}")),
    ("zai",        re.compile(r"[0-9a-f]{32}\.[A-Za-z0-9]{10,}")),
    ("hf",         re.compile(r"hf_[A-Za-z0-9]{30,}")),
    ("stripe",     re.compile(r"(?:sk_live_|pk_live_|sk_test_|pk_test_)[A-Za-z0-9]{20,}")),
    ("aws",        re.compile(r"AKIA[0-9A-Z]{16}")),
    ("slack",      re.compile(r"xox[bp]-[A-Za-z0-9\-]{20,}")),
    ("private_key",re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----")),
]
SKIP = {".git", "node_modules", "dist", "build", ".next", "__pycache__", ".venv", "venv", ".wrangler"}
TEXT_EXT = {".env", ".js", ".ts", ".tsx", ".jsx", ".py", ".json", ".yaml", ".yml", ".toml",
            ".ps1", ".sh", ".txt", ".md", ".cfg", ".ini", ".properties", ".java", ".go", ".rb"}

def scan(root: Path):
    found = {}
    for p in root.rglob("*"):
        if not p.is_file() or any(part in SKIP for part in p.parts):
            continue
        if p.suffix.lower() not in TEXT_EXT and p.name not in (".env", ".env.local", ".env.production"):
            continue
        try:
            txt = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for prov, rx in PATTERNS:
            for m in rx.finditer(txt):
                v = m.group(0)
                h = hashlib.sha256(v.encode()).hexdigest()[:8]
                found.setdefault(prov, {})[h] = {"mask": v[:7] + "..." + v[-4:], "file": str(p.relative_to(root))}
    return found

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", required=True)
    ap.add_argument("--out")
    a = ap.parse_args()
    root = Path(a.path)
    res = scan(root)
    for prov, keys in sorted(res.items()):
        print(f"=== {prov} ({len(keys)}) ===")
        for h, d in keys.items():
            print(f"  {h}  {d['mask']:20} {d['file']}")
    if not res:
        print("sin hallazgos")
    if a.out:
        Path(a.out).write_text(json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8")
        print("saved:", a.out)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
