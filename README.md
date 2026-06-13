# Architecture Skills

[![Tests](https://img.shields.io/badge/tests-210%20passing-brightgreen)]()
[![Skills](https://img.shields.io/badge/skills-30-blue)]()
[![Scenarios](https://img.shields.io/badge/scenarios-172-orange)]()

A comprehensive collection of 30 Codex skills for software architecture documentation, review, validation, and governance. Covers all major non-functional requirements (NFRs) with best practices from industry standards.

## Quick Start

### Supported Harnesses

This skill set follows the [Agent Skills specification](https://agentskills.io/specification) and works with:

| Harness | Status | Path |
|---------|--------|------|
| **Claude Code** | ✅ | `~/.claude/skills/` |
| **OpenAI Codex** | ✅ | `~/.codex/skills/` |
| **Cursor** | ✅ | `.cursor/rules/` |
| **GitHub Copilot** | ✅ | `.github/copilot-instructions.md` |
| **Gemini CLI** | ✅ | `.gemini/skills/` |
| **JetBrains Junie** | ✅ | `.agents/skills/` |
| **OpenHands** | ✅ | `.agents/skills/` |
| **OpenCode** | ✅ | `.config/opencode/skills/` |
| **Pi (badlogic)** | ✅ | `.pi/skills/` |
| **Cline** | ✅ | `.cline/skills/` |
| **Kilo Code** | ✅ | `.kilo/skills/` |
| **MiMoCode** | ✅ | `.mimocode/skills/` |

### Installation

**Set up unified skills (single source of truth):**

```bash
python scripts/setup_unified.py
```

This creates symlinks from each tool's expected location to the central `skills/` directory. Changes to `skills/` are immediately visible to all tools.

**For Windows (if symlinks fail):**
```powershell
.\sync-skills.ps1
```

### Usage Examples

```
# Generate architecture documentation
Use arch-doc to create C4 diagrams for an e-commerce platform

# Review an architecture
Use arch-review to evaluate this microservices architecture

# Create fitness functions
Use arch-fitness to create ArchUnit tests for layer dependencies

# Make an architecture decision
Use arch-decision to help me choose between PostgreSQL and MongoDB

# Security review
Use arch-security to perform threat modeling for this API

# Performance analysis
Use arch-perf to design a caching strategy for this service

# Microservices design
Use arch-microservices to decompose this monolith

# Cost optimization
Use arch-cost to optimize our cloud spending

# Automate architecture validation
Use arch-automation to set up CI/CD for architecture checks
```

## Skills Overview

### Core Architecture (5 skills)

| Skill | Purpose | Key Topics |
|-------|---------|------------|
| **arch-doc** | Generate architecture documentation | C4, arc42, TOGAF, ISO 42010, ADRs |
| **arch-review** | Orchestrate architecture reviews | ATAM, SAAM, review methodology |
| **arch-fitness** | Create fitness functions | ArchUnit/ArchUnitTS, CI/CD validation |
| **arch-decision** | DAR methodology | Weighted scoring, sensitivity analysis |
| **arch-governance** | Architecture governance | Standards, boards, compliance |

### Technical Architecture (4 skills)

| Skill | Purpose | Key Topics |
|-------|---------|------------|
| **arch-security** | Security architecture | STRIDE, DREAD, OWASP, compliance |
| **arch-perf** | Performance engineering | SLA/SLO, caching, load testing |
| **arch-resilience** | Resilience patterns | Circuit breaker, retry, bulkhead |
| **arch-test** | Test architecture | Test pyramids, contract testing |

### System Architecture (10 skills)

| Skill | Purpose | Key Topics |
|-------|---------|------------|
| **arch-api** | API design | REST, GraphQL, gRPC, OpenAPI |
| **arch-cloud** | Cloud-native architecture | Well-Architected, FinOps, multi-cloud |
| **arch-event** | Event-driven architecture | CQRS, Event Sourcing, sagas |
| **arch-ddd** | Domain-Driven Design | Bounded contexts, aggregates |
| **arch-data** | Data architecture | Modeling, pipelines, governance |
| **arch-metrics** | Architecture metrics | Complexity, dependencies, debt |
| **arch-integration** | Integration patterns | Service mesh, API gateway, ESB |
| **arch-microservices** | Microservices architecture | Service decomposition, communication |
| **arch-patterns** | Architecture patterns | Clean, Hexagonal, Layered, Pipes & Filters |
| **arch-refactoring** | Refactoring patterns | Code smells, incremental improvement |

### Frontend (1 skill)

| Skill | Purpose | Key Topics |
|-------|---------|------------|
| **arch-frontend** | Frontend architecture | Micro frontends, UI patterns, SPA |

### Operations (5 skills)

| Skill | Purpose | Key Topics |
|-------|---------|------------|
| **arch-observability** | Observability | Logs, metrics, traces, alerting |
| **arch-migration** | Migration planning | Strangler fig, rollback, risk assessment |
| **arch-deployment** | Deployment architecture | CI/CD, blue-green, canary, GitOps |
| **arch-devops** | DevOps & infrastructure | IaC, Kubernetes, GitOps |
| **arch-cost** | Cost optimization | FinOps, cost modeling, optimization |

### Feature Management (1 skill)

| Skill | Purpose | Key Topics |
|-------|---------|------------|
| **arch-features** | Feature management | Feature flags, toggles, experimentation |

### Automation (1 skill)

| Skill | Purpose | Key Topics |
|-------|---------|------------|
| **arch-automation** | Architecture automation | CI/CD, documentation, infrastructure automation |

### Non-Functional Requirements (3 skills)

| Skill | Purpose | Key Topics |
|-------|---------|------------|
| **arch-usability** | Usability architecture | UX patterns, heuristics, user research |
| **arch-accessibility** | Accessibility | WCAG compliance, ARIA, assistive tech |
| **arch-compliance** | Regulatory compliance | GDPR, HIPAA, SOC 2, audit trails |

## Project Structure

```
arch-skills/
├── README.md                          # This file
├── AGENTS.md                          # Agent instructions
├── TODO.md                            # Task tracking
├── sync-skills.ps1                    # Sync script (Windows)
├── sync-skills.sh                     # Sync script (Linux/Mac)
├── run-tests.ps1                      # Test runner (Windows)
├── run-tests.sh                       # Test runner (Linux/Mac)
├── docs/                              # Documentation
│   ├── coverage-analysis.md           # Test coverage matrix
│   ├── skill-testing.md               # Skill testing guide
│   └── best-practices-master.md       # Best practices cross-reference
├── skills/                            # 30 architecture skills
│   ├── arch-doc/                      # Documentation generation
│   ├── arch-review/                   # Review orchestration
│   ├── arch-fitness/                  # Fitness functions
│   ├── arch-decision/                 # DAR methodology
│   ├── arch-governance/               # Architecture governance
│   ├── arch-security/                 # Security patterns
│   ├── arch-perf/                     # Performance engineering
│   ├── arch-resilience/               # Fault tolerance
│   ├── arch-test/                     # Test strategy
│   ├── arch-api/                      # API design
│   ├── arch-cloud/                    # Cloud patterns
│   ├── arch-event/                    # Event-driven
│   ├── arch-ddd/                      # Domain modeling
│   ├── arch-data/                     # Data architecture
│   ├── arch-metrics/                  # Metrics analysis
│   ├── arch-integration/              # Integration patterns
│   ├── arch-microservices/            # Microservices architecture
│   ├── arch-patterns/                 # Architecture patterns
│   ├── arch-refactoring/              # Refactoring patterns
│   ├── arch-frontend/                 # Frontend architecture
│   ├── arch-observability/            # Observability
│   ├── arch-migration/                # Migration planning
│   ├── arch-deployment/               # Deployment strategy
│   ├── arch-devops/                   # DevOps & infrastructure
│   ├── arch-cost/                     # Cost optimization
│   ├── arch-features/                 # Feature management
│   ├── arch-automation/               # Architecture automation
│   ├── arch-usability/                # UX patterns
│   ├── arch-accessibility/            # WCAG compliance
│   └── arch-compliance/               # Regulatory compliance
└── tests/                             # Test suite
    ├── test_skills.py                 # Structural validation
    ├── test-arch-*.yaml               # Skillprobe scenarios
    └── test-dar.md                    # DAR math test data
```

## Testing

### Structural Validation (210 tests)

**Linux/Mac:**
```bash
./run-tests.sh
```

**Windows:**
```powershell
.\run-tests.ps1
```

### Skill Test Scenarios (172 scenarios)

| Skill | Scenarios |
|-------|-----------|
| arch-doc | 12 |
| arch-review | 9 |
| arch-fitness | 9 |
| arch-decision | 9 |
| arch-security | 5 |
| arch-perf | 5 |
| arch-migration | 5 |
| arch-api | 5 |
| arch-cloud | 5 |
| arch-event | 5 |
| arch-ddd | 5 |
| arch-metrics | 5 |
| arch-resilience | 5 |
| arch-test | 5 |
| arch-data | 5 |
| arch-observability | 5 |
| arch-usability | 5 |
| arch-accessibility | 5 |
| arch-compliance | 5 |
| arch-deployment | 5 |
| arch-integration | 5 |
| arch-microservices | 5 |
| arch-devops | 5 |
| arch-cost | 5 |
| arch-governance | 5 |
| arch-patterns | 5 |
| arch-refactoring | 5 |
| arch-frontend | 5 |
| arch-features | 5 |
| arch-automation | 5 |
| **Total** | **172** |

**Run with skillprobe:**
```bash
for f in tests/test-arch-*.yaml; do skillprobe run "$f" --harness claude-code; done
```

## NFR Coverage Matrix

| NFR | Primary Skill | Status |
|-----|---------------|--------|
| Performance | arch-perf | ✅ |
| Scalability | arch-perf, arch-cloud | ✅ |
| Availability | arch-resilience | ✅ |
| Reliability | arch-resilience | ✅ |
| Security | arch-security | ✅ |
| Maintainability | arch-metrics | ✅ |
| Testability | arch-test | ✅ |
| Observability | arch-observability | ✅ |
| Deployability | arch-deployment | ✅ |
| Usability | arch-usability | ✅ |
| Accessibility | arch-accessibility | ✅ |
| Compliance | arch-compliance | ✅ |
| Data Integrity | arch-data | ✅ |
| Auditability | arch-compliance | ✅ |
| Recoverability | arch-resilience | ✅ |
| Modifiability | arch-metrics | ✅ |

## Research Sources

- [C4 Model](https://c4model.com/) — Official C4 documentation
- [arc42](https://arc42.org/) — Architecture documentation template
- [MADR](https://github.com/joelparkerhenderson/architecture-decision-record) — ADR templates
- [ArchUnit](https://www.archunit.org/) — Java architecture testing
- [ISO 25010](https://www.iso.org/standard/35733.html) — Quality model
- [DAR Skill](https://github.com/DAR_Platform/DAR_Skill) — DAR methodology
- [OWASP](https://owasp.org/) — Security best practices
- [Google SRE](https://sre.google/) — Reliability engineering
- [Thoughtworks Radar](https://www.thoughtworks.com/radar) — Technology trends
- [Agent Skills](https://agentskills.io/) — Agent Skills specification
- [microservices.io](https://microservices.io/) — Microservices patterns
- [FinOps Foundation](https://www.finops.org/) — FinOps framework
- [Kubernetes](https://kubernetes.io/) — Container orchestration
- [Martin Fowler](https://martinfowler.com/) — Software architecture patterns

## License

MIT
