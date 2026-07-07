# Test Coverage Analysis

## Coverage Summary

| Metric | Count |
|--------|-------|
| Skills | 29 |
| Structural Tests | 203 |
| Skillprobe Scenarios | 170 |
| Total Tests | 373 |

## Skills Coverage

### Core Architecture (5 skills)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-doc | 7 | 11 | 7 | 12 |
| arch-review | 5 | 1 | 7 | 8 |
| arch-fitness | 2 | 1 | 7 | 10 |
| arch-decision | 1 | 1 | 7 | 9 |
| arch-governance | 1 | 1 | 7 | 5 |

### Technical Architecture (4 skills)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-security | 2 | 1 | 7 | 5 |
| arch-perf | 1 | 1 | 7 | 5 |
| arch-resilience | 1 | 1 | 7 | 5 |
| arch-test | 1 | 1 | 7 | 5 |

### System Architecture (10 skills)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-api | 2 | 1 | 7 | 5 |
| arch-cloud | 1 | 1 | 7 | 5 |
| arch-event | 2 | 1 | 7 | 5 |
| arch-ddd | 2 | 1 | 7 | 5 |
| arch-data | 1 | 1 | 7 | 5 |
| arch-metrics | 1 | 1 | 7 | 5 |
| arch-integration | 1 | 1 | 7 | 5 |
| arch-microservices | 1 | 1 | 7 | 5 |
| arch-patterns | 1 | 1 | 7 | 5 |
| arch-refactoring | 1 | 1 | 7 | 5 |

### Frontend (1 skill)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-frontend | 1 | 1 | 7 | 5 |

### Operations (4 skills)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-observability | 1 | 1 | 7 | 6 |
| arch-migration | 1 | 1 | 7 | 5 |
| arch-devops | 3 | 1 | 7 | 10 |
| arch-cost | 1 | 1 | 7 | 5 |

### Feature Management (1 skill)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-features | 1 | 1 | 7 | 5 |

### AI (1 skill)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-ai | 1 | 1 | 7 | 5 |

### NFR (3 skills)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-usability | 1 | 1 | 7 | 5 |
| arch-accessibility | 1 | 1 | 7 | 5 |
| arch-compliance | 1 | 1 | 7 | 5 |

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
└───────────┴───────────┴───────────┴───────────┴───────────────┘
```
