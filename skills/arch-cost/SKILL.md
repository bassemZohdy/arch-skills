---
name: arch-cost
description: Guide cost optimization and FinOps architecture. Use when optimizing cloud costs, implementing FinOps practices, modeling infrastructure costs, or establishing cost governance.
---

# Cost Optimization Architecture

Systematic approach to cost management and optimization.

## Workflow

```
1. Understand Costs → Where is money spent?
2. Allocate Costs → Tag resources by team/project
3. Optimize → Right-size, reserved instances
4. Monitor → Track spending trends
5. Govern → Budgets, alerts, policies
6. Report → Cost visibility to stakeholders
```

## Step 1: FinOps Framework

### FinOps Principles

1. **Teams need to collaborate** - Engineering, finance, business work together
2. **Everyone takes ownership** - Cost awareness at all levels
3. **A centralized team drives FinOps** - Coordinated approach
4. **Reports should be accessible** - Real-time cost data
5. **Decisions are data-driven** - Cost/quality trade-offs
6. **Varies by cloud provider** - Leverage provider tools

### FinOps Phases

| Phase | Activities |
|-------|------------|
| **Inform** | Visibility, allocation, benchmarking |
| **Optimize** | Right-sizing, reservations, savings plans |
| **Operate** | Continuous improvement, automation |

## Step 2: Cost Allocation

### Tagging Strategy

| Tag | Purpose | Example |
|-----|---------|---------|
| **Team** | Owning team | backend, frontend |
| **Project** | Initiative | feature-x, refactor-y |
| **Environment** | Deployment stage | dev, staging, prod |
| **Cost Center** | Financial tracking | engineering, marketing |

### Cost Allocation Methods

| Method | Description |
|--------|-------------|
| **Tag-Based** | Allocate by resource tags |
| **Account-Based** | Separate accounts per team |
| **Service-Based** | Allocate by service consumption |

## Step 3: Optimization Strategies

### Compute Optimization

| Strategy | Savings | Effort |
|----------|---------|--------|
| **Right-sizing** | 20-40% | Low |
| **Reserved Instances** | 30-60% | Low |
| **Spot Instances** | 60-90% | Medium |
| **Auto-scaling** | 10-30% | Medium |
| **Serverless** | Variable | High |

### Storage Optimization

| Strategy | Savings | Effort |
|----------|---------|--------|
| **Tiering** | 30-50% | Low |
| **Compression** | 20-40% | Medium |
| **Deduplication** | 10-30% | Medium |
| **Lifecycle Policies** | 20-40% | Low |

### Database Optimization

| Strategy | Savings | Effort |
|----------|---------|--------|
| **Reserved Capacity** | 30-60% | Low |
| **Right-sizing** | 20-40% | Low |
| **Read Replicas** | Performance | Medium |
| **Caching** | 30-50% | Medium |

## Step 4: Cost Monitoring

### Key Metrics

| Metric | Description |
|--------|-------------|
| **Total Cost** | Overall spending |
| **Cost per User** | Efficiency metric |
| **Cost per Transaction** | Business metric |
| **Cost Trend** | Month-over-month change |
| **Budget Variance** | Actual vs budgeted |

### Cost Anomaly Detection

| Pattern | Action |
|---------|--------|
| **Sudden spike** | Investigate immediately |
| **Gradual increase** | Review optimization |
| **Seasonal pattern** | Plan for peaks |
| **New resource** | Verify necessity |

## Step 5: Cost Governance

### Budget Management

| Level | Action |
|-------|--------|
| **Budget set** | Define monthly/quarterly budgets |
| **Alerts** | 50%, 80%, 100% thresholds |
| **Reviews** | Weekly cost reviews |
| **Optimization** | Monthly optimization sprints |

### Cost Review Process

1. **Weekly**: Team-level cost review
2. **Monthly**: Department-level analysis
3. **Quarterly**: Strategic optimization planning
4. **Annual**: Budget planning and forecasting

## Step 6: Cost Reporting

### Dashboard Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Monthly spend | [Budget] | [Actual] |
| Cost per user | [Target] | [Actual] |
| Optimization savings | [Target] | [Actual] |
| Waste reduction | [Target] | [Actual] |

## Examples

- Build a tagging and allocation model so each team sees its own cloud spend.
- Cut compute cost with right-sizing plus reserved instances for steady load.
- Set budget alerts and anomaly detection before a usage-based launch.

## Common Gotchas

- Reserved capacity bought before right-sizing locks in the waste.
- Untagged resources make allocation guesswork; enforce tags at provision time via IaC.
- Optimizing unit cost while ignoring cost-per-transaction can hide real efficiency losses.

## Related Skills

- **arch-cloud** - Provider services and Well-Architected cost pillar
- **arch-devops** - IaC enforcement of tagging and budgets
- **arch-ai** - Inference spend budgeting

## Cost Review Template

```markdown
## Cost Review: [System]

### Current Spend
- Monthly: [Amount]
- Trend: [Increasing/Stable/Decreasing]

### Cost Breakdown
| Category | Amount | % of Total |
|----------|--------|------------|

### Optimization Opportunities
| Opportunity | Potential Savings | Effort |
|-------------|-------------------|--------|

### Recommendations
1. [High impact]
2. [Medium impact]
```
