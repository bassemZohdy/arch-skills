# Quality Attributes Reference

## Versioned product-quality model

Use [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) as the current
product-quality model, which has nine characteristics. Record the selected
edition and consult its authoritative definitions for detailed criterion mapping.

Organize review concerns around functional suitability, performance efficiency,
compatibility, interaction capability, reliability, security, maintainability,
flexibility and safety. Do not label the older eight-characteristic model as the
2023 edition or imply formal ISO conformity from this review checklist.

Targets below are illustrative; adopt scenario-specific thresholds and evidence
with the accountable owner before using them as project gates.

## Quality Attribute Scenarios

Each quality attribute should be documented as a scenario with six parts:

```markdown
## Quality Attribute Scenario: [Name]

### Source
[External entity that triggers the stimulus]

### Stimulus
[Event that arrives at the system]

### Environment
[System state when stimulus occurs]

### Artifact
[Part of the system affected]

### Response
[System response to stimulus]

### Response Measure
[How response is measured]
```

### Example: Performance Scenario

```markdown
## Scenario: Normal Load Response Time

### Source
User

### Stimulus
Browse product catalog

### Environment
Normal operation (not peak)

### Artifact
Web Application

### Response
Display product list within 2 seconds

### Response Measure
95th percentile < 2000ms
```

### Example: Security Scenario

```markdown
## Scenario: Unauthorized Access Attempt

### Source
Attacker

### Stimulus
Attempt to access admin functions without authentication

### Environment
Production

### Artifact
API Gateway

### Response
Reject request, log attempt, alert security team

### Response Measure
- Response time < 100ms
- Alert within 1 minute
- No data exposure
```

## Performance Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Response Time (p50) | < 100ms | APM tools |
| Response Time (p95) | < 200ms | APM tools |
| Response Time (p99) | < 500ms | APM tools |
| Throughput | > 1000 req/s | Load testing |
| CPU Utilization | < 70% | Monitoring |
| Memory Utilization | < 80% | Monitoring |

## Scalability Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Horizontal Scale | Linear | Load testing |
| Time to Scale | < 5 min | Auto-scaling metrics |
| Data Growth | Supported | Capacity planning |

## Security Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Vulnerabilities | 0 critical/high | Security scanning |
| Authentication | MFA | Audit |
| Authorization | RBAC | Audit |
| Data Encryption | At rest + transit | Audit |

## Availability Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Uptime | 99.9% | Monitoring |
| MTBF | > 720 hours | Incident tracking |
| MTTR | < 1 hour | Incident tracking |
| Recovery Point | < 1 hour | Backup testing |

## Maintainability Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Code Coverage | > 80% | Test reports |
| Cyclomatic Complexity | < 10 | Static analysis |
| Technical Debt | Decreasing | SonarQube |
| Documentation | Complete | Audit |

## Review Checklists

### Performance Review
- [ ] Caching strategy implemented
- [ ] Database queries optimized
- [ ] Async processing for long operations
- [ ] Connection pooling configured
- [ ] Resource limits set

### Scalability Review
- [ ] Stateless services (can scale horizontally)
- [ ] Database sharding/replication strategy
- [ ] Load balancer configured
- [ ] Auto-scaling rules defined
- [ ] Rate limiting implemented

### Security Review
- [ ] Input validation
- [ ] SQL injection prevention
- [ ] XSS protection
- [ ] CSRF protection
- [ ] Secure configuration management
- [ ] Secrets management
- [ ] Audit logging

### Availability Review
- [ ] Redundancy at all levels
- [ ] Health checks implemented
- [ ] Circuit breakers configured
- [ ] Failover mechanisms tested
- [ ] Disaster recovery plan documented

### Maintainability Review
- [ ] Code follows style guidelines
- [ ] SOLID principles adhered
- [ ] Tests are comprehensive
- [ ] Documentation is current
- [ ] Logging is adequate
- [ ] Configuration is externalized
