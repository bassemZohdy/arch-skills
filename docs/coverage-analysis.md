# Test Coverage Analysis

The inventory below is a historical coverage baseline, not a current pass result. Use the repository test commands and DAP implementation status for current verification evidence.

## Coverage Summary

| Metric | Count |
|--------|-------|
| Skills | 33 |
| Structural Tests | 224 |
| Behavioral scenarios (historical) | 185 |
| Total tests (historical) | 409 |

## Skills Coverage

### Process (1 skill)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-evaluate | 1 | 1 | 7 | 0 |


### Orchestration (1 skill)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-orchestrator | 3 | 3 | 7 | 5 |

### Core Architecture (5 skills)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-doc | 8 | 11 | 7 | 12 |
| arch-review | 6 | 1 | 7 | 8 |
| arch-fitness | 3 | 1 | 7 | 10 |
| arch-decision | 2 | 1 | 7 | 9 |
| arch-governance | 3 | 1 | 7 | 5 |

### Design Fundamentals (2 skills)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-principles | 3 | 1 | 7 | 5 |
| arch-antipatterns | 3 | 1 | 7 | 5 |

### Technical Architecture (4 skills)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-security | 4 | 1 | 7 | 5 |
| arch-perf | 3 | 1 | 7 | 5 |
| arch-resilience | 3 | 1 | 7 | 5 |
| arch-test | 3 | 1 | 7 | 5 |

### System Architecture (10 skills)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-api | 4 | 1 | 7 | 5 |
| arch-cloud | 3 | 1 | 7 | 5 |
| arch-event | 4 | 1 | 7 | 5 |
| arch-ddd | 4 | 1 | 7 | 5 |
| arch-data | 3 | 1 | 7 | 5 |
| arch-metrics | 3 | 1 | 7 | 5 |
| arch-integration | 2 | 1 | 7 | 5 |
| arch-microservices | 2 | 1 | 7 | 5 |
| arch-patterns | 2 | 1 | 7 | 5 |
| arch-refactoring | 2 | 1 | 7 | 5 |

### Frontend (1 skill)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-frontend | 3 | 1 | 7 | 5 |

### Operations (4 skills)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-observability | 3 | 1 | 7 | 6 |
| arch-migration | 3 | 1 | 7 | 5 |
| arch-devops | 4 | 1 | 7 | 10 |
| arch-cost | 2 | 1 | 7 | 5 |

### Feature Management (1 skill)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-features | 2 | 1 | 7 | 5 |

### AI (1 skill)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-ai | 2 | 1 | 7 | 5 |

### NFR (3 skills)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-usability | 2 | 1 | 7 | 5 |
| arch-accessibility | 2 | 1 | 7 | 5 |
| arch-compliance | 3 | 1 | 7 | 5 |

The evaluator is covered by the deterministic DAP checks; it is not represented as a model scenario because it operates on frozen artifacts and repository scripts.

## NFR Coverage Matrix

| NFR | Primary Skill | Supporting Skills | Status |
|-----|---------------|-------------------|--------|
| Performance | arch-perf | arch-cloud, arch-resilience | ✅ 100% |
| Scalability | arch-perf | arch-cloud | ✅ 100% |
| Availability | arch-resilience | arch-observability | ✅ 100% |
| Reliability | arch-resilience | arch-test | ✅ 100% |
| Security | arch-security | arch-compliance | ✅ 100% |
| Maintainability | arch-metrics | arch-doc | ✅ 100% |
| Testability | arch-test | arch-fitness | ✅ 100% |
| Observability | arch-observability | arch-metrics | ✅ 100% |
| Deployability | arch-devops | arch-cloud | ✅ 100% |
| Usability | arch-usability | arch-accessibility | ✅ 100% |
| Accessibility | arch-accessibility | arch-usability | ✅ 100% |
| Compliance | arch-compliance | arch-security | ✅ 100% |
| Data Integrity | arch-data | arch-metrics | ✅ 100% |
| Auditability | arch-compliance | arch-observability | ✅ 100% |
| Recoverability | arch-resilience | arch-migration | ✅ 100% |
| Modifiability | arch-metrics | arch-doc | ✅ 100% |

## Skill Relationships

```
┌─────────────────────────────────────────────────────────────────┐
│                        arch-review                              │
│                    (Orchestration Layer)                        │
└─────────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│  arch-doc     │    │  arch-fitness │    │  arch-metrics │
│  (Document)   │    │  (Validate)   │    │  (Measure)    │
└───────────────┘    └───────────────┘    └───────────────┘
        │                     │                     │
        ▼                     ▼                     ▼
┌───────────────────────────────────────────────────────────────┐
│                    Specialized Skills                         │
├───────────┬───────────┬───────────┬───────────┬───────────────┤
│ Security  │ Perf      │ Resilience│ Test      │ Data          │
│ API       │ Cloud     │ Event     │ DDD       │ Migration     │
│ Observability │ Usability │ Accessibility │ Compliance │ AI │
│ Integration │ Microservices │ DevOps │ Cost │ Governance     │
│ Patterns  │ Refactoring │ Frontend │ Features │ Fitness       │
│ Principles │ Antipatterns │      │           │               │
└───────────┴───────────┴───────────┴───────────┴───────────────┘
```

## External Resources

Every skill includes `references/awesome-architecture.md` with curated deep links into
[awesome-architecture.com](https://awesome-architecture.com/). See
[awesome-architecture-mapping.md](awesome-architecture-mapping.md) for the full taxonomy-to-skill
analysis.

In addition, every skill cites its specialized reference files (`*-deep-dive.md`,
`*-patterns.md`, topic references) from `## Further Reading`, so deeper guidance is
loadable on demand. Diagrams use fenced Mermaid blocks (per the
Mermaid > PlantUML > Draw.io priority in `AGENTS.md`).
