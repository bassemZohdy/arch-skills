# Architecture Skills - Task List

## Completed

### Phase 1: Initial Skills (4)
- [x] arch-doc — Architecture documentation (C4, arc42, TOGAF, ISO 42010)
- [x] arch-review — Review orchestration (ATAM, SAAM)
- [x] arch-fitness — Fitness functions (ArchUnit/ArchUnitTS)
- [x] arch-decision — DAR methodology

### Phase 2: Technical Skills (4)
- [x] arch-security — Security patterns (STRIDE, OWASP)
- [x] arch-perf — Performance engineering (SLA/SLO)
- [x] arch-resilience — Resilience patterns (circuit breaker, retry)
- [x] arch-test — Test architecture (pyramids, contracts)

### Phase 3: System Skills (10)
- [x] arch-api — API design (REST, GraphQL, gRPC, OpenAPI)
- [x] arch-cloud — Cloud patterns (Well-Architected, FinOps)
- [x] arch-event — Event-driven (CQRS, Event Sourcing)
- [x] arch-ddd — Domain-Driven Design
- [x] arch-data — Data architecture
- [x] arch-metrics — Architecture metrics
- [x] arch-integration — Integration patterns (service mesh, ESB)
- [x] arch-microservices — Microservices architecture
- [x] arch-patterns — Architecture patterns (Clean, Hexagonal, Layered)
- [x] arch-refactoring — Code smells, refactoring patterns

### Phase 4: Frontend
- [x] arch-frontend — Micro frontends, UI patterns, SPA

### Phase 5: Operations (5)
- [x] arch-observability — Observability (logs, metrics, traces)
- [x] arch-migration — Migration planning
- [x] arch-deployment — Deployment strategies
- [x] arch-devops — DevOps (IaC, Kubernetes, GitOps)
- [x] arch-cost — Cost optimization (FinOps)

### Phase 6: Feature Management
- [x] arch-features — Feature flags, toggles, experimentation

### Phase 7: Automation
- [x] arch-automation — CI/CD, documentation, infrastructure automation

### Phase 8: NFR Skills (3)
- [x] arch-usability — Usability patterns (Nielsen's heuristics)
- [x] arch-accessibility — WCAG compliance (ARIA)
- [x] arch-compliance — Regulatory compliance (GDPR, HIPAA)

### Phase 9: Governance
- [x] arch-governance — Architecture governance

### Phase 10: Documentation & Testing
- [x] README.md — Complete project documentation
- [x] AGENTS.md — Agent instructions
- [x] docs/coverage-analysis.md — Test coverage matrix
- [x] docs/harness-compatibility.md — Supported harnesses
- [x] docs/skill-testing.md — Skill testing guide
- [x] tests/test_skills.py — 210 structural tests
- [x] tests/test-arch-*.yaml — 167 skillprobe scenarios

### Phase 11: Cross-Harness Support
- [x] scripts/detect_harness.py — Detect available harnesses
- [x] scripts/setup_unified.py — Unified skill management
- [x] 12 harnesses supported

## Project Status

| Metric | Value |
|--------|-------|
| Skills | 30 |
| Structural Tests | 210 |
| Skill Scenarios | 167 |
| Total Tests | 377 |
| References | 60+ |
| Assets | 40+ |
| NFR Coverage | 100% |
| Harnesses | 12 |

## File Structure

```
arch-skills/
├── README.md
├── AGENTS.md
├── TODO.md
├── sync-skills.ps1
├── sync-skills.sh
├── run-tests.ps1
├── run-tests.sh
├── scripts/
│   ├── detect_harness.py
│   ├── setup_unified.py
│   └── sync_all.py
├── docs/
│   ├── coverage-analysis.md
│   ├── harness-compatibility.md
│   ├── skill-testing.md
│   └── best-practices-master.md
├── skills/ (30 skills)
└── tests/
    ├── test_skills.py
    ├── test-arch-*.yaml
    └── test-dar.md
```
