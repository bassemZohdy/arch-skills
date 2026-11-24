#!/usr/bin/env python3
"""Atomically save or inspect a DAP checkpoint."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from dap.persistence import ConcurrentRevisionError, load_checkpoint, save_checkpoint


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--state", type=Path)
    parser.add_argument("--expected-revision", type=int)
    parser.add_argument("--show", action="store_true")
    parser.add_argument("--project", type=Path, help="Verify the referenced artifact subject when resuming")
    args = parser.parse_args()
    try:
        if args.show:
            result = load_checkpoint(args.path, args.project)
        else:
            if not args.state:
                parser.error("--state is required unless --show is used")
            state = json.loads(args.state.read_text(encoding="utf-8"))
            result = save_checkpoint(args.path, state, args.expected_revision)
    except (ConcurrentRevisionError, OSError, ValueError) as exc:
        print(f"checkpoint failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
