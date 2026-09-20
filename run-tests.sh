#!/usr/bin/env bash
# Run the offline release checks from any working directory.
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"

python3 tests/test_skills.py
python3 -m unittest discover -s tests -p 'test_*.py'
python3 tests/test_activation.py

echo 'All offline checks passed.'
