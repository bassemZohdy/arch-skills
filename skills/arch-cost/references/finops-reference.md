# FinOps Reference

## FinOps Principles

1. **Teams need to collaborate** - Engineering, finance, business work together
2. **Everyone takes ownership** - Cost awareness at all levels
3. **A centralized team drives FinOps** - Coordinated approach
4. **Reports should be accessible** - Real-time cost data
5. **Decisions are data-driven** - Cost/quality trade-offs

## Cost Optimization Strategies

### Compute

| Strategy | Savings | Effort |
|----------|---------|--------|
| Right-sizing | 20-40% | Low |
| Reserved Instances | 30-60% | Low |
| Spot Instances | 60-90% | Medium |
| Auto-scaling | 10-30% | Medium |
| Serverless | Variable | High |

### Storage

| Strategy | Savings | Effort |
|----------|---------|--------|
| Tiering | 30-50% | Low |
| Compression | 20-40% | Medium |
| Lifecycle Policies | 20-40% | Low |

## Cost Metrics

| Metric | Description |
|--------|-------------|
| Total Cost | Overall spending |
| Cost per User | Efficiency metric |
| Cost per Transaction | Business metric |
| Cost Trend | Month-over-month change |
| Budget Variance | Actual vs budgeted |

## Tagging Strategy

| Tag | Purpose | Example |
|-----|---------|---------|
| Team | Owning team | backend, frontend |
| Project | Initiative | feature-x, refactor-y |
| Environment | Deployment stage | dev, staging, prod |
| Cost Center | Financial tracking | engineering, marketing |
