#!/usr/bin/env python3
"""Validate and score a DAP project without modifying its artifacts."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from dap.scoring import evaluate_project


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--config", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.output:
        parser.error("audit is read-only; use dap_publish.py to publish a versioned report")
    try:
        report = evaluate_project(args.project, args.config)
    except (KeyError, OSError, ValueError) as exc:
        print(f"DAP validation failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["gate"]["ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
