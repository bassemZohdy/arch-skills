#!/usr/bin/env python3
from __future__ import annotations
import argparse, sys
from pathlib import Path
from datetime import datetime, timezone
sys.path.insert(0,str(Path(__file__).resolve().parent))
from dap.scoring import evaluate_project, report_is_stale
from dap.persistence import atomic_write_json
def main() -> int:
    p=argparse.ArgumentParser(description="Publish a DAP evaluation report")
    p.add_argument("project",type=Path)
    p.add_argument("--output",type=Path)
    a=p.parse_args()
    report=evaluate_project(a.project)
    report["publication"]={"published_at":datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z"),"mode":"generated-report"}
    out=a.output or a.project/"evaluations/latest.json"
    if out.exists():
        import json
        report["previous_report_stale"] = report_is_stale(a.project, json.loads(out.read_text(encoding="utf-8")))
    atomic_write_json(out,report)
    print(out)
    return 0
if __name__=="__main__": raise SystemExit(main())
