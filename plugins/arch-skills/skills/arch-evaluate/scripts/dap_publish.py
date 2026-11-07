#!/usr/bin/env python3
"""Publish an immutable DAP evaluation report and generated summary."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

from dap.publishing import publish_report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        print(publish_report(args.project, args.output))
        return 0
    except (ValueError, OSError, RuntimeError) as exc:
        print(f"publication refused: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
