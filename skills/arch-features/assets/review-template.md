# Feature Review Template

## Feature Management Review: [System]

### Feature Flags
| Flag | Type | Status | Owner |
|------|------|--------|-------|

### Rollout Status
| Feature | Strategy | Progress | Rollback Plan |
|---------|----------|----------|---------------|

### Experiments
| Experiment | Variants | Sample Size | Status |
|------------|----------|-------------|--------|

### Recommendations
1. [Improvement]

## Scope, evidence and DAP handoff

For standalone use, omit inapplicable process fields; do not invent a DAP run.

| Field | Recorded value |
| --- | --- |
| Scope, run, stage and baseline revision/hash | |
| REQ / CON / DES / ADR IDs and source revisions | |
| Findings: ID, target, observed/proposed/unknown, evidence locator, rationale, uncertainty | |
| Alternatives and consequences | |
| Required human review, authority and disposition evidence | |
| Affected dependencies, supersessions and stale approvals | |
| Open Q / ASM / EXC IDs, owner and next action | |
| Contribution status: complete for scope / provisional / blocked | |

### Domain evidence

Record flag/experiment IDs, exposure and privacy policy, owner/expiry, guardrail thresholds, approval, kill-switch checks and removal criteria.

### Verification plans and results

| VER ID | Protected IDs | Method and environment | Acceptance threshold | Owner | Planned/executed status | Actual evidence locator |
| --- | --- | --- | --- | --- | --- | --- |

Leave execution evidence empty for planned verification. A recommendation,
checkbox or generated test is not proof of implementation or human approval.
