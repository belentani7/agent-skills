# Subagent Driven Development

Ejecutar tareas en subagentes en paralelo para acelerar work en repos múltiples simultáneamente. Cada agente opera independiente sin bloquear context principal.

## Token Economy
- Usar subagentes para trabajos largos (>10 pasos secuenciales)
- Delegar lectura de estructura + análisis → resultados comprimidos
- Nunca delegar lo que se puede hacer con un solo comando
