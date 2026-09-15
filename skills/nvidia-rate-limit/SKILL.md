---
name: nvidia-rate-limit
description: >-
  Presupuesto de peticiones del backend NVIDIA NIM (DeepSeek) — máximo 40 RPM, objetivo <35 RPM y ~1000 créditos de inferencia. Aplicar SIEMPRE: batch de tool calls en un solo mensaje, un script local determinista en vez de N pasos del modelo, sin subagentes paralelos innecesarios, sin lecturas repetidas, salida concisa. Trigger: cualquier sesión sobre NVIDIA DeepSeek, trabajo a escala (multi-repo/multi-archivo), o cuando el usuario pida "menos de 35 peticiones por minuto".
---

# nvidia-rate-limit

Presupuesto fijo del modelo (NVIDIA NIM / DeepSeek free tier): **40 RPM hard cap**, margen de seguridad **<35 RPM**, y un tope de ~1000 créditos de inferencia (no infinito).

## Hecho clave

Cada **turno del modelo** (asistente → respuesta) cuenta como petición. Las tool calls que vienen dentro de un mismo turno no son peticiones separadas. Por eso, ahorrar = **menos turnos**, no menos tool calls aisladas.

## Reglas duras (todas obligatorias)

1. **Batch paralelo**: N tool calls independientes se lanzan EN UN SOLO mensaje (un turno), nunca una por turno.
2. **Un script > N pasos**: cualquier operación a escala (auditar N repos, tocar N archivos) se hace con UN script local determinista (Python/bash) que itera dentro de un subproceso. Prohibido hacer la misma operación con decenas de llamadas secuenciales del modelo.
3. **Nada de subagentes paralelos** si un script local resuelve lo mismo en una llamada.
4. **Leer una sola vez**: no re-leer ni re-grep el mismo archivo/resultado. Guardar hallazgos antes de seguir.
5. **Sin exploración especulativa**: pensar el plan, luego una tanda de tool calls dirigidas. No "probar y ver".
6. **Salida corta**: respuestas concisas, sin resúmenes innecesarios. Caveman/Spanish-telegráfico bajo demanda.
7. **Operaciones largas en un subproceso**: un comando con progreso interno, no polling iterativo en turnos separados.
8. **Antes de cada tanda**: contar turnos usados en el minuto actual; si van >35, esperar/consolidar en vez de disparar otra tanda.

## Checklist de arranque (cada tarea)

- [ ] ¿Puedo resolverlo con UN script local en vez de varios turnos?
- [ ] ¿Agrupé las tool calls independientes en un solo mensaje?
- [ ] ¿Voy a reusar un resultado ya obtenido en vez de re-leer?
- [ ] ¿La salida es lo más corta que puede ser?

## Operación a escala (N repos / N archivos)

Plantilla: escribir un `.py` a `%TEMP%\opencode\` que itera sobre la lista con `subprocess.run` + imprime un resumen compacto. Una sola ejecución = un turno. Cero bucles desde el modelo.