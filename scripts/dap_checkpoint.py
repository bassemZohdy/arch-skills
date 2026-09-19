#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from dap.persistence import save_checkpoint, load_checkpoint, ConcurrentRevisionError
def main() -> int:
    p=argparse.ArgumentParser(description="Atomically save or inspect a DAP checkpoint")
    p.add_argument("path", type=Path)
    p.add_argument("--state", type=Path)
    p.add_argument("--expected-revision", type=int)
    p.add_argument("--show", action="store_true")
    a=p.parse_args()
    try:
        if a.show:
            print(json.dumps(load_checkpoint(a.path), indent=2)); return 0
        if not a.state: p.error("--state is required unless --show is used")
        state=json.loads(a.state.read_text(encoding="utf-8"))
        print(json.dumps(save_checkpoint(a.path,state,a.expected_revision),indent=2)); return 0
    except (ConcurrentRevisionError, ValueError, json.JSONDecodeError) as exc:
        print(f"checkpoint failed: {exc}", file=sys.stderr); return 2
if __name__=="__main__": raise SystemExit(main())

