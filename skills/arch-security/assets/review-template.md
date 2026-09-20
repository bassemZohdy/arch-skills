# Security Review Template

## Security Review: [System Name]

### Assets Protected
- [List assets]

### Threats Identified
| ID | Threat | STRIDE | Risk (DREAD) | Mitigation |
|----|--------|--------|--------------|------------|

### Versioned security verification

Use [OWASP Top 10:2025](https://top10.owasp.org/2025/) as risk-awareness guidance,
not a complete compliance standard. Pin the chosen ASVS/control baseline and
record criterion IDs, threats, controls, evidence and residual-risk disposition.
Do not reuse category numbers from another edition.

| Standard / edition | Criterion | Threat / target IDs | Planned control | Verification evidence | Human disposition |
| --- | --- | --- | --- | --- | --- |

### Recommendations
1. [Critical]
2. [High]
3. [Medium]

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

Record threat/control IDs and selected standard edition, trust boundaries, residual risk, verification evidence and human security disposition.

### Verification plans and results

| VER ID | Protected IDs | Method and environment | Acceptance threshold | Owner | Planned/executed status | Actual evidence locator |
| --- | --- | --- | --- | --- | --- | --- |

Leave execution evidence empty for planned verification. A recommendation,
checkbox or generated test is not proof of implementation or human approval.
