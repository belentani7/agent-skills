#!/usr/bin/env python3
"""model-auto-router: clasifica una tarea y elige proveedor/modelo mas barato capaz.
Sin llamadas a API. Heuristica local sobre palabras clave. Uso:
    python route.py "describe la tarea"
"""
import re
import sys

# tier, provider, model, env_key
# Orden = prioridad. Reglas de alto riesgo (seguridad/razonamiento) ANTES que las de codigo.
ROUTES = [
    ("free-fast",  "groq",       "openai/gpt-oss-20b",        "GROQ_API_KEY",
     r"\b(renombra|rename|formatea|formato|resumen|summary|traduce|traducir|hola|saluda)\b"),
    ("judgment",   "anthropic",  "claude-sonnet-4-5",         "ANTHROPIC_API_KEY",
     r"\b(audita|auditoria|security|seguridad|revisa critico|vulnerabilidad|pentest|threat)\b"),
    ("reasoning",  "morph",      "morph-glm52-744b",          "MORPH_API_KEY",
     r"\b(arquitectura|architecture|disena|design|planifica|plan|razona|reason|analiza a fondo|estrategia)\b"),
    ("reasoning",  "deepseek",   "deepseek-reasoner",         "DEEPSEEK_API_KEY",
     r"\b(demuestra|prueba|proof|matematica|algoritmo|optimiza complejidad)\b"),
    ("multimodal", "anthropic",  "claude-sonnet-4-5",         "ANTHROPIC_API_KEY",
     r"\b(imagen|image|screenshot|vision|ui|diseno visual|video)\b"),
    ("free-mid",   "groq",       "openai/gpt-oss-120b",       "GROQ_API_KEY",
     r"\b(refactor|codigo|code|test|tests|funcion|function|bug|fix|arregla|implementa)\b"),
    ("free-mid",   "zai",        "glm-4.5-flash",             "Z_AI_API_KEY",
     r"\b(clasifica|clasificacion|etiqueta|extrae|json|tabla|lista)\b"),
    ("cheap",      "morph",      "morph-dsv41flash",          "MORPH_API_KEY",
     r"\b(edita|edit|patch|aplica|apply|diff|multi-archivo)\b"),
]

FALLBACK = ["groq", "zai", "morph", "deepseek", "openrouter", "anthropic"]


def choose(task: str):
    t = task.lower()
    for tier, provider, model, key, pat in ROUTES:
        if re.search(pat, t, re.IGNORECASE):
            return tier, provider, model, key
    return "cheap-default", "morph", "morph-dsv41flash", "MORPH_API_KEY"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    task = " ".join(sys.argv[1:])
    tier, provider, model, key = choose(task)
    print(f"task     : {task}")
    print(f"tier     : {tier}")
    print(f"provider : {provider}")
    print(f"model    : {model}")
    print(f"env      : {key}")
    print(f"fallback : {' > '.join(FALLBACK)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
