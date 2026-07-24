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
