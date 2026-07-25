# Shared Architecture Context

Maintained by the orchestrator; the relevant subset is passed to every specialist
invocation and updated after each completion. Delete rows that are genuinely
not applicable; never delete open questions.

## Problem & Business

| Field | Value |
|-------|-------|
| Problem statement | |
| Business goals | |
| Stakeholders | |
| Expected deliverables | |

## Requirements

| Field | Value |
|-------|-------|
| Functional requirements | |
| Quality attributes (prioritized) | |
| Integration requirements | |
| Expected scale | |
| Availability / recovery (RTO/RPO) | |

## Constraints & Environment

| Field | Value |
|-------|-------|
| Constraints | |
| Assumptions | |
| Existing systems | |
| Preferred technologies (preferences, not mandates) | |
| Prohibited technologies | |
| Deployment environment | |
| Security & compliance requirements | |
| Data residency requirements | |
| Budget / delivery constraints | |

## Classification

| Dimension | Value |
|-----------|-------|
| Initiative | greenfield / modernization / migration / integration / review |
| Style tendency | |
| System type | |
| Environment | |
| Criticality | |
| Processing modes | |

## Working State

| Field | Value |
|-------|-------|
| Selected architectural style | |
| Decisions already made (id → decision → source skill) | |
| Open questions | |
| Identified risks | |
| Selected skills | |
| Skill execution status (skill → pending/running/done/failed) | |

## Update Rules

- Merge only confirmed findings and ratified decisions after each skill completes.
- A specialist may propose a change to an approved decision; only the orchestrator
  ratifies it, and the change is recorded with its rationale.
- Every decision entry links back to the requirement(s) or quality attribute(s)
  that motivated it.
