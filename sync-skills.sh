#!/bin/bash
# Sync skills from workspace to Codex install location
# Usage: ./sync-skills.sh

set -e

SOURCE="$(cd "$(dirname "$0")" && pwd)/skills"
DESTINATION="${HOME}/.codex/skills"

echo "Syncing skills to ${DESTINATION}..."

mkdir -p "${DESTINATION}"

for skill in arch-doc arch-review arch-fitness arch-decision; do
    if [ -d "${SOURCE}/${skill}" ]; then
        cp -r "${SOURCE}/${skill}" "${DESTINATION}/${skill}"
        echo "  Synced: ${skill}"
    else
        echo "  Warning: ${skill} not found in source"
    fi
done

echo ""
echo "Done! Installed skills:"
ls -d "${DESTINATION}"/arch-* 2>/dev/null | xargs -I {} basename {} | sed 's/^/  - /'
