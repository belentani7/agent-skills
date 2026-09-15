# audit-api-keys.ps1
# Auditoria local de API keys en tu propia maquina Windows.
# Busca .env, config.* y credenciales del sistema. NO envia nada a internet.
# Uso:  powershell -ExecutionPolicy Bypass -File audit-api-keys.ps1 [-ScanPath C:\proyectos] [-Verbose]

param(
    [string]$ScanPath = "$env:USERPROFILE",
    [string]$ReportPath = "$env:USERPROFILE\api-keys-audit.csv"
)

$ErrorActionPreference = 'SilentlyContinue'

$patterns = [ordered]@{
    'OpenAI'        = 'sk-[A-Za-z0-9_-]{20,}'
    'GitHub'        = 'gh[pousr]_[A-Za-z0-9]{20,}'
    'AWS AccessKey' = 'AKIA[0-9A-Z]{16}'
    'AWS Secret'    = '(?i)aws_secret(_access)?_key["'']?\s*[:=]\s*["''][A-Za-z0-9/+=]{40}'
    'Google API'    = 'AIza[0-9A-Za-z_-]{35}'
    'Slack'         = 'xox[baprs]-[0-9A-Za-z-]{10,}'
    'Telegram Bot'  = '[0-9]{8,10}:[A-Za-z0-9_-]{35}'
    'Stripe'        = 'sk_live_[0-9a-zA-Z]{20,}'
    'DeepSeek'      = 'sk-[a-f0-9]{32,64}'
    'Generic Bearer'= '(?i)(api[_-]?key|token)["'']?\s*[:=]\s*["''][A-Za-z0-9._-]{16,}["'']'
}

Write-Host "[*] Escaneando $ScanPath ..." -ForegroundColor Cyan
$results = @()
$files = Get-ChildItem -Path $ScanPath -Recurse -File -Include '*.env*','*.ini','*.conf','*.cfg','*.yaml','*.yml','*.json','*.properties','*.toml','*.ps1','*.py','*.ts','*.js' -ErrorAction SilentlyContinue |
    Where-Object { $_.FullName -notmatch 'node_modules|\.git\\|\\bin\\|\.cache' }

foreach ($f in $files) {
    foreach ($name in $patterns.Keys) {
        $matches = Select-String -Path $f.FullName -Pattern $patterns[$name] -AllMatches -ErrorAction SilentlyContinue
        if ($matches) {
            foreach ($m in $matches) {
                $results += [pscustomobject]@{
                    Tipo       = $name
                    Archivo    = $f.FullName
                    Linea      = $m.LineNumber
                    Enmascarado = ($m.Matches[0].Value.Substring(0, [Math]::Min(8, $m.Matches[0].Value.Length)) + '***')
                    Fecha      = (Get-Date -Format 'yyyy-MM-dd HH:mm')
                }
            }
        }
    }
}

# Windows Credential Manager
$credResults = cmdkey /list 2>$null | Select-String 'Target:'
foreach ($c in $credResults) {
    $results += [pscustomobject]@{
        Tipo = 'CredentialManager'; Archivo = ($c.ToString() -replace 'Target: ',''); Linea = '-'; Enmascarado = '(requiere elevacion para ver)'; Fecha = (Get-Date -Format 'yyyy-MM-dd HH:mm')
    }
}

$results | Export-Csv -Path $ReportPath -NoTypeInformation -Encoding UTF8
$total = $results.Count

Write-Host ""
Write-Host "==============================" -ForegroundColor Yellow
Write-Host " AUDITORIA COMPLETA" -ForegroundColor Yellow
Write-Host " Posibles credenciales: $total" -ForegroundColor White
Write-Host " Reporte: $ReportPath" -ForegroundColor White
Write-Host "==============================" -ForegroundColor Yellow

if ($total -gt 0) {
    Write-Host "`n[!] Acciones recomendadas:" -ForegroundColor Red
    Write-Host "  1. Mueve las keys a variables de entorno o secret manager (Infisical/Doppler)" -ForegroundColor White
    Write-Host "  2. ROTA las keys que aparezcan en archivos commiteables (asumelas quemadas)" -ForegroundColor White
    Write-Host "  3. Si hay keys en .env de repos git, ejecuta: gitleaks detect --source ." -ForegroundColor White
} else {
    Write-Host "[+] No se encontraron credenciales expuestas. Limpio." -ForegroundColor Green
}
