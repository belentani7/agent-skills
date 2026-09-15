---
name: repo-hygiene
description: Auditar y mantener repositorios de GitHub de forma segura. Usar cuando el usuario pida limpiar, archivar, borrar, auditar o revisar su cuenta de GitHub o lista de repos. Evita borrar actualizaciones/mejoras propias.
---

# Auditoría y mantenimiento seguro de repositorios GitHub

Usa este skill cuando el usuario quiera limpiar, auditar, archivar o borrar repositorios de su cuenta de GitHub.

## Regla de oro
**NUNCA borres un repo que pueda contener trabajo propio.** Antes de eliminar cualquier cosa, verifica de forma concluyente que el repo es basura segura.

## Checklist de verificación previa al borrado
1. **Tamaño y contenido**: `gh api repos/{owner}/{repo}` → comprueba `size` (KB), `fork`, `parent`.
2. **Historial**: mira HEAD commit y su autor: `gh api repos/{owner}/{repo}/commits/{defaultBranch}`.
   - HEAD con autor propio y mensaje tipo *"backup: snapshot completo antes de limpieza local"* = snapshot propio → **NO borrar** (puede contener mejoras locales).
   - HEAD con autor upstream = posible clon puro de terceros.
3. **Vacíos reales**: `default_branch`, `size:0`, y sin árbol de contenido (`gh api .../git/trees/{branch}?recursive=1`). Un repo vacío de verdad no tiene ningún archivo.
4. **Contenido propio en la raíz**: lista el árbol; si hay archivos obra del usuario (PLAN.md, notebooks propios, configs firmadas por él), conservarlo.
5. **Fork**: si `fork=true`, verifica que `parent` es del upstream y que no tiene commits propios encima.

## Ejecución
- Borrado: `gh repo delete owner/repo --yes` (irreversible → solo tras verificación y consentimiento explícito).
- Registrar cada borrado con fecha en un log persistente.
- Regenerar cualquier informe/inventario después de borrar.

## Categorización rápida
- backups genéricos → revisar, no borrar a ciegas.
- clones/forks puros (0 commits propios) → candidatos, requiere verificación de HEAD.
- vacíos (0 archivos) → seguros si el usuario autoriza.
- repos de producto propio → conservar siempre.

## Medición
- Saber cuándo terminó: reportar cuántos repos se verificaron, cuántos se borraron, cuántos se conservaron y por qué.