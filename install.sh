#!/usr/bin/env bash
# Instala todas las skills en cada CLI de agentes del sistema (Linux/macOS) via symlinks.
# Uso:  ./install.sh            (instala)
#       ./install.sh --uninstall
set -euo pipefail

REPO_SKILLS="$(cd "$(dirname "$0")" && pwd)/skills"
[ -d "$REPO_SKILLS" ] || { echo "No se encuentra $REPO_SKILLS"; exit 1; }

TARGETS=(
  "$HOME/.agents/skills"
  "$HOME/.claude/skills"
  "$HOME/.config/opencode/skills"
  "$HOME/.codex/skills"
  "$HOME/.zcode/skills"
  "$HOME/.gemini/skills"
  "$HOME/.qwen/skills"
)

UNINSTALL=0
[ "${1:-}" = "--uninstall" ] && UNINSTALL=1

added=0; skipped=0
for root in "${TARGETS[@]}"; do
  if [ "$UNINSTALL" = "1" ]; then
    [ -d "$root" ] || continue
    for link in "$root"/*; do
      [ -L "$link" ] && { rm -f "$link"; added=$((added+1)); }
    done
    continue
  fi
  mkdir -p "$root"
  for skill in "$REPO_SKILLS"/*/; do
    name="$(basename "$skill")"
    link="$root/$name"
    if [ -e "$link" ] || [ -L "$link" ]; then skipped=$((skipped+1)); continue; fi
    ln -s "$skill" "$link"; added=$((added+1))
  done
done

if [ "$UNINSTALL" = "1" ]; then echo "Desinstalados $added symlinks."
else echo "Instalados $added symlinks en ${#TARGETS[@]} roots ($skipped ya existian)."; fi
