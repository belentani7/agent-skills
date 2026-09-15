#Requires -Version 5.1
<#
.SYNOPSIS
    Limpieza segura de archivos basura en Windows.

.DESCRIPTION
    Mide, previsualiza y limpia solo objetivos seguros. Omite archivos en uso
    y por defecto no toca nada con menos de -DaysOld dias de antiguedad.
    Las acciones destructivas (papelera) van detras de flags explicitos.

.EXAMPLE
    .\limpiar.ps1 -ReportOnly
    Solo informa cuanto espacio se puede liberar. No borra nada.

.EXAMPLE
    .\limpiar.ps1 -WhatIf
    Muestra que borraria, sin borrar.

.EXAMPLE
    .\limpiar.ps1
    Limpia los objetivos seguros.

.EXAMPLE
    .\limpiar.ps1 -IncludeRecycleBin -IncludeDevCaches
    Tambien vacia la papelera y purga caches de npm/pip.
#>
[CmdletBinding()]
param(
    # Limpiar solo archivos con mas de N dias (defecto 7).
    [ValidateRange(0, 365)]
    [int]$DaysOld = 7,

    # Solo medir y reportar; no borra nada.
    [switch]$ReportOnly,

    # Vaciar tambien la papelera de reciclaje (destructivo).
    [switch]$IncludeRecycleBin,

    # Purgar caches de npm y pip via comandos oficiales.
    [switch]$IncludeDevCaches,

    # Purgar cache de Delivery Optimization (requiere admin).
    [switch]$IncludeDeliveryOptimization
)

$ErrorActionPreference = 'SilentlyContinue'

function Get-FreeBytes {
    param([string]$DriveName)
    $name = $DriveName.TrimEnd(':')
    $d = Get-PSDrive -Name $name -ErrorAction SilentlyContinue
    if ($d) { return [int64]$d.Free }
    $wmi = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='$($name):'"
    if ($wmi) { return [int64]$wmi.FreeSpace }
    return [int64]0
}

function Clean-Folder {
    param(
        [string]$Path,
        [string]$Label,
        [string[]]$FileFilter = @()
    )
    $r = [pscustomobject]@{
        Label = $Label; Path = $Path
        FoundBytes = [int64]0; FreedBytes = [int64]0
        FilesFound = 0; FilesDeleted = 0
    }
    if (-not (Test-Path -LiteralPath $Path)) { return $r }

    $cutoff = (Get-Date).AddDays(-$DaysOld)
    $files = Get-ChildItem -LiteralPath $Path -Recurse -File -Force -ErrorAction SilentlyContinue |
             Where-Object { $_.LastWriteTime -lt $cutoff -and
                            -not $_.Attributes.HasFlag([IO.FileAttributes]::ReadOnly) }
    if ($FileFilter.Count -gt 0) {
        $files = $files | Where-Object {
            $n = $_.Name
            @($FileFilter | Where-Object { $n -like $_ }).Count -gt 0
        }
    }

    $files = @($files)
    $r.FilesFound = $files.Count
    $r.FoundBytes = [int64]($files | Measure-Object Length -Sum).Sum
    if ($null -eq $r.FoundBytes) { $r.FoundBytes = [int64]0 }

    if ($ReportOnly -or $WhatIfPreference) { return $r }

    foreach ($f in $files) {
        $len = $f.Length
        Remove-Item -LiteralPath $f.FullName -Force -ErrorAction SilentlyContinue
        if (-not (Test-Path -LiteralPath $f.FullName)) {
            $r.FreedBytes += $len
            $r.FilesDeleted++
        }
    }

    # Directorios vacios resultantes (mas profundos primero).
    Get-ChildItem -LiteralPath $Path -Recurse -Directory -Force -ErrorAction SilentlyContinue |
        Sort-Object FullName -Descending |
        Where-Object {
            -not @(Get-ChildItem -LiteralPath $_.FullName -Force -ErrorAction SilentlyContinue).Count
        } |
        Remove-Item -Force -ErrorAction SilentlyContinue

    return $r
}

function Add-InfoRow {
    param([string]$Label, [string]$Path, [int64]$Bytes)
    return [pscustomobject]@{
        Label = $Label; Path = $Path
        FoundBytes = $Bytes; FreedBytes = [int64]0
        FilesFound = 0; FilesDeleted = 0
    }
}

# ---------------------------------------------------------------- main

$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()
           ).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host 'Aviso: sin privilegios de administrador; se omitira lo que los requiera.' -ForegroundColor Yellow
}

$drive = $env:SystemDrive
$before = Get-FreeBytes -DriveName $drive
$report = @()

$report += Clean-Folder -Path $env:TEMP -Label 'Temp de usuario (%TEMP%)'
$report += Clean-Folder -Path (Join-Path $env:SystemRoot 'Temp') -Label 'Temp de Windows'
$report += Clean-Folder -Path (Join-Path $env:LOCALAPPDATA 'D3DSCache') -Label 'Cache shaders DirectX'
$report += Clean-Folder -Path (Join-Path $env:LOCALAPPDATA 'Microsoft\Windows\Explorer') `
                        -Label 'Cache de miniaturas' `
                        -FileFilter @('thumbcache_*.db', 'iconcache_*.db')
$report += Clean-Folder -Path (Join-Path $env:LOCALAPPDATA 'Microsoft\Windows\WER\ReportArchive') -Label 'WER ReportArchive'
$report += Clean-Folder -Path (Join-Path $env:LOCALAPPDATA 'Microsoft\Windows\WER\ReportQueue') -Label 'WER ReportQueue'

if ($IncludeDeliveryOptimization) {
    if (Get-Command Delete-DeliveryOptimizationCache -ErrorAction SilentlyContinue) {
        if (-not $ReportOnly) {
            Delete-DeliveryOptimizationCache -Force -ErrorAction SilentlyContinue
        }
        $report += Add-InfoRow -Label 'Delivery Optimization' -Path '(cmdlet oficial)' -Bytes 0
    } else {
        Write-Host 'Delete-DeliveryOptimizationCache no disponible en esta edicion.' -ForegroundColor Yellow
    }
}

if ($IncludeRecycleBin) {
    $rbBytes = [int64]0
    try {
        $shell = New-Object -ComObject Shell.Application
        foreach ($i in $shell.Namespace(0xA).Items()) {
            $sz = $i.ExtendedProperty('System.Size')
            if ($sz) { $rbBytes += [int64]$sz }
        }
    } catch { }
    if (-not $ReportOnly) {
        Clear-RecycleBin -Force -ErrorAction SilentlyContinue
    }
    $report += Add-InfoRow -Label 'Papelera de reciclaje' -Path 'Recycle Bin' -Bytes $rbBytes
}

if ($IncludeDevCaches) {
    $npmCache = Join-Path $env:LOCALAPPDATA 'npm-cache'
    if (Test-Path $npmCache) {
        $sz = [int64]((Get-ChildItem -LiteralPath $npmCache -Recurse -File -Force |
                       Measure-Object Length -Sum).Sum)
        if (-not $ReportOnly -and (Get-Command npm -ErrorAction SilentlyContinue)) {
            cmd /c 'npm cache clean --force' 2>$null
        }
        $report += Add-InfoRow -Label 'Cache npm' -Path $npmCache -Bytes $sz
    }
    $pipCache = Join-Path $env:LOCALAPPDATA 'pip\cache'
    if (Test-Path $pipCache) {
        $sz = [int64]((Get-ChildItem -LiteralPath $pipCache -Recurse -File -Force |
                       Measure-Object Length -Sum).Sum)
        if (-not $ReportOnly -and (Get-Command pip -ErrorAction SilentlyContinue)) {
            cmd /c 'pip cache purge' 2>$null
        }
        $report += Add-InfoRow -Label 'Cache pip' -Path $pipCache -Bytes $sz
    }
}

# ---------------------------------------------------------------- informe

$report | Format-Table Label,
    @{ n = 'Encontrado (MB)'; e = { [math]::Round($_.FoundBytes / 1MB, 1) } },
    @{ n = 'Liberado (MB)';   e = { [math]::Round($_.FreedBytes / 1MB, 1) } },
    FilesFound, FilesDeleted -AutoSize

$after = Get-FreeBytes -DriveName $drive
Write-Host ("Espacio libre antes : {0:N2} GB" -f ($before / 1GB))
Write-Host ("Espacio libre ahora : {0:N2} GB" -f ($after  / 1GB))
if ($ReportOnly -or $WhatIfPreference) {
    Write-Host ('Modo informe/preview: no se ha borrado nada.') -ForegroundColor Cyan
} else {
    Write-Host ('Liberado (segundo disco): {0:N1} MB' -f (($after - $before) / 1MB)) -ForegroundColor Green
}
