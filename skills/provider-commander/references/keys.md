# Inventario de llaves — organizacion (sin valores)

Generado 2026-09-15. Los valores NO se guardan: solo nombres de variable y hashes cortos.
Rellenar la columna "cuenta" cuando se conozca el email.

## OpenRouter (4 llaves distintas, 3 vivas)

| Hash | Var principal | Alias | Estado | Saldo | Cuenta |
|---|---|---|---|---|---|
| 3838e35e | `OPENROUTER_API_KEY` | `OPENROUTER_KEY_1` | OK | ~$0.97 | (email principal) |
| c789eaff | `OPENROUTER_KEY_2` | `ANTHROPIC_AUTH_TOKEN` | OK | sin limite | (email 2?) |
| f42571c1 | `OPENROUTER_KEY_3` | `ANTHROPIC_FALLBACK_AUTH_TOKEN` | OK | sin limite | (email 3?) |
| d47286c6 | `OPENROUTER_DEMO_KEY` | — | 401 | — | muerta |

22 modelos `:free` disponibles. `openrouter/auto` elige solo y funciono.

## NVIDIA (2 llaves)

| Hash | Var | Estado | Modelos |
|---|---|---|---|
| e749041a | `NVIDIA_API_KEY` | OK | 81 |
| 9071920a | `NVIDIA_ALT_KEY` | OK | 81 |

## Una llave por proveedor

| Proveedor | Var | Alias | Estado |
|---|---|---|---|
| Groq | `GROQ_API_KEY` | — | OK (13 modelos, gratis) |
| Morph | `MORPH_API_KEY` | — | OK (23) |
| DeepSeek | `DEEPSEEK_API_KEY` | — | OK (2) |
| Z.ai | `Z_AI_API_KEY` | `ZAI_API_KEY` | OK (10) |
| Anthropic | `ANTHROPIC_API_KEY` | — | OK (11) |
| Cerebras | `CEREBRAS_API_KEY` | — | 402 pago |
| Google | `GOOGLE_API_KEY` | `GEMINI_API_KEY` | key invalida |
| OpenAI | `OPENAI_API_KEY` | — | 401 |
| OpenZen | `OPENZEN_API_KEY` | — | DNS muerto |
| GitHub | `GITHUB_TOKEN` | `GITHUB_PAT` | OK |

## Bases duplicadas

`OPENROUTER_BASE` = `OPENROUTER_BASE_URL` = `https://openrouter.ai/api/v1`.

## Acciones pendientes

1. Rotar `GOOGLE_API_KEY` (invalida) o eliminarla.
2. Rotar `OPENAI_API_KEY` (401) o eliminarla.
3. Eliminar `OPENROUTER_DEMO_KEY` (401) o dejarla fuera de la rotacion.
4. Rellenar emails/cuentas en la tabla OpenRouter.
5. Confirmar si `NVIDIA_ALT_KEY` es de otra cuenta (rotacion ya activa).
