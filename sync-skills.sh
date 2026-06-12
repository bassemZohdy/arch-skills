#!/bin/bash
# Sync skills from workspace to Codex install location
# Usage: ./sync-skills.sh

set -e

SOURCE="$(cd "$(dirname "$0")" && pwd)/skills"
DESTINATION="${HOME}/.codex/skills"

echo "Syncing skills to ${DESTINATION}..."

mkdir -p "${DESTINATION}"

# Core Architecture
for skill in arch-doc arch-review arch-fitness arch-decision arch-governance; do
    if [ -d "${SOURCE}/${skill}" ]; then
        cp -r "${SOURCE}/${skill}" "${DESTINATION}/${skill}"
        echo "  Synced: ${skill}"
    fi
done

# Technical Architecture
for skill in arch-security arch-perf arch-resilience arch-test; do
    if [ -d "${SOURCE}/${skill}" ]; then
        cp -r "${SOURCE}/${skill}" "${DESTINATION}/${skill}"
        echo "  Synced: ${skill}"
    fi
done

# System Architecture
for skill in arch-api arch-cloud arch-event arch-ddd arch-data arch-metrics arch-integration arch-microservices arch-patterns arch-refactoring; do
    if [ -d "${SOURCE}/${skill}" ]; then
        cp -r "${SOURCE}/${skill}" "${DESTINATION}/${skill}"
        echo "  Synced: ${skill}"
    fi
done

# Frontend
for skill in arch-frontend; do
    if [ -d "${SOURCE}/${skill}" ]; then
        cp -r "${SOURCE}/${skill}" "${DESTINATION}/${skill}"
        echo "  Synced: ${skill}"
    fi
done

# Operations
for skill in arch-observability arch-migration arch-deployment arch-devops arch-cost; do
    if [ -d "${SOURCE}/${skill}" ]; then
        cp -r "${SOURCE}/${skill}" "${DESTINATION}/${skill}"
        echo "  Synced: ${skill}"
    fi
done

# Feature Management
for skill in arch-features; do
    if [ -d "${SOURCE}/${skill}" ]; then
        cp -r "${SOURCE}/${skill}" "${DESTINATION}/${skill}"
        echo "  Synced: ${skill}"
    fi
done

# NFR
for skill in arch-usability arch-accessibility arch-compliance; do
    if [ -d "${SOURCE}/${skill}" ]; then
        cp -r "${SOURCE}/${skill}" "${DESTINATION}/${skill}"
        echo "  Synced: ${skill}"
    fi
done

echo ""
echo "Done! Installed skills:"
ls -d "${DESTINATION}"/arch-* 2>/dev/null | xargs -I {} basename {} | sed 's/^/  - /'
