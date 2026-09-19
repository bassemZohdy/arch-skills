#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

def main() -> int:
    p=argparse.ArgumentParser(description="Render a DAP traceability graph as a Markdown RTM")
    p.add_argument("project", type=Path)
    p.add_argument("--output", type=Path)
    a=p.parse_args()
    requirements=json.loads((a.project/"requirements.json").read_text())
    links=json.loads((a.project/"traceability.json").read_text())
    rows=["# Requirements Traceability Matrix","","| Requirement | Priority | Design elements | Decisions | Verification |","| --- | --- | --- | --- | --- |"]
    for r in requirements:
        rid=r["id"]
        d=sorted({l["to"] for l in links if l["from"]==rid and l["type"]=="requirement_to_design"})
        ads=sorted({l["to"] for l in links if l["from"]==rid and l["type"]=="requirement_to_decision"})
        v=sorted({l["to"] for l in links if l["from"]==rid and l["type"]=="requirement_to_verification"})
        rows.append(f"| {rid} | {r.get('priority','')} | {', '.join(d) or 'UNMAPPED'} | {', '.join(ads) or '—'} | {', '.join(v) or 'PLANNED'} |")
    out=a.output or a.project/"traceability.md"
    out.write_text("\n".join(rows)+"\n",encoding="utf-8")
    print(out)
    return 0
if __name__=="__main__": raise SystemExit(main())

