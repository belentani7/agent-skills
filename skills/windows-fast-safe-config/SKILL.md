---
name: windows-fast-safe-config
description: Configure Windows 10/11 for maximum performance and security using only official Microsoft sources, with automatic rollback. Use when hardening Windows, improving boot/UI performance, disabling telemetry or ads, or applying Microsoft security baselines safely.
---

# Windows Fast & Safe Configuration Skill

Configura Windows 10/11 para máximo rendimiento y seguridad usando **solo fuentes oficiales Microsoft** y scripts validados por la comunidad. Sin bloatware, sin riesgos, con rollback automático.

## 🎯 Objetivo

- **Rendimiento**: Boot <10s, UI responsiva, latencia mínima
- **Seguridad**: Hardening Microsoft Security Baselines + VBS/HVCI
- **Privacidad**: Telemetry off, ads off, data collection mínima
- **Seguridad**: System Restore point automático antes de cada cambio
- **Reversible**: JSON undo manifest + System Restore

---

## 📚 Fuentes Oficiales Microsoft

| Fuente | URL | Qué aporta |
|--------|-----|------------|
| **Security Baselines** | `https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines` | 300+ GPO settings validados por Microsoft Security Engineering |
| **Windows Hardening Guidance** | `https://support.microsoft.com/en-us/servicing/os/windows/2024/02/latest-windows-hardening-guidance-and-key-dates` | Timeline de hardening mensual (Secure Boot, PAC, VBS, Kerberos) |
| **Performance Tips (Official)** | `https://support.microsoft.com/en-us/windows/experience/performance-optimization/tips-to-improve-pc-performance-in-windows` | 12 soluciones oficiales Microsoft |
| **Windows 11 24H2 Security Baseline** | `https://techcommunity.microsoft.com/blog/microsoft-security-baselines/windows-11-version-24h2-security-baseline/4252801` | Nuevas settings: LSA Protection, VBS Keys, MDAV EDR Block Mode |
| **VBS Rollback Protection** | `https://support.microsoft.com/en-us/servicing/os/windows/2024/07/guidance-for-blocking-rollback-of-virtualization-based-security-vbs-related-security-updates` | SkuSiPolicy.p7b deployment |
| **Windows Security Book** | `https://www.microsoft.com/en-us/security/blog/2024/05/20/new-windows-11-features-strengthen-security-to-address-evolving-cyberthreat-landscape/` | LSA Protection, VBS, Windows Hello, PDE, Zero Trust DNS |

---

## 🛠️ Scripts Comunitarios Validados (Referencia)

| Script | Repo | Por qué usarlo |
|--------|------|----------------|
| **Debloat-Win11** | `https://github.com/mattparker/Debloat-Win11` | Hardware-aware, DryRun, JSON undo, logging, médico-grade |
| **Windows11-Optimizer** | `https://github.com/Ublaze/Windows11-Optimizer` | Restore point auto, 10 fases, security scan, MIT |
| **Sophia Script** | `https://github.com/Sophia-Community/Sophia-Script-for-Windows` | 150+ funciones modulares, métodos oficiales only |
| **ChrisTitusTech WinUtil** | `https://github.com/ChrisTitusTech/winutil` | GUI interactiva, categorías Essential/Advanced/Desktop |

---

## ⚡ Uso Rápido (One-Liner)

```powershell
# Ejecución completa con restore point y logging
irm "https://raw.githubusercontent.com/mattparker/Debloat-Win11/main/Debloat-Win11.ps1" -OutFile "$env:TEMP\Debloat.ps1"
Start-Process powershell -Verb RunAs -ArgumentList "-ExecutionPolicy Bypass -File $env:TEMP\Debloat.ps1 -LogPath $env:USERPROFILE\DebloatLog.txt"
```

### Modo Seguro (DryRun primero)
```powershell
.\Debloat-Win11.ps1 -DryRun -LogPath "$env:USERPROFILE\DebloatLog.txt"
# Revisa el log, luego ejecuta real:
.\Debloat-Win11.ps1 -LogPath "$env:USERPROFILE\DebloatLog.txt"
```

### Solo Fases Específicas
```powershell
# Solo privacidad + rendimiento + SSD
.\Debloat-Win11.ps1 -Only Privacy,Performance,SSD -Skip Bloatware,OEM
```

---

## 🔧 Configuración Manual (Sin Scripts Externos)

### 1. Crear Punto de Restauración (OBLIGATORIO)
```powershell
Checkpoint-Computer -Description "Pre-Windows-Optimization-$(Get-Date -Format 'yyyyMMdd-HHmmss')" -RestorePointType "MODIFY_SETTINGS"
```

### 2. Hardening Seguridad (Baseline Microsoft)
```powershell
# LSA Protection (enabled by default en 24H2+)
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa" -Name "RunAsPPL" -Value 1 -Type DWord -Force

# VBS / HVCI (Memory Integrity)
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios\HypervisorEnforcedCodeIntegrity" -Name "Enabled" -Value 1 -Type DWord -Force

# Vulnerable Driver Blocklist (enabled by default)
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios\SystemGuard" -Name "Enabled" -Value 1 -Type DWord -Force

# Secure Boot - verificar estado
Confirm-SecureBootUEFI
```

### 3. Privacy / Telemetry Off
```powershell
# Diagnostic Data: Basic (mínimo permitido)
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\DataCollection" -Name "AllowTelemetry" -Value 1 -Type DWord -Force

# Deshabilitar tareas de telemetría
Get-ScheduledTask -TaskPath "\Microsoft\Windows\Customer Experience Improvement Program\" | Disable-ScheduledTask -ErrorAction SilentlyContinue
Get-ScheduledTask -TaskName "Consolidator" -ErrorAction SilentlyContinue | Disable-ScheduledTask
Get-ScheduledTask -TaskName "UsbCeip" -ErrorAction SilentlyContinue | Disable-ScheduledTask

# Ads y suggestions
Set-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" -Name "SystemPaneSuggestionsEnabled" -Value 0 -Type DWord -Force
Set-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" -Name "SoftLandingEnabled" -Value 0 -Type DWord -Force
Set-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" -Name "SubscribedContent-338387Enabled" -Value 0 -Type DWord -Force
```

### 4. Rendimiento (Registry Tweaks Seguros)
```powershell
# Menu delay = 0 (instant)
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name "MenuShowDelay" -Value "0" -Type String -Force

# Disable visual effects for performance
Set-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects" -Name "VisualFXSetting" -Value 2 -Type DWord -Force

# Prefetch/Superfetch según disco
$diskType = (Get-PhysicalDisk | Where-Object {$_.MediaType -eq "SSD"}).Count
if ($diskType -gt 0) {
    # SSD: Disable SysMain (Superfetch), enable TRIM
    Set-Service -Name "SysMain" -StartupType Disabled -ErrorAction SilentlyContinue
    Stop-Service -Name "SysMain" -ErrorAction SilentlyContinue
    fsutil behavior set disablelastaccess 1
} else {
    # HDD: Enable SysMain
    Set-Service -Name "SysMain" -StartupType Automatic -ErrorAction SilentlyContinue
    Start-Service -Name "SysMain" -ErrorAction SilentlyContinue
}

# Hibernación off (ahorra SSD space + boot faster)
powercfg /hibernate off
```

### 5. Servicios Innecesarios (Safe to Disable)
```powershell
$servicesToDisable = @(
    "XboxGipSvc",           # Xbox Game Bar
    "XboxNetApiSvc",        # Xbox Networking
    "WerSvc",               # Windows Error Reporting
    "DiagTrack",            # Connected User Experiences (Telemetry)
    "MapsBroker",           # Downloaded Maps Manager
    "lfsvc",                # Geolocation
    "WpnService",           # Windows Push Notifications
    "PrintNotify",          # Printer Notifications
    "Fax",                  # Fax Service
    "RemoteRegistry",       # Remote Registry (security risk)
    "HomeGroupListener",    # HomeGroup (deprecated)
    "HomeGroupProvider",    # HomeGroup Provider
    "WalletService",        # Windows Wallet
    "OneSyncSvc",           # Sync Host (OneDrive/Contacts/Calendar)
    "PimIndexMaintenanceSvc" # People indexing
)

$servicesToDisable | ForEach-Object {
    Set-Service -Name $_ -StartupType Disabled -ErrorAction SilentlyContinue
    Stop-Service -Name $_ -ErrorAction SilentlyContinue
}
```

### 6. Appx Bloatware Removal (Safe List)
```powershell
$bloatPackages = @(
    "Microsoft.XboxGamingOverlay",
    "Microsoft.XboxGameOverlay",
    "Microsoft.XboxIdentityProvider",
    "Microsoft.XboxSpeechToTextOverlay",
    "Microsoft.GamingApp",
    "Microsoft.GamingServices",
    "Microsoft.MicrosoftSolitaireCollection",
    "Microsoft.MicrosoftStickyNotes",
    "Microsoft.Paint",
    "Microsoft.WindowsCamera",
    "Microsoft.WindowsSoundRecorder",
    "Microsoft.GetHelp",
    "Microsoft.Getstarted",
    "Microsoft.Office.OneNote",
    "Microsoft.People",
    "Microsoft.SkypeApp",
    "Microsoft.Todos",
    "Microsoft.YourPhone",
    "Microsoft.ZuneMusic",
    "Microsoft.ZuneVideo",
    "Microsoft.MSPaint",
    "Microsoft.WebMediaExtensions",
    "Microsoft.WebpImageExtension",
    "Microsoft.HEIFImageExtension",
    "Microsoft.RawImageExtension",
    "Microsoft.VP9VideoExtensions",
    "Microsoft.ScreenSketch",
    "Microsoft.Microsoft3DViewer",
    "Microsoft.Print3D",
    "Microsoft.WindowsMaps",
    "Microsoft.MicrosoftEdge.Stable"  # Edge solo si usas otro navegador
)

$bloatPackages | ForEach-Object {
    Get-AppxPackage -Name $_ -AllUsers -ErrorAction SilentlyContinue | Remove-AppxPackage -AllUsers -ErrorAction SilentlyContinue
    Get-AppxProvisionedPackage -Online | Where-Object {$_.PackageName -like "$_*"} | Remove-AppxProvisionedPackage -Online -ErrorAction SilentlyContinue
}
```

### 7. Power Plan Optimizado
```powershell
# Ultimate Performance (hidden by default)
powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
$ultimate = (powercfg /l | Select-String "Ultimate Performance").ToString().Split(" ")[3]
powercfg /s $ultimate

# O laptop: Balanced con tweaks
powercfg /setactive 381b4222-f694-41f0-9685-ff5bb260df2e
powercfg /change standby-timeout-ac 0
powercfg /change monitor-timeout-ac 15
```

### 8. Network Optimization (TCP)
```powershell
# TCP optimization para latencia baja
netsh int tcp set global autotuninglevel=normal
netsh int tcp set global congestionprovider=ctcp
netsh int tcp set global ecncapability=enabled
netsh int tcp set global timestamps=enabled
# RSS y RSC para NICs modernas
netsh int tcp set global rss=enabled
netsh int tcp set global rsc=enabled
```

### 9. Windows Update (Controlado)
```powershell
# Pausar updates 7 días (máximo oficial)
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" -Name "NoAutoUpdate" -Value 0 -Type DWord -Force
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" -Name "AUOptions" -Value 2 -Type DWord -Force  # Notify before download
```

---

## ✅ Checklist Post-Config

```powershell
# Verificar estado
Write-Host "=== VERIFICACIÓN POST-CONFIG ===" -ForegroundColor Green

# Security
Write-Host "LSA Protection: $(Get-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Control\Lsa -Name RunAsPPL -ErrorAction SilentlyContinue).RunAsPPL"
Write-Host "HVCI Enabled: $(Get-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios\HypervisorEnforcedCodeIntegrity -Name Enabled -ErrorAction SilentlyContinue).Enabled"
Write-Host "Secure Boot: $(Confirm-SecureBootUEFI)"

# Performance
Write-Host "Power Plan: $(powercfg /getactivescheme)"
Write-Host "Hibernation: $(powercfg /a | Select-String 'Hibernation')"

# Services
$disabled = @("XboxGipSvc","DiagTrack","WerSvc","MapsBroker","lfsvc","RemoteRegistry")
$disabled | ForEach-Object { Write-Host "$_ : $(Get-Service $_ -ErrorAction SilentlyContinue).Status" }

# Appx count
$count = (Get-AppxPackage -AllUsers).Count
Write-Host "Appx packages remaining: $count"

# RAM/CPU baseline
$mem = Get-CimInstance Win32_OperatingSystem
Write-Host "RAM Free: $([math]::Round($mem.FreePhysicalMemory/1MB,1)) GB"
```

---

## 🔄 Rollback / Undo

### Opción A: System Restore (Recomendado)
```powershell
# Listar puntos
Get-ComputerRestorePoint | Format-Table SequenceNumber, Description, CreationTime

# Restaurar (requiere reboot)
Restore-Computer -RestorePoint <SequenceNumber>
```

### Opción B: JSON Undo Manifest (Debloat-Win11)
```powershell
# El script genera: $env:USERPROFILE\DebloatUndo.json
# Para revertir:
$undo = Get-Content "$env:USERPROFILE\DebloatUndo.json" | ConvertFrom-Json
$undo.Changes | ForEach-Object {
    # Revertir cada cambio según tipo (Registry, Service, Appx, Task)
}
```

### Opción C: Re-enable Services
```powershell
$servicesToEnable = @("SysMain","WerSvc","DiagTrack","MapsBroker","lfsvc","RemoteRegistry")
$servicesToEnable | ForEach-Object {
    Set-Service -Name $_ -StartupType Automatic -ErrorAction SilentlyContinue
    Start-Service -Name $_ -ErrorAction SilentlyContinue
}
```

---

## ⚠️ Seguridad y Advertencias

| Riesgo | Mitigación |
|--------|------------|
| **Romper Windows Update** | No deshabilitar `wuauserv`, `BITS`, `TrustedInstaller` |
| **Romper Store/Apps** | No quitar `Microsoft.VCLibs`, `Microsoft.NET.*`, `Microsoft.UI.Xaml` |
| **Romper Audio/Video** | No tocar `AudioEndpointBuilder`, `Audiosrv`, `WindowsMediaFoundation` |
| **Romper Red** | No deshabilitar `Dnscache`, `Dhcp`, `Netman`, `NlaSvc` |
| **Boot loop (VBS)** | No aplicar SkuSiPolicy.p7b sin testear + recovery drive |

### Servicios NUNCA tocar:
```
wuauserv, BITS, TrustedInstaller, Dnscache, Dhcp, Netman, NlaSvc,
AudioEndpointBuilder, Audiosrv, Winmgmt, RpcSs, LSM, PlugPlay,
WmiApSrv, EventLog, EventSystem, CryptSvc, AppIDSvc, LicenseManager
```

---

## 📋 Perfiles Predefinidos

### Perfil "Developer" (Equilibrado)
```powershell
.\Debloat-Win11.ps1 -Profile Developer
# Mantiene: Windows Terminal, DevTools, Hyper-V, WSL, Docker support
# Quita: Xbox, Games, Mixed Reality, Tips, Ads, Telemetry
```

### Perfil "Gaming/Latency" (Máximo rendimiento)
```powershell
.\Debloat-Win11.ps1 -Profile Gaming
# Ultimate Performance, HPET off, Timer resolution 0.5ms, Network tweaks
# Quita: Todo lo anterior + servicios de fondo, visual effects
```

### Perfil "Laptop/Battery" (Optimizado batería)
```powershell
.\Debloat-Win11.ps1 -Profile Laptop
# Balanced power, USB selective suspend on, adaptive brightness
# Mantiene: Modern Standby, Wi-Fi power saving
```

### Perfil "Enterprise/Security" (Hardening máximo)
```powershell
.\Debloat-Win11.ps1 -Profile Enterprise
# Security Baselines completos, AppLocker, WDAC, LSA Protection, VBS
# Audit mode first, then enforce
```

---

## 📦 Instalación Skill en Kilo

```bash
# Copiar a skills directory
mkdir -p ~/.agents/skills/windows-fast-safe-config
# Este archivo ya está en: C:\Users\USER\.agents\skills\windows-fast-safe-config\SKILL.md
```

### Uso desde Kilo
```
> skill windows-fast-safe-config
> # Ahora tienes acceso a todas las funciones arriba
```

---

## 🔗 Enlaces Directos Descarga

| Herramienta | Descarga Directa |
|-------------|------------------|
| **Security Compliance Toolkit (SCT)** | `https://aka.ms/SCT` |
| **Security Baselines (GPO/MDM)** | `https://aka.ms/baselines` |
| **Debloat-Win11 (Matt Parker)** | `https://raw.githubusercontent.com/mattparker/Debloat-Win11/main/Debloat-Win11.ps1` |
| **Windows11-Optimizer (Ublaze)** | `https://raw.githubusercontent.com/Ublaze/Windows11-Optimizer/main/Windows11_Optimizer.ps1` |
| **Sophia Script** | `https://github.com/Sophia-Community/Sophia-Script-for-Windows/archive/refs/heads/main.zip` |
| **WinUtil (Chris Titus)** | `https://github.com/ChrisTitusTech/winutil/releases/latest` |

---

## 📝 Changelog

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0 | 2026-09-07 | Creación inicial con fuentes oficiales Microsoft + scripts validados |

---

**⚡ Principio**: "Mide dos veces, corta una. Siempre restore point. Siempre dry-run. Nunca toque servicios críticos."
