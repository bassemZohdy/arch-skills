# Anti-Pattern Review Template

Copy this into review notes when auditing a system or module for anti-patterns.

## Scope

- System/module:
- Date:
- Reviewer:
- Trigger (review / incident / pre-feature):

## Structural Scan

| Anti-Pattern | Present? | Evidence | Severity (H/M/L) |
|--------------|----------|----------|-------------------|
| Big Ball of Mud | | | |
| God Object | | | |
| Distributed Monolith | | | |
| Leaky Abstraction | | | |
| Static Cling | | | |
| Anemic / Partial Objects | | | |
| Golden Hammer | | | |
| Cargo-Cult Architecture | | | |

## Code Smell Hot Spots

| Location | Smell | Root Smell | Suggested Refactoring |
|----------|-------|------------|------------------------|
| | | | |

## Impact Ranking

Rank by change frequency × coupling radius (not by ugliness):

1. [Anti-pattern] — [why it costs the most]
2.
3.

## Decisions

| Item | Refactor / Contain / Accept | Rationale | ADR needed? |
|------|-----------------------------|-----------|-------------|
| | | | |

## Remediation Plan

| Step | Change | Tests Required | Owner | Status |
|------|--------|----------------|-------|--------|
| 1 | | | | |

## Prevention

- [ ] Architecture/fitness test added for the violated boundary
- [ ] Smell added to review checklist for this codebase
- [ ] Debt register entry with revisit date

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

Record observed location and cost of change, refactor/contain/accept disposition, accepted-debt authority, revisit date and prevention checks.

### Verification plans and results

| VER ID | Protected IDs | Method and environment | Acceptance threshold | Owner | Planned/executed status | Actual evidence locator |
| --- | --- | --- | --- | --- | --- | --- |

Leave execution evidence empty for planned verification. A recommendation,
checkbox or generated test is not proof of implementation or human approval.
