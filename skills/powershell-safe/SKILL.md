---
name: powershell-safe
description: Escribir y ejecutar scripts de PowerShell 5.1 en Windows de forma robusta. Usar cuando haya que automatizar tareas en la terminal de Windows, manejar archivos, logs o encodings, y evitar errores clásicos de parseo y codificación.
---

# PowerShell 5.1 resistente (Windows)

Aplica a scripts y comandos en PowerShell 5.1.

## Rincón tedioso de encoding
- PowerShell 5.1 malinterpreta UTF-8 sin BOM con caracteres Unicode: pueden romper el parseo o el render.
- **Usa solo ASCII en scripts y comandos**: reemplaza símbolos no ASCII (barras █/░, acentos, → en strings literales fuera de strings normales).
- Al escribir archivos de texto desde PowerShell usa `-Encoding utf8` y strings ASCII o usa el formato correcto para el destino.

## Errores clásicos de parseo
- **NO encadenes `foreach (...)` a una canalización** (`foreach {...} | Tee-Object`) → "No se permiten elementos de canalización vacíos". Recoge resultados en un array y vuelca después con `Set-Content`.
- Buena práctica: `$out = @(); foreach(...) { $out += "..." }; $out | Set-Content log.txt`.
- Usa `-LiteralPath` para rutas con caracteres especiales y comilla siempre rutas con espacios.

## Robustez
- `if ($?)` entre comandos dependientes; `;` cuando no importa el fallo.
- Nunca loguear secretos claves.
- Destrucción: confirmar irreversible, verificar antes (`Test-Path`).
- Preferir comandos nativos con `& "ruta\exe"`.

## Medición
- Terminado = el script corre sin errores de parseo y produce el log/archivo esperado con encoding correcto.