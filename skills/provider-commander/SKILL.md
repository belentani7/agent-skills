---
name: provider-commander
description: "Orquestador multi-proveedor con gestion de secretos, enmascarado de logs, throttling, rotacion de llaves, circuit breaker, backoff, fallback y tracking de coste. Descubre llaves en repos, sondea el catalogo de modelos gratis en vivo y reparte tareas en paralelo al modelo mas barato capaz. Trigger: 'comandante', 'orquestador', 'todas las apis', 'reparte tareas', 'fan-out', 'paralelo', 'multi-proveedor', 'que modelos gratis hay', 'organiza las llaves', 'varias keys del mismo proveedor', 'escanea llaves'."
---

# provider-commander

Orquestador multi-agente sobre todas las APIs del usuario. Secreta las llaves fuera del
prompt, elige modelo por tarea (gratis primero) y ejecuta en paralelo con resiliencia.

## Pipeline

1. **Descubrimiento** — `discover.py --path <repo>`: escaneo estatico de llaves
   (regex por proveedor). Salida enmascarada, nunca valores completos.
2. **Validacion** — `catalog.py`: sondea cada llave y el catalogo de modelos gratis
   disponible **ahora**. Escribe `commander/catalog.json`.
3. **Planificacion** — `registry.json`: cadena de fallback y tabla `routing` por tipo de
   tarea.
4. **Ejecucion** — `orchestrator.py`: reparte tareas en paralelo, rota llaves, aplica
   throttling, circuit breaker, backoff y fallback.
5. **Auditoria** — `references/usage.json`: llamadas, tokens y coste estimado por llave.
   `references/last_run.json`: resultados con la cadena `tried`.

## Capacidades de seguridad (implementadas)

- **Secretos fuera del prompt**: las llaves solo viven en env. Nunca se pasan al texto.
- **Enmascarado de logs**: `mask()` sustituye cualquier valor de llave o patron
  `sk-or-v1-`, `nvapi-`, `gsk_`, etc. en la salida de los proveedores.
- **Tool abstraction**: el sub-agente recibe tarea; el orquestador resuelve llave.
- **Aislamiento de contexto**: cada tarea es independiente; solo se agrega el resultado.
- **State cleanup**: el estado vive en memoria del proceso y muere al terminar.

## Capacidades de resiliencia (implementadas)

- **Throttling** por proveedor con ventana deslizante de 60s (`rpm` del registry).
- **Rotacion round-robin** de llaves del mismo proveedor (OpenRouter x3, NVIDIA x2).
- **Circuit breaker** por llave: 2 fallos consecutivos de red/HTTP -> 60s de cooldown;
  si todas las llaves del proveedor abren, el proveedor se salta.
- **Backoff exponencial**: 1s, 2s, 4s.
- **Fallback en cadena** por tipo de tarea (hasta 7 eslabones).
- **Tracking de coste** por llave y global.

## Uso

```bash
cd ~/.config/opencode/skills/provider-commander/scripts

python discover.py --path C:\ruta\repo --out inventory.json   # escanear llaves
python catalog.py                                             # modelos gratis en vivo
python orchestrator.py --dry-run --tasks tasks.json           # simulacion, coste 0
python orchestrator.py --tasks tasks.json                     # real, gratis primero
python orchestrator.py --compare "prompt" --providers groq,zai,openrouter
```

## Registry (registry.json)

- `chain`: orden de fallback global.
- `providers`: base, api, env vars, rpm, tier, coste, disabled+reason.
- `routing`: tipo de tarea -> lista ordenada de (proveedor, modelo).

Deshabilitados con motivo: cerebras (402), google (key invalida), openai (401),
openzen (DNS).

## Contrato de agente

Ver `references/agent-contract.md` (JSON schema de Task/Result, invariantes).

## Inventario de llaves

Ver `references/keys.md`. Resumen: OpenRouter 4 (3 vivas), NVIDIA 2, y una por proveedor
en Groq, Morph, DeepSeek, Z.ai, Anthropic. Alias detectados por hash.

## Reglas

- Gratis primero; subir tier solo justificado.
- Nunca Qwen / Alibaba / Bailian.
- `max_tokens >= 2000` con modelos de razonamiento.
- No escribir valores de llaves en disco: solo nombres de variable.
- Z.ai `glm-4.5-flash` es gratis pero lento (~200s); usar Groq para lo que importe latencia.

## Estructura

```
provider-commander/
  SKILL.md
  scripts/    discover.py · catalog.py · orchestrator.py · providers.py · commander.py · registry.json
  references/ keys.md · agent-contract.md · usage.json · last_run.json
commander/    keys_inventory.json · catalog.json   (estado runtime)
```
