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
