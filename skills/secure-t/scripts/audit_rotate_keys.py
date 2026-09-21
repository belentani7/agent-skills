#!/usr/bin/env python3
"""
audit_rotate_keys.py — Auditoria y rotacion de API keys en .env (multiplataforma).

Acciones (solo archivos que TU indiques, nada se envia a internet):
  1. scan    : detecta keys por patron en .env/config de un directorio
  2. rotate  : regenera una key aleatoria y actualiza el .env con backup atomico
  3. report  : genera reporte CSV con keys enmascaradas y antiguedad

Uso:
  python audit_rotate_keys.py scan   C:\\proyectos
  python audit_rotate_keys.py rotate C:\\proyectos\\.env  OPENAI_API_KEY
  python audit_rotate_keys.py report C:\\proyectos
"""

import csv
import re
import secrets
import shutil
import sys
from datetime import datetime
from pathlib import Path

PATTERNS = {
    "OpenAI":        re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    "GitHub":        re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    "AWS AccessKey": re.compile(r"AKIA[0-9A-Z]{16}"),
    "AWS Secret":    re.compile(r"(?i)aws_secret(_access)?_key[\"']?\s*[:=]\s*[\"'][A-Za-z0-9/+=]{40}"),
    "Google API":    re.compile(r"AIza[0-9A-Za-z_-]{35}"),
    "Slack":         re.compile(r"xox[baprs]-[0-9A-Za-z-]{10,}"),
    "Telegram Bot":  re.compile(r"[0-9]{8,10}:[A-Za-z0-9_-]{35}"),
    "Stripe":        re.compile(r"sk_live_[0-9a-zA-Z]{20,}"),
    "DeepSeek":      re.compile(r"sk-[a-f0-9]{32,64}"),
    "Generic":       re.compile(r"(?i)(api[_-]?key|token)[\"']?\s*[:=]\s*[\"'][A-Za-z0-9._-]{16,}[\"']"),
}

IGNORE_DIRS = {"node_modules", ".git", "venv", "__pycache__", "dist", "build"}

CONFIG_FILES = ("*.env", "*.env.*", "*.ini", "*.conf", "*.cfg", "*.yaml", "*.yml", "*.json", "*.toml")


def iter_config_files(root: Path):
    for pat in CONFIG_FILES:
        for f in root.rglob(pat):
            parts = set(f.parts)
            if parts & IGNORE_DIRS:
                continue
            yield f


def mask(secret: str) -> str:
    return secret[:6] + "***" + secret[-4:] if len(secret) > 12 else "***"


def scan(root: Path) -> list:
    hits = []
    for f in iter_config_files(root):
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for line_no, line in enumerate(text.splitlines(), 1):
            for kind, pat in PATTERNS.items():
                for m in pat.finditer(line):
                    hits.append({
                        "tipo": kind,
                        "archivo": str(f),
                        "linea": line_no,
                        "key": mask(m.group(0)),
                    })
    return hits


def rotate(env_file: Path, var_name: str) -> bool:
    """Regenera una variable en un .env con backup atomico."""
    if not env_file.exists():
        print(f"[!] No existe {env_file}")
        return False
    lines = env_file.read_text(encoding="utf-8").splitlines()
    new_key = secrets.token_urlsafe(32)
    replaced = False
    for i, line in enumerate(lines):
        if line.strip().startswith(var_name + "=") or line.strip().startswith(var_name + " ="):
            lines[i] = f"{var_name}={new_key}"
            replaced = True
    if not replaced:
        lines.append(f"{var_name}={new_key}")
    backup = env_file.with_suffix(env_file.suffix + f".bak-{datetime.now():%Y%m%d%H%M%S}")
    shutil.copy2(env_file, backup)
    tmp = env_file.with_suffix(env_file.suffix + ".tmp")
    tmp.write_text("\n".join(lines) + "\n", encoding="utf-8")
    tmp.replace(env_file)
    print(f"[+] {var_name} rotada en {env_file}")
    print(f"[+] Nueva key: {mask(new_key)} (guarda la real en tu secret manager)")
    print(f"[+] Backup: {backup}")
    return True


def report(root: Path, out_csv: str):
    hits = scan(root)
    now = datetime.now().isoformat(timespec="seconds")
    with open(out_csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["fecha", "tipo", "archivo", "linea", "key"])
        w.writeheader()
        for h in hits:
            w.writerow({"fecha": now, **h})
    print(f"[*] {len(hits)} credenciales detectadas -> {out_csv}")
    for h in hits:
        print(f"  {h['tipo']:15} {h['archivo']}:{h['linea']}  {h['key']}")


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    action = sys.argv[1]
    path = Path(sys.argv[2])
    if action == "scan":
        for h in scan(path):
            print(f"  {h['tipo']:15} {h['archivo']}:{h['linea']}  {h['key']}")
    elif action == "rotate" and len(sys.argv) == 4:
        rotate(path, sys.argv[3])
    elif action == "report":
        report(path, str(path / "api-keys-report.csv"))
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
