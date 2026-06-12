#!/bin/bash
# Run validation tests for all skills
# Usage: ./run-tests.sh [--dar-only]

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "============================================"
echo "Architecture Skills Test Suite"
echo "============================================"
echo ""

if [ "$1" = "--dar-only" ]; then
    # Only run DAR validation
    echo "Running DAR math validation..."
    if [ -f "${SCRIPT_DIR}/tests/test-dar.md" ]; then
        python3 "${SCRIPT_DIR}/skills/arch-decision/scripts/validate_math.py" "${SCRIPT_DIR}/tests/test-dar.md"
    else
        echo "No test-dar.md found, skipping."
    fi
else
    # Run all tests
    echo "Running structural validation tests..."
    python3 "${SCRIPT_DIR}/tests/test_skills.py"

    echo ""
    echo "Running DAR math validation..."
    if [ -f "${SCRIPT_DIR}/tests/test-dar.md" ]; then
        python3 "${SCRIPT_DIR}/skills/arch-decision/scripts/validate_math.py" "${SCRIPT_DIR}/tests/test-dar.md"
    else
        echo "No test-dar.md found, skipping."
    fi
fi

echo ""
echo "============================================"
echo "All tests completed!"
echo "============================================"
