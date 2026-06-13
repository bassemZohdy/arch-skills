#!/bin/bash
# Run validation tests for all skills

echo "============================================"
echo "Architecture Skills Test Suite"
echo "============================================"
echo ""

python3 "$(dirname "$0")/tests/test_skills.py"

echo ""
echo "============================================"
echo "All tests completed!"
echo "============================================"
