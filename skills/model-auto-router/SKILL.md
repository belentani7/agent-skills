---
name: model-auto-router
description: "Elige automaticamente el modelo/proveedor LLM mas barato capaz de resolver la tarea, con cadena de fallback entre las APIs verificadas del usuario. Trigger: 'que modelo uso', 'routing de modelos', 'abaratar tokens', 'fallback de proveedor', 'auto-router', 'modelo adecuado', 'optimiza coste LLM', o al arrancar tarea grande donde importe el coste."
---

# model-auto-router

Politica de enrutado de modelos. Objetivo: **maxima capacidad cuando la tarea la exige,
minimo coste el resto del tiempo.** Documentacion completa en `~/.config/opencode/router/`:
`MAP.md`, `CONTEXT.md`, `PROMPT.md`, `REPOS.md`.

## Regla de oro

1. Empieza por el **tier gratis** con key verificada.
2. Sube de tier **solo** si la tarea lo justifica (ver `router/MAP.md`).
3. Nunca Qwen / Alibaba / Bailian.
4. Cache de prompt siempre activo; compactar a ~25K; salida en `caveman`.
5. Con modelos de razonamiento, `max_tokens >= 2000` (si no, devuelven content vacio).

## Proveedores verificados por chat completion (2026-09-15)

| Proveedor | Env var | Estado | Modelos validos |
|---|---|---|---|
| Groq | `GROQ_API_KEY` | OK | `openai/gpt-oss-120b`, `openai/gpt-oss-20b`, `groq/compound`, `groq/compound-mini` |
| Z.ai | `Z_AI_API_KEY` | OK | `glm-4.5-flash` (gratis) |
| Morph | `MORPH_API_KEY` | OK | `morph-dsv41flash`, `auto`, `morph-glm52-744b` |
| DeepSeek | `DEEPSEEK_API_KEY` | OK | `deepseek-chat`, `deepseek-reasoner`, `deepseek-v4-pro` |
| NVIDIA NIM | `NVIDIA_API_KEY` / `NVIDIA_ALT_KEY` | OK | `nvidia/nemotron-*` |
| OpenRouter | `OPENROUTER_API_KEY` | OK | `openrouter/auto`, modelos `:free` (saldo ~$0.97) |
| Anthropic | `ANTHROPIC_API_KEY` | OK | `claude-sonnet-4-5` (caro) |

Caidos / no usar:

| Proveedor | Sintoma | Accion |
|---|---|---|
| Cerebras | `402 Payment Required` | free tier agotado; fuera de la cadena |
| Google Gemini | `400 API key invalida` | rotar `GOOGLE_API_KEY` |
| OpenAI | `401 Incorrect API key` | rotar `OPENAI_API_KEY` |
| OpenZen | DNS inexistente | deshabilitar |
| Qwen / Bailian | regla del usuario | `qwen-token-plan` en `disabled_providers` |

## Matriz tarea a modelo

| Tarea | Proveedor | Modelo |
|---|---|---|
| Trivial (rename, formato, resumen) | groq | `openai/gpt-oss-20b` |
| Codigo normal, refactor, tests | groq | `openai/gpt-oss-120b` |
| Clasificar, extraer, JSON | zai | `glm-4.5-flash` |
| Edicion mecanica multi-archivo | morph | `morph-dsv41flash` |
| Razonamiento largo / arquitectura | morph | `morph-glm52-744b` o `auto` |
| Matematica / prueba / algoritmo | deepseek | `deepseek-reasoner` |
| Juicio critico (auditoria, seguridad) | anthropic | `claude-sonnet-4-5` |

## Cuando SI necesitas deepseek-v4-pro (o tier 3+)

Solo 4 casos: (1) razonamiento largo/arquitectura, (2) depuracion dificil tras 2 fallos
del tier bajo, (3) juicio critico o decision irreversible, (4) ambiguedad real de requisitos.
Fuera de eso es gasto puro.

## Cadena de fallback

`groq` -> `zai` -> `morph` -> `deepseek` -> `openrouter` -> `anthropic`

## Script

```bash
python scripts/route.py "refactoriza el modulo de auth y anade tests"
# -> tier, proveedor, modelo, env var, cadena de fallback
```

## Uso

1. `router/MAP.md` para la tabla completa.
2. `router/CONTEXT.md` para el estado de keys, economia de uso y guardas de presupuesto.
3. `router/PROMPT.md` como system prompt del agente orquestador.
4. `router/REPOS.md` para gateways/routers open-source.
