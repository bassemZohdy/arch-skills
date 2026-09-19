#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
SCRIPT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_ROOT))
from dap.scoring import evaluate_project
from dap.contracts import ContractError
def main() -> int:
    parser = argparse.ArgumentParser(description="Validate and score a DAP project baseline")
    parser.add_argument("project", type=Path)
    parser.add_argument("--config", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        report = evaluate_project(args.project, args.config)
    except (ContractError, KeyError, FileNotFoundError, ValueError) as exc:
        print(f"DAP validation failed: {exc}", file=sys.stderr)
        return 2
    payload = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())

