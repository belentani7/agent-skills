---
name: code-review-checklist
description: Revisar cambios de código (PR, merge request o diff local) con enfoque en corrección, regresiones, tests, cambios de API arriesgados y mantenibilidad. Usar cuando el usuario pida revisar un diff, PR o merge request.
---

# Revisión de código con checklist

Aplica a pull requests, merge requests y diffs locales.

## Checklist
1. **Corrección**: ¿el cambio cumple exactamente lo que promete? ¿hay caminos sin cubrir (condiciones límite, errores)?
2. **Regresiones**: ¿rompe comportamiento existente que el usuario no pidió tocar? Verifica con diff contra la base.
3. **Tests**: ¿hay tests para el cambio? ¿se ejecutan y pasan? Si no hay cobertura de la lógica nueva, señalarlo.
4. **API y contratos**: ¿cambia firmas, nombres o formatos de datos que otros módulos consumen?
5. **Mantenibilidad**: ¿código claro, sin duplicación innecesaria, siguiendo convenciones del proyecto?
6. **Seguridad**: entradas de usuario, inyección, secretos (nunca loguear claves).
7. **Consistencia del estilo**: respetar el estilo existente; no introducir estilos nuevos sin motivo.

## Formato de salida
- Lista priorizada: Crítico / Importante / Menor / Nit.
- Cada punto: ruta:línea del problema, qué está mal, y una corrección concreta sugerida.

## Medición
- Terminado = todas las áreas de la checklist revisadas y al menos un veredicto: aprobar, aprobar con cambios o rechazar con motivos.