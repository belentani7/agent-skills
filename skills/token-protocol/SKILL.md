---
name: token-protocol
description: >-
  Protocolo anti-quema de tokens para Qwen Code CLI / ModelStudio Token Plan. Aplicar SIEMPRE: sesiones cortas por tarea, /compact a ~25K, thinking OFF en tier barato, ventanas de contexto reducidas (flash 32K, medio 64K). Trigger: cualquier sesión de Qwen Code, consumo alto de cachedTokens, arranque de sesión nueva.
---

# token-protocol

Protocolo permanente contra la quema de tokens (ModelStudio Token Plan).

## Por qué existe

2026-08-25: una sola sesión quemó 72.5M tokens cached (96.5% del input, 75.1M total) en un día. Causa: ventana de contexto 1M → el CLI nunca compacta → ~46K de contexto reenviado en CADA turno (cache input facturado).

## Reglas duras (todas obligatorias)

1. **Sesión nueva por tarea.** Cerrar al terminar. Prohibido dejar sesión abierta entre tareas o días.
2. **/compact al superar ~25K de contexto.** Nunca dejar crecer el contexto.
3. **Thinking OFF por defecto.** Tier barato = sin razonamiento. Solo activar thinking en tareas que lo exijan (y revertir después).
4. **Ventanas reducidas** (ya aplicado en settings.json):
   - barato (deepseek-v4-flash-0731, deepseek-v3.2, qwen3.6-flash): 32768, thinking=false
   - medio (glm-5.2, deepseek-v4-pro, qwen3.7-plus, kimi-k2.7-code): 65536
   - flagship (qwen3.7-max, qwen3.8-max): último recurso, preguntar antes
   - Subir ventana puntualmente solo si la tarea lo necesita; revertir después.
5. **Verificar consumo cada sesión**: `/stats`. Si `cachedTokens` crece >30% del input, compactar o nueva sesión.
6. **No arrancar MCP con keys placeholder** (figma/google-drive/magic en settings.json) — solo ruido y errores.
7. **Modelos de terceros** (deepseek/glm/kimi) pueden facturar distinto al plan Qwen: ante duda, usar qwen3.6-flash.
8. **Caveman / respuestas cortas** bajo demanda: menos tokens de salida.

## Checklist de arranque de sesión

- [ ] ¿Sesión nueva? (nunca reanudar la de ayer)
- [ ] ¿Modelo barato? (flash por defecto)
- [ ] ¿Thinking desactivado?
- [ ] ¿MCPs solo los necesarios?

## Verificación semanal

Revisar `~/.qwen/usage/token-usage-*.jsonl`: sumar `cachedTokens` por día. Si >30% del input o consumo total alto, aplicar /compact más agresivo y sesiones más cortas.
