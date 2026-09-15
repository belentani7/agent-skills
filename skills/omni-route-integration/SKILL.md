---
name: omni-route-integration
description: "Routing inteligente de modelos: elige el LLM mas barato capaz de resolver la tarea y encadena fallbacks entre las APIs verificadas. Ver la skill `model-auto-router` para la politica completa."
platforms: [linux, macos, windows]
---

# omni-route-integration

Enrutado de modelos para el ecosistema Belentani. Esta skill es el punto de entrada; la
politica completa vive en `model-auto-router`.

## Que resuelve

- Elegir modelo por tarea: gratis primero, subir de tier solo si hace falta.
- Cadena de fallback entre proveedores verificados (Groq, Cerebras, OpenRouter, Morph,
  DeepSeek, Z.AI, NVIDIA, Anthropic).
- Evitar gasto innecesario (cache de prompt, compactacion, caveman).
- Regla dura: **nunca** Qwen / Alibaba / Bailian.

## Uso

1. Consulta `model-auto-router/SKILL.md` para la matriz tarea -> modelo.
2. Ejecuta `python model-auto-router/scripts/route.py "<tarea>"` para una recomendacion.
3. Si un proveedor devuelve 401/403/SSL/timeout, pasa al siguiente de la cadena.

## Verificacion de keys

`model-auto-router` incluye la lista de proveedores verificados el 2026-09-15. Rotos:
OpenAI (401), OpenZen (DNS), Google Gemini (SSL en Python; probar desde Node).

## Skills relacionadas

- model-auto-router
- multi-cli-unified
- multi-engine
- morph-migrate
- token-protocol
- nvidia-rate-limit
- openrouter-free-models
