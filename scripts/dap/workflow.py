"""Small shared transition helpers, not a second orchestration engine."""
from .contracts import ContractError

AUTHORING_MODES = {"interview", "create", "update"}


def route(mode, assessment="both"):
    if mode in AUTHORING_MODES:
        return {"entry": "arch-orchestrator", "mode": mode, "read_only": False,
                "stop_after": "requirements" if mode == "interview" else "candidate"}
    if mode == "evaluate" and assessment in {"process", "design", "both"}:
        return {"entries": (["arch-evaluate"] if assessment == "process" else
                            ["arch-review"] if assessment == "design" else ["arch-evaluate", "arch-review"]),
                "read_only": True}
    raise ContractError("select interview, create, update, or evaluate(process/design/both)")


def plan_change(changed_ids, links, change_kind):
    if change_kind not in {"requirements", "design", "approval", "editorial"}:
        raise ContractError("unknown change kind")
    if change_kind == "editorial":
        return {"stage": "documentation", "affected_ids": sorted(set(changed_ids)), "invalidate": ["evaluation"]}
    affected = set(changed_ids)
    # Conservative dependency closure; do not hide effects behind edge orientation.
    while True:
        following = affected | {end for link in links if link["from"] in affected or link["to"] in affected
                                for end in (link["from"], link["to"])}
        if following == affected:
            break
        affected = following
    return {"stage": {"requirements": "interview", "design": "design", "approval": "review"}[change_kind],
            "affected_ids": sorted(affected), "invalidate": ["affected_assessments", "affected_approvals", "evaluation"]}


def interview_status(rounds, minutes, limits, confirmed, unresolved):
    if unresolved or not confirmed:
        if rounds >= limits["max_interview_rounds"] or minutes >= limits["max_interview_minutes"]:
            return "blocked"
        return "draft"
    return "ready-for-review"
