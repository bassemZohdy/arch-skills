---
name: arch-cost
description: Optimize cloud costs and design FinOps architecture. Use when modeling workload cost, measuring unit economics, implementing FinOps practices, right-sizing resources, managing commitments and anomalies, or establishing cost governance and budgets.
---

# Cost Optimization Architecture

Systematic approach to cost management and optimization.

## DAP contribution

For a DAP invocation, read `framework/contribution-contract.md` from the outer
package root (the repository root in a source checkout). Keep standalone tasks
within their requested scope. Use `assets/review-template.md` and record currency and time horizon, dated rate sources, demand/commitment assumptions, unit economics, forecast uncertainty and approval threshold.
Return evidence-linked proposals and VER plans, not invented approvals or delivery proof.

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
6. **Use the cloud's variable-cost model deliberately** - Automate visibility and optimization where it is safe

### FinOps Domains

| Domain | Activities |
|-------|------------|
| **Understand usage and cost** | Visibility, allocation, forecasting and benchmarking |
| **Quantify business value** | Unit economics, value metrics and trade-offs |
| **Optimize usage and cost** | Right-sizing, commitments, architecture and waste reduction |
| **Manage practice** | Policies, accountability, automation and continuous improvement |

## Step 2: Cost Allocation

Apply the Inform, Optimize and Operate phases across these domains; phases and
domains are different dimensions. Use `references/finops-reference.md` and pin
the adopted [FinOps Framework](https://www.finops.org/framework/) revision.

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

Treat savings percentages as illustrative, not promises. Measure before/after cost
and service impact using provider-specific rates, workload shape, utilization,
commitment risk and egress. Prefer cost per business outcome (for example,
transaction, tenant or inference request) over spend alone.

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

Track forecast error, commitment utilization, idle spend, egress and cost
anomalies. Make ownership and remediation time explicit for every alert.

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
- Buying a commitment before workload and utilization are stable can turn a saving into stranded capacity.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)
- `references/finops-reference.md` — FinOps Reference

The [FinOps Framework](https://www.finops.org/framework/) is a living reference;
pin the version used by the organization and record the business-value metric
that justifies each optimization.

## Related Skills

- **arch-cloud** - Provider services and Well-Architected cost pillar
- **arch-devops** - IaC enforcement of tagging and budgets
- **arch-ai** - Inference spend budgeting

## Output template

Use `assets/review-template.md`. Populate its scope and evidence fields for DAP work;
keep missing measurements and approvals explicit.
