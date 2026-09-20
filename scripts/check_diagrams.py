#!/usr/bin/env python3
"""Inventory Mermaid sources and optionally render them with a trusted command."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
MERMAID_FENCE = "```mermaid"
KNOWN_STARTS = (
    "graph ", "graph\n", "flowchart ", "flowchart\n", "sequenceDiagram",
    "stateDiagram", "classDiagram", "erDiagram", "journey", "gantt", "pie",
    "mindmap", "timeline", "quadrantChart", "gitGraph", "C4Context",
    "C4Container", "C4Component", "C4Dynamic", "C4Deployment",
)


def fenced_sources(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    inside = False
    start = None
    body = []
    for number, line in enumerate(lines, 1):
        if not inside and line.strip().lower() == MERMAID_FENCE:
            inside, start, body = True, number, []
            continue
        if inside and line.strip().startswith("```"):
            yield start, "\n".join(body).strip() + "\n"
            inside = False
            continue
        if inside:
            body.append(line)
    if inside:
        raise ValueError(f"unterminated Mermaid fence: {path}:{start}")


def discover_sources(root: Path):
    root = root.resolve()
    sources = []
    for path in sorted(root.rglob("*.mmd")):
        if any(part in {".git", ".cache", "__pycache__"} for part in path.parts):
            continue
        sources.append({"path": path, "line": 1, "kind": "file",
                        "source": path.read_text(encoding="utf-8")})
    for path in sorted(root.rglob("*.md")):
        if any(part in {".git", ".cache", "__pycache__"} for part in path.parts):
            continue
        for line, source in fenced_sources(path):
            sources.append({"path": path, "line": line, "kind": "fence", "source": source})
    return sources


def validate_source(source: str, label: str):
    if not source.strip():
        raise ValueError(f"empty Mermaid source: {label}")
    first = source.lstrip().splitlines()[0].strip()
    if not first.startswith(KNOWN_STARTS):
        raise ValueError(f"unknown Mermaid diagram header {first!r}: {label}")
    if "\x00" in source:
        raise ValueError(f"NUL byte in Mermaid source: {label}")


def render_source(command, source: str, output: Path, label: str, timeout: int):
    with tempfile.TemporaryDirectory(prefix="arch-diagram-") as directory:
        input_path = Path(directory) / "diagram.mmd"
        input_path.write_text(source, encoding="utf-8")
        result = subprocess.run(command + ["-i", str(input_path), "-o", str(output)],
                                capture_output=True, text=True, timeout=timeout, check=False)
        if result.returncode:
            detail = (result.stderr or result.stdout).strip().splitlines()[-1:]
            raise RuntimeError(f"renderer failed for {label}: {detail[0] if detail else result.returncode}")
        if not output.is_file() or output.stat().st_size == 0:
            raise RuntimeError(f"renderer produced no output for {label}")


def check(root: Path, output: Path | None = None, renderer=None, timeout=120):
    root = root.resolve()
    sources = discover_sources(root)
    if not sources:
        raise ValueError("no Mermaid sources found")
    output = output.resolve() if output else None
    if output:
        output.mkdir(parents=True, exist_ok=True)
    report = {"schema_version": "1.0", "renderer": renderer,
              "rendered": 0, "sources": [], "errors": []}
    for index, item in enumerate(sources, 1):
        label = f"{item['path'].relative_to(root)}:{item['line']}"
        record = {"path": item["path"].relative_to(root).as_posix(),
                  "line": item["line"], "kind": item["kind"],
                  "sha256": hashlib.sha256(item["source"].encode()).hexdigest()}
        try:
            validate_source(item["source"], label)
            if renderer:
                target = output / f"diagram-{index:04d}.svg"
                render_source(renderer, item["source"], target, label, timeout)
                record["rendered"] = str(target.relative_to(output))
                report["rendered"] += 1
        except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as exc:
            report["errors"].append(str(exc))
        report["sources"].append(record)
    if output:
        (output / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--renderer-command", help="JSON argv prefix; it receives -i INPUT -o OUTPUT")
    parser.add_argument("--timeout", type=int, default=120)
    args = parser.parse_args(argv)
    try:
        renderer = json.loads(args.renderer_command) if args.renderer_command else None
        if renderer is not None and (not isinstance(renderer, list) or not renderer or
                                     any(not isinstance(x, str) or not x for x in renderer)):
            raise ValueError("renderer command must be a nonempty JSON argv list")
        report = check(args.root.resolve(), args.output, renderer, args.timeout)
        print(json.dumps({"sources": len(report["sources"]), "rendered": report["rendered"],
                          "errors": len(report["errors"]), "renderer": renderer}))
        return 1 if report["errors"] else 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"diagram check failed: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
