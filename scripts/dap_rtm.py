#!/usr/bin/env python3
"""Render the same validated trace graph used by the evaluator."""
from __future__ import annotations
import argparse
from pathlib import Path
from dap.contracts import FILES, validate_records
from dap.graph import trace_coverage
from dap.snapshot import Snapshot


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        snapshot = Snapshot(args.project)
        records = {k: snapshot.json(v) for k, v in FILES.items()}
        validate_records(records)
        _, _, rows = trace_coverage(records, snapshot.json("process/config.json")["scope"], snapshot.evidence)
        output = args.output or args.project / "evaluations/traceability.md"
        root = args.project.resolve()
        if output.resolve().parent != root / "evaluations" or output.suffix != ".md":
            raise ValueError("generated RTM must be a Markdown file directly under evaluations/")
        if output.is_symlink() or (output.exists() and output.name != 'traceability.md'):
            raise ValueError('custom RTM output must be fresh; archived evaluation summaries are immutable')
        output.parent.mkdir(exist_ok=True)
        text = ["# Requirements Traceability Matrix", "",
                "| Requirement | Source confirmed | Design | ADR | Verification plan | Complete |",
                "| --- | --- | --- | --- | --- | --- |"]
        for row in rows:
            text.append("| " + " | ".join([row["id"], str(row["source_confirmed"]),
                ", ".join(row["designs"]) or "MISSING", ", ".join(row["decisions"]) or "NONE REQUIRED",
                ", ".join(row["verification"]) or "MISSING", str(row["complete"])]) + " |")
        if not snapshot.unchanged():
            raise ValueError("baseline changed while rendering")
        output.write_text("\n".join(text) + "\n", encoding="utf-8")
        print(output)
        return 0
    except (ValueError, OSError, KeyError) as exc:
        print(f"RTM refused: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
