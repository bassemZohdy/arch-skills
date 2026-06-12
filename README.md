# Architecture Skills

[![Tests](https://img.shields.io/badge/tests-140%20passing-brightgreen)]()
[![Skills](https://img.shields.io/badge/skills-20-blue)]()
[![Scenarios](https://img.shields.io/badge/scenarios-97-orange)]()

A comprehensive collection of 20 Codex skills for software architecture documentation, review, validation, and governance. Covers all major non-functional requirements (NFRs) with best practices from industry standards.

## Skills Overview

### Core Architecture Skills

| Skill | Purpose | Key Topics |
|-------|---------|------------|
| **arch-doc** | Generate architecture documentation | C4, arc42, TOGAF, ISO 42010, ADRs |
| **arch-review** | Orchestrate architecture reviews | Review methodology, scoring, reporting |
| **arch-fitness** | Create fitness functions | ArchUnit/ArchUnitTS, CI/CD validation |
| **arch-decision** | DAR methodology | Weighted scoring, sensitivity analysis |

### Technical Architecture Skills

| Skill | Purpose | Key Topics |
|-------|---------|------------|
| **arch-security** | Security architecture | STRIDE, DREAD, OWASP, compliance |
| **arch-perf** | Performance engineering | SLA/SLO, caching, load testing |
| **arch-resilience** | Resilience patterns | Circuit breaker, retry, bulkhead |
| **arch-test** | Test architecture | Test pyramids, contract testing |

### System Architecture Skills

| Skill | Purpose | Key Topics |
|-------|---------|------------|
| **arch-api** | API design | REST, GraphQL, gRPC, versioning |
| **arch-cloud** | Cloud-native architecture | Well-Architected, FinOps, multi-cloud |
| **arch-event** | Event-driven architecture | CQRS, Event Sourcing, sagas |
| **arch-ddd** | Domain-Driven Design | Bounded contexts, aggregates, Event Storming |
| **arch-data** | Data architecture | Modeling, pipelines, governance |
| **arch-metrics** | Architecture metrics | Complexity, dependencies, debt |

### Operations Skills

| Skill | Purpose | Key Topics |
|-------|---------|------------|
| **arch-observability** | Observability | Logs, metrics, traces, alerting |
| **arch-migration** | Migration planning | Strangler fig, rollback, risk assessment |
| **arch-deployment** | Deployment architecture | CI/CD, blue-green, canary, GitOps |

### Non-Functional Requirements Skills

| Skill | Purpose | Key Topics |
|-------|---------|------------|
| **arch-usability** | Usability architecture | Nielsen's heuristics, user research |
| **arch-accessibility** | Accessibility | WCAG 2.1, ARIA, screen readers |
| **arch-compliance** | Regulatory compliance | GDPR, HIPAA, SOC 2, PCI DSS |

## Quick Start

### Installation

**Linux/Mac:**
```bash
chmod +x sync-skills.sh run-tests.sh
./sync-skills.sh
```

**Windows:**
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
```

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
│   └── skill-testing.md               # Skill testing guide
├── skills/                            # 20 architecture skills
│   ├── arch-doc/                      # Documentation generation
│   ├── arch-review/                   # Review orchestration
│   ├── arch-fitness/                  # Fitness functions
│   ├── arch-decision/                 # DAR methodology
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
│   ├── arch-observability/            # Observability
│   ├── arch-migration/                # Migration planning
│   ├── arch-deployment/               # Deployment strategy
│   ├── arch-usability/                # UX patterns
│   ├── arch-accessibility/            # WCAG compliance
│   └── arch-compliance/               # Regulatory compliance
└── tests/                             # Test suite
    ├── test_skills.py                 # Structural validation
    ├── test-arch-*.yaml               # Skillprobe scenarios
    └── test-dar.md                    # DAR math test data
```

## Skill Details

### arch-doc — Architecture Documentation

Generate comprehensive architecture documentation with diagrams.

**Frameworks Supported:**
- C4 Model (Context, Container, Component, Code)
- arc42 (12-section template)
- TOGAF (Architecture Development Method)
- ISO 42010 (Views and viewpoints)

**Diagram Formats:**
- Mermaid (primary)
- PlantUML (secondary)
- Draw.io (tertiary)

**Features:**
- Framework selection guidance
- ADR creation with MADR templates
- C4 diagram review checklist
- Tech stack considerations

### arch-review — Architecture Review

Orchestrate comprehensive architecture reviews.

**Review Dimensions:**
- Design patterns and anti-patterns
- Quality attributes (ISO 25010)
- Best practices (SOLID, DRY, KISS)
- Technical debt assessment
- Fitness functions validation

**Output:**
- Executive summary
- Findings by dimension
- Severity ratings
- Remediation roadmap

### arch-decision — Decision Analysis

Structured decision-making using DAR methodology.

**Process:**
1. Frame the decision
2. Define gate criteria
3. List alternatives
4. Create weighted scoring matrix
5. Evaluate and score
6. Sensitivity analysis
7. Generate recommendation
8. Document decision

**Features:**
- Expedited mode (2-4 criteria)
- Formal mode (3-7 criteria)
- Criteria library (5 bundles)
- DAR math validation script

### arch-security — Security Architecture

Threat modeling and security patterns.

**Frameworks:**
- STRIDE threat modeling
- DREAD risk assessment
- OWASP Top 10
- SOC 2, GDPR, HIPAA compliance

**Patterns:**
- Authentication (OAuth, JWT, MFA)
- Authorization (RBAC, ABAC)
- Data protection (encryption, masking)
- API security (rate limiting, input validation)

### arch-perf — Performance Engineering

Performance patterns and capacity planning.

**Topics:**
- SLA/SLO/error budgets
- Caching strategies (browser, CDN, Redis)
- Async processing (queues, streams)
- Database optimization
- Load testing (k6, JMeter, Locust)
- Performance budgets

### arch-resilience — Resilience Patterns

Fault tolerance for distributed systems.

**Patterns:**
- Circuit breaker
- Retry with exponential backoff
- Bulkhead isolation
- Timeout management
- Fallback strategies

**Testing:**
- Chaos engineering
- Fault injection
- Game day exercises

### arch-deployment — Deployment Architecture

CI/CD pipelines and deployment strategies.

**Strategies:**
- Blue-green deployment
- Canary releases
- Rolling updates
- Recreate

**CI/CD:**
- Pipeline stages
- Quality gates
- GitOps patterns
- Infrastructure as Code

## Testing

### Structural Validation (140 tests)

**Linux/Mac:**
```bash
./run-tests.sh
```

**Windows:**
```powershell
.\run-tests.ps1
```

**Tests:**
- Skill directory structure
- SKILL.md existence and frontmatter
- Reference files completeness
- Asset files presence
- Content quality (word count, sections)
- DAR weighted score calculations

### Skill Test Scenarios (97 scenarios)

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
| **Total** | **127** |

**Run with skillprobe:**
```bash
for f in tests/test-arch-*.yaml; do skillprobe run "$f" --harness claude-code; done
```

## NFR Coverage Matrix

| NFR | Skill | Coverage |
|-----|-------|----------|
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

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests (`./run-tests.sh`)
5. Submit a pull request

## License

MIT
