# Instala todas las skills en cada CLI de agentes del sistema (Windows).
# Crea junctions (sin copiar) apuntando al clon del repo, para que `git pull` actualice todo.
# Uso:  .\install.ps1            (instala)
#       .\install.ps1 -Uninstall (elimina las junctions creadas)
param(
    [switch]$Uninstall
)

$ErrorActionPreference = "Stop"
$repoSkills = Join-Path $PSScriptRoot "skills"
if (-not (Test-Path $repoSkills)) { throw "No se encuentra $repoSkills" }

# Roots de skills por CLI. Se crean si no existen.
$targets = @(
    (Join-Path $HOME ".agents\skills"),                 # master agent-agnostic
    (Join-Path $HOME ".claude\skills"),                 # Claude Code
    (Join-Path $HOME ".config\opencode\skills"),        # OpenCode
    (Join-Path $HOME ".codex\skills"),                  # Codex CLI
    (Join-Path $HOME ".zcode\skills"),                  # ZCode
    (Join-Path $HOME ".gemini\skills"),                 # Gemini CLI
    (Join-Path $HOME ".qwen\skills")                    # Qwen Code
)

function New-Junction([string]$link, [string]$target) {
    cmd /c mklink /J "$link" "$target" | Out-Null
    if ((Get-Item -LiteralPath $link -Force).LinkType -ne 'Junction') {
        throw "Fallo al crear junction: $link"
    }
}

$added = 0; $skipped = 0
foreach ($root in $targets) {
    if (-not (Test-Path $root)) {
        if ($Uninstall) { continue }
        New-Item -ItemType Directory -Path $root -Force | Out-Null
    }
    foreach ($skill in (Get-ChildItem $repoSkills -Directory)) {
        $link = Join-Path $root $skill.Name
        if ($Uninstall) {
            if (Test-Path $link) {
                $i = Get-Item -LiteralPath $link -Force
                if ($i.LinkType -eq 'Junction') { cmd /c rmdir "$link" | Out-Null; $added++ }
            }
            continue
        }
        if (Test-Path $link) { $skipped++; continue }
        New-Junction $link $skill.FullName
        $added++
    }
}

if ($Uninstall) { Write-Host "Desinstaladas $added junctions." }
else { Write-Host "Instaladas $added junctions en $($targets.Count) roots ($skipped ya existían)." }
