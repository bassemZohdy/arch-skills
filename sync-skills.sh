#!/bin/bash
# Sync skills from workspace to Codex and Pi
# Run this after making changes to skills

SOURCE="$(cd "$(dirname "$0")" && pwd)/skills"

# --- Codex ---
CODEX_DEST="${HOME}/.codex/skills"
echo "Syncing skills to ${CODEX_DEST}..."
mkdir -p "${CODEX_DEST}"
find "${SOURCE}" -mindepth 1 -maxdepth 1 ! -name 'copilot-instructions.md' -print0 | \
  while IFS= read -r -d '' item; do
    cp -r "${item}" "${CODEX_DEST}/"
  done

# --- Pi ---
PI_DEST="${HOME}/.pi/agent/skills"
echo "Syncing skills to ${PI_DEST}..."
mkdir -p "${PI_DEST}"
find "${SOURCE}" -mindepth 1 -maxdepth 1 ! -name 'copilot-instructions.md' -print0 | \
  while IFS= read -r -d '' item; do
    cp -r "${item}" "${PI_DEST}/"
  done

echo "Done! Installed skills:"
ls -d "${CODEX_DEST}"/arch-* 2>/dev/null | xargs -I {} basename {} | sed 's/^/  - /'
