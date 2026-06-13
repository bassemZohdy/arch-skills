# Architecture Review Methods

## ATAM (Architecture Tradeoff Analysis Method)

### Steps

1. **Present ATAM** - Explain the method
2. **Present Business Drivers** - Describe business context
3. **Present Architecture** - Describe the architecture
4. **Identify Architectural Approaches** - Find patterns used
5. **Generate Quality Attribute Utility Tree** - Prioritize quality attributes
6. **Analyze Architectural Approaches** - Evaluate approaches

### Quality Attribute Utility Tree

```
Utility
├── Performance
│   ├── Latency
│   │   └── Scenario: 95% < 200ms
│   └── Throughput
│       └── Scenario: 1000 req/s
├── Security
│   ├── Authentication
│   │   └── Scenario: MFA required
│   └── Authorization
│       └── Scenario: RBAC enforced
└── Availability
    ├── Uptime
    │   └── Scenario: 99.9% SLA
    └── Recovery
        └── Scenario: < 1 hour MTTR
```

## SAAM (Software Architecture Analysis Method)

### Steps

1. **Develop Description** - Document architecture
2. **Identify Scenarios** - Use cases and quality scenarios
3. **Analyze Architectural Approach** - Evaluate each scenario
4. **Evaluate Overall Architecture** - Assess overall quality

### Scenario Categories

| Category | Description |
|----------|-------------|
| **Use Scenarios** | Typical user interactions |
| **Change Scenarios** | Modifications to the system |
| **Growth Scenarios** | Scaling requirements |

## Review Checklist

### Architecture Quality

- [ ] Principles compliance
- [ ] Standards adherence
- [ ] Pattern usage
- [ ] Security review
- [ ] Performance review
- [ ] Cost review
- [ ] Risk assessment
- [ ] Documentation completeness

### Process Quality

- [ ] Stakeholder involvement
- [ ] Decision documentation
- [ ] Exception handling
- [ ] Follow-up actions
