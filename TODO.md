# Architecture Skills - Task List

## Completed

### Phase 1: Initial Skills (4)
- [x] arch-doc — Architecture documentation (C4, arc42, TOGAF, ISO 42010)
- [x] arch-review — Review orchestration
- [x] arch-fitness — Fitness functions (ArchUnit/ArchUnitTS)
- [x] arch-decision — DAR methodology

### Phase 2: Technical Skills (4)
- [x] arch-security — Security patterns (STRIDE, OWASP)
- [x] arch-perf — Performance engineering (SLA/SLO)
- [x] arch-resilience — Resilience patterns (circuit breaker, retry)
- [x] arch-test — Test architecture (pyramids, contracts)

### Phase 3: System Skills (8)
- [x] arch-api — API design (REST, GraphQL, gRPC)
- [x] arch-cloud — Cloud patterns (Well-Architected, FinOps)
- [x] arch-event — Event-driven (CQRS, Event Sourcing)
- [x] arch-ddd — Domain-Driven Design
- [x] arch-data — Data architecture
- [x] arch-metrics — Architecture metrics
- [x] arch-integration — Integration patterns (service mesh, ESB)
- [x] arch-microservices — Microservices architecture

### Phase 4: Operations Skills (5)
- [x] arch-observability — Observability (logs, metrics, traces)
- [x] arch-migration — Migration planning
- [x] arch-deployment — Deployment strategies
- [x] arch-devops — DevOps (IaC, Kubernetes, GitOps)
- [x] arch-cost — Cost optimization (FinOps)

### Phase 5: NFR Skills (3)
- [x] arch-usability — Usability patterns (Nielsen's heuristics)
- [x] arch-accessibility — WCAG compliance (ARIA)
- [x] arch-compliance — Regulatory compliance (GDPR, HIPAA)

### Phase 6: Governance
- [x] arch-governance — Architecture governance

### Phase 7: Documentation & Testing
- [x] README.md — Complete project documentation
- [x] AGENTS.md — Agent instructions
- [x] docs/coverage-analysis.md — Test coverage matrix
- [x] docs/best-practices-master.md — Best practices cross-reference
- [x] tests/test_skills.py — 175 structural tests
- [x] tests/test-arch-*.yaml — 152 skillprobe scenarios
- [x] sync-skills.ps1 / sync-skills.sh — Cross-platform sync

## Project Status

| Metric | Value |
|--------|-------|
| Skills | 25 |
| Structural Tests | 175 |
| Skill Scenarios | 152 |
| Total Tests | 327 |
| References | 40+ |
| Assets | 25+ |
| NFR Coverage | 100% |

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
├── docs/
│   ├── coverage-analysis.md
│   ├── skill-testing.md
│   └── best-practices-master.md
├── skills/ (25 skills)
└── tests/
    ├── test_skills.py
    ├── test-arch-*.yaml
    └── test-dar.md
```
