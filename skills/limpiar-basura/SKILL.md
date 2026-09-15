---
name: limpiar-basura
description: "Limpieza segura de archivos basura en Windows y liberacion de espacio en disco: %TEMP%, C:\\Windows\\Temp, cache de Delivery Optimization, cache de miniaturas, cache de shaders DirectX, reportes WER, papelera de reciclaje, caches de npm/pip y WinSxS via DISM. USAR SIEMPRE que el usuario pida limpiar basura, limpiar temporales, limpiar cache, liberar espacio, liberar disco, limpiar Windows, limpiar PC, clean junk files, free up disk space, disk cleanup, o quiera recuperar GB en su equipo, aunque no use la palabra 'basura'."
platforms: [windows]
---

# limpiar-basura

Limpieza segura de archivos basura en Windows con un principio irrenunciable:
**medir -> previsualizar -> limpiar -> verificar**. Un buen limpiador solo borra
archivos que el sistema puede reconstruir solo. Nunca borres algo que no sepas
que es.

## Script incluido

`scripts/limpiar.ps1` hace el 90% del trabajo con seguridad integrada
(filtro de antiguedad, omite archivos en uso, informe antes/despues):

```powershell
.\scripts\limpiar.ps1 -ReportOnly        # PASO 1: solo mide, no borra nada
.\scripts\limpiar.ps1 -WhatIf            # muestra que archivos borraria
.\scripts\limpiar.ps1                    # limpia los objetivos seguros
.\scripts\limpiar.ps1 -DaysOld 3         # archivos con mas de 3 dias
.\scripts\limpiar.ps1 -IncludeRecycleBin # + vaciar papelera (destructivo)
.\scripts\limpiar.ps1 -IncludeDevCaches  # + npm cache clean, pip cache purge
.\scripts\limpiar.ps1 -IncludeDeliveryOptimization  # + cache de Windows Update P2P
```

Flujo obligatorio al usar la skill:
1. Ejecuta `-ReportOnly` y presenta al usuario el informe (MB por objetivo).
2. Ejecuta `-WhatIf` si el usuario quiere ver el detalle antes de decidir.
3. Ejecuta sin flags para limpiar lo seguro.
4. Reporta el espacio liberado (antes/despues).

Las acciones destructivas (`-IncludeRecycleBin`, DISM con `/ResetBase`,
desactivar hibernacion) exigen consentimiento explicito del usuario, nunca
se ejecutan por iniciativa propia.

## Objetivos y nivel de riesgo

| Objetivo | Ruta / comando | Riesgo | Admin |
|---|---|---|---|
| Temp de usuario | `%TEMP%` | Seguro | No |
| Temp de Windows | `C:\Windows\Temp` | Seguro | Parcial |
| Cache shaders DirectX | `%LOCALAPPDATA%\D3DSCache` | Seguro (se reconstruye) | No |
| Miniaturas/iconos | `%LOCALAPPDATA%\Microsoft\Windows\Explorer\thumbcache_*.db` | Seguro (algunos bloqueados por Explorer: omitir) | No |
| Reportes de errores | `%LOCALAPPDATA%\Microsoft\Windows\WER\Report*` | Seguro | No |
| Delivery Optimization | `Delete-DeliveryOptimizationCache -Force` | Seguro (cmdlet oficial) | Si |
| Papelera | `Clear-RecycleBin -Force` | Destructivo -> confirmar | No |
| Cache npm | `npm cache clean --force` | Seguro (se reconstruye) | No |
| Cache pip | `pip cache purge` | Seguro (se reconstruye) | No |
| Component store | `DISM /Online /Cleanup-Image /StartComponentCleanup` | Seguro | Si |
| Caches de navegador | `%LOCALAPPDATA%\Google\Chrome\User Data\...\Cache`, `\Microsoft\Edge\...`, `\Mozilla\Firefox\Profiles\...\cache2` | Manual: cerrar el navegador primero | No |

## NUNCA tocar

- `C:\Windows\WinSxS` a mano: borrar archivos de ahi rompe el arranque y las
  actualizaciones. Solo via `DISM /StartComponentCleanup` (Microsoft lo advierte
  explicitamente: "deleting files from the WinSxS folder may severely damage
  your system").
- `C:\Windows\System32`, `C:\Program Files`, `C:\ProgramData` generico.
- `AppData\Roaming` completo: ahi viven datos reales de aplicaciones.
- `Downloads`, `Documents`, `Desktop` ni datos de otros perfiles de usuario.
- `hiberfil.sys`, `pagefile.sys`. Desactivar hibernacion
  (`powercfg /h off`) libera GB pero es una decision del usuario: proponla, no
  la ejecutes sin consentimiento.

## Herramientas nativas de referencia

- `DISM /Online /Cleanup-Image /StartComponentCleanup`: reduce WinSxS. Sin
  `/ResetBase` mantiene la posibilidad de desinstalar updates. Con `/ResetBase`
  libera mas pero impide desinstalar updates ya instalados -> solo con
  consentimiento.
- `schtasks /Run /TN "\Microsoft\Windows\Servicing\StartComponentCleanup"`:
  equivalente con periodo de gracia de 30 dias.
- `cleanmgr /sageset:N` + `cleanmgr /sagerun:N`: Disk Cleanup automatizado
  (incluye "Windows Update Cleanup").
- `ipconfig /flushdns`: refresca cache DNS (no libera disco, se suele pedir junto).
- Storage Sense (Configuracion > Sistema > Almacenamiento): automatiza esto
  para siempre; mencionarlo como solucion permanente.

## Reglas de oro

- Edad minima 7 dias por defecto (nunca menos de 48h en Temp: Disk Cleanup de
  Windows usa ese mismo umbral).
- Archivos en uso u ocupados: omitir con `-ErrorAction SilentlyContinue`, jamas
  forzar con `taskkill`.
- Siempre medir espacio libre antes y despues, y reportarlo al usuario.
- Ante cualquier ruta fuera de la tabla de objetivos seguros: no inventes,
  pregunta al usuario primero.
