# Contrato de agente (Agent Contract)

Esquema estable entre orquestador y sub-agente. Evita texto libre no parseable.

## Entrada (Task)

```json
{
  "id": "string, unico",
  "prompt": "string, obligatorio",
  "kind": "trivial|code|classify|edit|reason|judge (opcional, se infiere)",
  "provider": "string (opcional, fuerza proveedor)",
  "model": "string (opcional, requiere provider)",
  "max_tokens": 2048,
  "system": "string (opcional)"
}
```

## Salida (Result)

```json
{
  "id": "string",
  "kind": "string",
  "provider": "string|null",
  "model": "string|null",
  "key_var": "string (nombre de variable, nunca el valor)",
  "ok": true,
  "text": "string (enmascarado)",
  "elapsed_s": 0.0,
  "tried": ["proveedor/modelo", "..."],
  "error": "string (solo si ok=false)"
}
```

## Invariantes

- `key_var` es un NOMBRE de variable de entorno, jamas una llave.
- `text` pasa por `mask()` antes de salir.
- `tried` registra la cadena de fallback intentada.
- Si `ok=false` y `error=all_failed`, se agoto la cadena.

## Herramientas (tool abstraction)

El sub-agente no recibe llaves. Recibe una tarea; el orquestador resuelve proveedor, modelo
y llave internamente. Si en el futuro se expone como MCP, cada proveedor sera un servidor
MCP y el orquestador llamara a `mcp_<provider>_chat` sin conocer la llave.
