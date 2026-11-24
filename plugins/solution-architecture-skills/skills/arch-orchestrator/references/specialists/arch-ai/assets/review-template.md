# AI Architecture Review: [System Name]

## Executive Summary

[2-3 sentences: what the AI components do, overall health, top risks]

## Use Case Inventory

| Use Case | Pattern | Model(s) | Criticality | Fallback |
|----------|---------|----------|-------------|----------|
| | Direct / RAG / Tool Use / Agent | | High/Med/Low | |

## RAG & Context Assessment

- Corpus and freshness: [sources, refresh cadence]
- Retrieval: [vector / hybrid / rerank, top-k]
- Grounding: [citations, context-only instructions]
- Retrieval metrics: [recall@k, MRR if measured]

## Agent & Tooling Assessment

| Tool | Purpose | Permissions | Destructive? | Logged? |
|------|---------|-------------|--------------|---------|

- Step / spend limits: [values]
- Human approval gates: [where]

## Guardrails

| Layer | Control | Status |
|-------|---------|--------|
| Input | Injection screening, PII redaction | |
| Permissions | User-scoped tool access | |
| Output | Schema validation, filtering | |
| Execution | Sandboxing, rate limits, spend caps | |

## Evaluation

- Offline eval set: [size, coverage, last run]
- Online monitoring: [sampled scoring, feedback, fallback rate]
- Prompt versioning: [how prompts are tracked and gated]

## Cost & Latency

| Metric | Budget | Current | Status |
|--------|--------|---------|--------|
| Cost per request | | | |
| p95 latency | | | |
| Monthly spend | | | |

## Findings

| ID | Finding | Severity | Effort | Recommendation |
|----|---------|----------|--------|----------------|

## Remediation Roadmap

1. **Immediate**: [critical gaps — e.g., missing injection controls]
2. **Short-term**: [eval coverage, fallbacks]
3. **Medium-term**: [cost optimization, model tiering]

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

Record model/prompt/corpus/evaluation-set revisions, permitted tool actions, risk-specific thresholds, human gates, fallback and spend limits.

### Verification plans and results

| VER ID | Protected IDs | Method and environment | Acceptance threshold | Owner | Planned/executed status | Actual evidence locator |
| --- | --- | --- | --- | --- | --- | --- |

Leave execution evidence empty for planned verification. A recommendation,
checkbox or generated test is not proof of implementation or human approval.
