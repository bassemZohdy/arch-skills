# Test Coverage Analysis

## Coverage Summary

| Metric | Count |
|--------|-------|
| Skills | 25 |
| Structural Tests | 175 |
| Skillprobe Scenarios | 152 |
| Total Tests | 327 |

## Skills Coverage

### Core Architecture (5 skills)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-doc | 6 | 11 | 7 | 12 |
| arch-review | 4 | 1 | 7 | 9 |
| arch-fitness | 1 | 1 | 7 | 9 |
| arch-decision | 1 | 1 | 7 | 9 |
| arch-governance | 1 | 1 | 7 | 5 |

### Technical Architecture (4 skills)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-security | 2 | 1 | 7 | 5 |
| arch-perf | 1 | 1 | 7 | 5 |
| arch-resilience | 1 | 1 | 7 | 5 |
| arch-test | 1 | 1 | 7 | 5 |

### System Architecture (8 skills)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-api | 1 | 1 | 7 | 5 |
| arch-cloud | 1 | 1 | 7 | 5 |
| arch-event | 2 | 1 | 7 | 5 |
| arch-ddd | 2 | 1 | 7 | 5 |
| arch-data | 1 | 1 | 7 | 5 |
| arch-metrics | 1 | 1 | 7 | 5 |
| arch-integration | 1 | 1 | 7 | 5 |
| arch-microservices | 1 | 1 | 7 | 5 |

### Operations (5 skills)

| Skill | References | Assets | Tests | Scenarios |
|-------|------------|--------|-------|-----------|
| arch-observability | 1 | 1 | 7 | 5 |
| arch-migration | 1 | 1 | 7 | 5 |
| arch-deployment | 1 | 1 | 7 | 5 |
| arch-devops | 1 | 1 | 7 | 5 |
| arch-cost | 1 | 1 | 7 | 5 |

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
| Deployability | arch-deployment | arch-cloud | ✅ 100% |
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
│ Observability │ Deployment │ Usability │ Accessibility │ Compliance │
│ Integration │ Microservices │ DevOps │ Cost │ Governance     │
└───────────┴───────────┴───────────┴───────────┴───────────────┘
```
