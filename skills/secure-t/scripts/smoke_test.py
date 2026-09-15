#!/usr/bin/env python3
"""
smoke_test.py — Valida API keys DeepSeek-compatibles SIN gastar tokens.

El endpoint /models no consume quota: sirve para verificar que una key
funciona y contra que proveedores (DeepSeek, SiliconFlow, Novita, OpenRouter).

Uso:
  python smoke_test.py
  python smoke_test.py sk-mi-key  (si no quieres que pregunte)
"""

import os
import sys
import urllib.request
import urllib.error

# (nombre, url_models, header_de_auth)
PROVIDERS = [
    ("DeepSeek oficial", "https://api.deepseek.com/models", "Authorization"),
    ("SiliconFlow",      "https://api.siliconflow.cn/v1/models", "Authorization"),
    ("Novita AI",        "https://api.novita.ai/v3/openai/models", "Authorization"),
    ("OpenRouter",       "https://openrouter.ai/api/v1/models", "Authorization"),
    ("Groq",             "https://api.groq.com/openai/v1/models", "Authorization"),
]


def test(provider: str, url: str, header: str, key: str, timeout: int = 10) -> str:
    req = urllib.request.Request(url)
    if key:
        req.add_header(header, f"Bearer {key}")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return f"OK  ({resp.status})"
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "ignore")[:80]
        return f"FAIL ({e.code}) {body}"
    except Exception as e:
        return f"ERROR {e}"


def main():
    key = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not key:
        key = input("Pega tu API key (Enter para probar solo endpoints publicos): ").strip()
    print(f"\nProbando key {'*' * 8 + key[-4:] if key else '(sin key)'} contra {len(PROVIDERS)} proveedores:\n")
    for name, url, header in PROVIDERS:
        result = test(name, url, header, key)
        print(f"  {name:16} {url:42} -> {result}")
    print("\nNota: /models NO consume tokens. Si OK, la key es valida para ese proveedor.")


if __name__ == "__main__":
    main()
