"""Explicit report-only publication; never overwrite assessed source records."""
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from .contracts import ContractError
from .persistence import atomic_write_json, exclusive_lock
from .scoring import evaluate_project
from .snapshot import report_is_stale


def publish_report(root, output=None):
    root = Path(root).resolve()
    directory = root / "evaluations"
    directory.mkdir(exist_ok=True)
    if directory.resolve().parent != root:
        raise ContractError("evaluation destination escapes project")
    if output is not None and Path(output).resolve() != directory / "latest.json":
        raise ContractError("publication output must be evaluations/latest.json; assessed files cannot be overwritten")
    with exclusive_lock(directory / ".publication.lock"):
        report = evaluate_project(root)
        if not report.get("input_manifest", {}).get("sha256") or report_is_stale(root, report):
            raise ContractError("no valid frozen snapshot to publish")
        run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S") + "-" + uuid4().hex
        report["publication"] = {"id": run_id, "input_revision": report["baseline_revision"],
                                 "published_at": datetime.now(timezone.utc).isoformat(),
                                 "assessment_status": "ready" if report["gate"]["ready"] else "blocked"}
        immutable = directory / f"{run_id}.json"
        atomic_write_json(immutable, report)
        # No source appendix mutation: an adjacent generated summary can be linked by arch-doc.
        summary = directory / f"{run_id}.md"
        summary.write_text(f"# DAP evaluation {run_id}\n\nBaseline: {report['baseline_revision']}\n\n"
                           f"Ready: {report['gate']['ready']}\n\nScore: {report['overall_score']}\n\n"
                           f"Manifest: {report['input_manifest']['sha256']}\n\n"
                           f"[Machine-readable findings]({immutable.name})\n", encoding="utf-8")
        if report_is_stale(root, report):
            raise ContractError("inputs changed during publication; archived report is stale; latest was not promoted")
        atomic_write_json(directory / "latest.json", report)
        return immutable
