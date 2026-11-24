#!/usr/bin/env python3
"""Create or compare a DAP input manifest without modifying source artifacts."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from dap.snapshot import Snapshot, report_is_stale


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--compare", type=Path)
    args = parser.parse_args()
    try:
        current = Snapshot(args.project).manifest
        if args.compare:
            old = json.loads(args.compare.read_text(encoding="utf-8"))
            if not isinstance(old, dict):
                raise ValueError("comparison must contain a manifest or report object")
            if "input_manifest" in old:
                current["stale"] = report_is_stale(args.project, old)
            else:
                previous = Snapshot(args.project, old.get("external_config")).manifest
                current["stale"] = old.get("sha256") != previous["sha256"]
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        print(f"manifest refused: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(current, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
