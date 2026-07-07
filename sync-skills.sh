#!/bin/bash
# Sync skills from workspace to Codex
# Run this after making changes to skills

SOURCE="$(cd "$(dirname "$0")" && pwd)/skills"
DESTINATION="${HOME}/.codex/skills"

echo "Syncing skills to ${DESTINATION}..."

mkdir -p "${DESTINATION}"
find "${SOURCE}" -mindepth 1 -maxdepth 1 ! -name 'copilot-instructions.md' -print0 | \
  while IFS= read -r -d '' item; do
    cp -r "${item}" "${DESTINATION}/"
  done

echo "Done! Installed skills:"
ls -d "${DESTINATION}"/arch-* 2>/dev/null | xargs -I {} basename {} | sed 's/^/  - /'
