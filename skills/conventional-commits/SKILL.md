---
name: conventional-commits
description: Escribir mensajes de commit claros y convencionales. Usar cuando el usuario pida crear un commit, escribir un mensaje de commit o estandarizar commits de un proyecto.
---

# Mensajes de commit convencionales

## Formato
`<type>(<scope>): <subject>`

- Construido en español o inglés según el proyecto; sintaxis siempre igual.
- `<subject>` en imperativo, ≤ 72 caracteres, sin punto final.

## Tipos
- `feat` — nueva funcionalidad.
- `fix` — corrección de bug.
- `refactor` — reestructuración sin cambio de comportamiento.
- `docs` — solo documentación.
- `test` — solo tests.
- `chore` — tareas de mantenimiento, dependencias, config.
- `perf` — optimización de rendimiento.
- `style` — formato/estilo sin lógica.

## Reglas
- `scope` opcional: módulo/área afectada (ej. `feat(api): agrega endpoint de login`).
- Cuerpo solo cuando el "por qué" no es obvio: explica contexto y decisión, no repitas el diff.
- No pongas emojis salvo que el proyecto los use.
- Al commitear: revisar `git status`, `git diff` y no incluir secretos.

## Medición
- Terminado = mensaje generado que sigue el formato y se puede usar directamente.