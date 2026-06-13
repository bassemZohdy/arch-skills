---
name: arch-governance
description: Guide architecture governance. Use when establishing architecture boards, defining architecture standards, implementing compliance processes, or managing architecture debt.
---

# Architecture Governance

Systematic approach to architecture governance.

## Workflow

```
1. Define Standards → What rules apply?
2. Establish Processes → How to comply?
3. Create Board → Who decides?
4. Implement Reviews → When to review?
5. Monitor Compliance → Are we following rules?
6. Manage Exceptions → What if we can't comply?
```

## Step 1: Architecture Standards

### Standard Types

| Type | Description | Example |
|------|-------------|---------|
| **Principles** | High-level guiding rules | "Use cloud-native services" |
| **Patterns** | Approved design patterns | "Use API Gateway pattern" |
| **Standards** | Specific technology standards | "Use PostgreSQL for databases" |
| **Guidelines** | Recommended practices | "Prefer REST over SOAP" |

### Architecture Principles

| Principle | Description |
|-----------|-------------|
| **Business Alignment** | Architecture supports business goals |
| **Simplicity** | Prefer simple solutions |
| **Reusability** | Leverage existing components |
| **Interoperability** | Systems should communicate easily |
| **Security** | Security by design |
| **Scalability** | Design for growth |
| **Maintainability** | Easy to modify and extend |

## Step 2: Architecture Board

### Board Structure

| Role | Responsibility |
|------|----------------|
| **Chair** | Leads reviews, final decisions |
| **Members** | Domain experts, senior architects |
| **Secretary** | Documents decisions, maintains records |
| **Stakeholders** | Business representatives |

### Board Activities

| Activity | Frequency |
|----------|-----------|
| **Architecture Reviews** | Per project |
| **Standards Updates** | Quarterly |
| **Technology Radar** | Monthly |
| **Exception Reviews** | As needed |

## Step 3: Review Process

### Review Types

| Type | Scope | Trigger |
|------|-------|---------|
| **Pre-Project** | Initial design | New project |
| **Milestone** | Progress review | Project phases |
| **Ad-Hoc** | Specific concern | Issue raised |
| **Audit** | Compliance check | Scheduled |

### Review Checklist

- [ ] Principles compliance
- [ ] Standards adherence
- [ ] Pattern usage
- [ ] Security review
- [ ] Performance review
- [ ] Cost review
- [ ] Risk assessment

## Step 4: Exception Management

### Exception Process

1. **Request** - Document exception need
2. **Assess** - Evaluate risk and impact
3. **Decide** - Approve or deny
4. **Document** - Record decision and rationale
5. **Monitor** - Track exception status

### Exception Categories

| Category | Description | Approval |
|----------|-------------|----------|
| **Technical** | Technology exception | Architecture Board |
| **Process** | Process exception | Management |
| **Resource** | Resource exception | Finance |

## Step 5: Architecture Debt

### Debt Categories

| Category | Description |
|----------|-------------|
| **Standards Debt** | Non-compliant implementations |
| **Pattern Debt** | Missing or incorrect patterns |
| **Technology Debt** | Outdated technologies |
| **Process Debt** | Skipped reviews |

### Debt Management

1. **Identify** - Track exceptions and deviations
2. **Assess** - Evaluate risk and impact
3. **Prioritize** - Focus on high-risk items
4. **Remediate** - Plan and execute fixes
5. **Prevent** - Update standards to prevent recurrence

## Step 6: Compliance Monitoring

### Compliance Metrics

| Metric | Target |
|--------|--------|
| **Standards Compliance** | > 90% |
| **Review Coverage** | 100% of projects |
| **Exception Rate** | < 10% |
| **Debt Trend** | Decreasing |

### Monitoring Tools

| Tool | Purpose |
|------|---------|
| **Architecture Repository** | Store standards, decisions |
| **Review Tracking** | Track review status |
| **Exception Management** | Manage exceptions |
| **Reporting** | Compliance dashboards |

## Governance Review Template

```markdown
## Governance Review: [Organization]

### Standards
| Standard | Status | Compliance |
|----------|--------|------------|

### Reviews
| Review Type | Frequency | Last Conducted |
|-------------|-----------|----------------|

### Exceptions
| Exception | Risk | Status | Owner |
|-----------|------|--------|-------|

### Debt
| Category | Items | Trend |
|----------|-------|-------|

### Recommendations
1. [Improvement]
```
