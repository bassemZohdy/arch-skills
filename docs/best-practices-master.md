# Architecture Best Practices Master Reference

Comprehensive best practices compiled from industry standards and research.

## Research Sources

| Source | Focus | URL |
|--------|-------|-----|
| C4 Model | Architecture documentation | c4model.com |
| arc42 | Documentation template | arc42.org |
| OWASP ASVS 5.0 | Security verification | owasp.org |
| WCAG 2.2 | Accessibility | w3.org/WAI |
| Google SRE | Reliability engineering | sre.google |
| Thoughtworks Radar | Technology trends | thoughtworks.com/radar |
| Microsoft Azure WAF | Cloud architecture | azure.microsoft.com |
| AWS Well-Architected | Cloud architecture | aws.amazon.com |
| ISO 25010 | Quality model | iso.org |
| Building Evolutionary Architectures | Architecture patterns | O'Reilly |

## Quick Reference by Skill

### Core Architecture

| Skill | Key Best Practices | Standards |
|-------|-------------------|-----------|
| arch-doc | C4 checklist, arc42 structure, diagram clarity | C4, arc42, TOGAF |
| arch-review | Multi-dimensional evaluation, severity scoring | ISO 25010 |
| arch-fitness | Automated validation, CI/CD integration | ArchUnit |
| arch-decision | Weighted scoring, sensitivity analysis | DAR methodology |

### Technical Architecture

| Skill | Key Best Practices | Standards |
|-------|-------------------|-----------|
| arch-security | STRIDE/DREAD, OWASP Top 10, least privilege | OWASP ASVS 5.0 |
| arch-perf | SLA/SLO/Error Budget, caching layers | Google SRE |
| arch-resilience | Circuit breaker, bulkhead, chaos engineering | Netflix Hystrix |
| arch-test | Test pyramid, contract testing, mutation testing | Testing Trophy |

### System Architecture

| Skill | Key Best Practices | Standards |
|-------|-------------------|-----------|
| arch-api | REST maturity, GraphQL schema-first, gRPC proto | OpenAPI 3.1 |
| arch-cloud | Well-Architected pillars, FinOps, multi-cloud | AWS/Azure WAF |
| arch-event | Event ordering, idempotency, schema evolution | CloudEvents |
| arch-ddd | Bounded contexts, ubiquitous language, aggregates | Eric Evans DDD |
| arch-data | Data lineage, quality dimensions, governance | DAMA-DMBOK |
| arch-metrics | Cyclomatic complexity, coupling metrics | SIG maintainability |

### Operations

| Skill | Key Best Practices | Standards |
|-------|-------------------|-----------|
| arch-observability | Three pillars, RED/USE methods, OpenTelemetry | Google SRE |
| arch-migration | Strangler fig, rollback strategies, risk assessment | Martin Fowler |
| arch-deployment | Blue-green, canary, GitOps, immutable artifacts | DORA metrics |

### Non-Functional Requirements

| Skill | Key Best Practices | Standards |
|-------|-------------------|-----------|
| arch-usability | Nielsen's heuristics, user research methods | ISO 9241 |
| arch-accessibility | WCAG 2.2 POUR principles, ARIA patterns | WCAG 2.2 |
| arch-compliance | GDPR principles, audit trails, data classification | GDPR, HIPAA, SOC 2 |

## Key Metrics by Domain

### Performance
- Response time: p95 < 200ms
- Throughput: context-dependent
- Error rate: < 0.1%
- Availability: 99.9% (8.76 hrs/year)

### Security
- OWASP Top 10: All addressed
- Vulnerability scan: 0 critical/high
- Dependency audit: Weekly
- Penetration test: Quarterly

### Reliability
- MTBF: > 720 hours
- MTTR: < 1 hour
- Error budget: Monitored
- Incident response: Documented

### Quality
- Code coverage: > 80%
- Technical debt: Decreasing trend
- Documentation: Current
- Tests: All passing
