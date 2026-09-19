#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from dap.scoring import _manifest
def main() -> int:
    p=argparse.ArgumentParser(description="Create or compare a DAP input manifest")
    p.add_argument("project", type=Path)
    p.add_argument("--compare", type=Path)
    a=p.parse_args()
    current=_manifest(a.project, {"process/assessment.json"})
    if a.compare:
        old=json.loads(a.compare.read_text(encoding="utf-8"))
        old_hash = old.get("sha256") or old.get("input_manifest", {}).get("sha256")
        current["stale"]=old_hash != current["sha256"]
    print(json.dumps(current,indent=2))
    return 0
if __name__=="__main__": raise SystemExit(main())
