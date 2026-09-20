---
name: arch-cloud
description: Design cloud-native architecture. Use when designing cloud architectures, applying Well-Architected reviews, planning landing zones and workload identity, evaluating multi-cloud or hybrid strategies, optimizing cloud costs and egress, or migrating to cloud.
---

# Cloud-Native Architecture

Systematic approach to designing cloud-native systems.

## DAP contribution

For a DAP invocation, read `framework/contribution-contract.md` from the outer
package root (the repository root in a source checkout). Keep standalone tasks
within their requested scope. Use `assets/architecture-template.md` and record workload constraints, dated regional/quota/rate evidence, identity boundaries, data residency, recovery and exit decisions.
Return evidence-linked proposals and VER plans, not invented approvals or delivery proof.

## Workflow

```
1. Define Requirements → What do we need?
2. Choose Provider → AWS, Azure, GCP, or multi-cloud?
3. Design Architecture → Apply cloud patterns
4. Optimize Costs → FinOps practices
5. Implement → Use managed services
```

## Step 1: Well-Architected Framework

### AWS Pillars

| Pillar | Focus |
|--------|-------|
| **Operational Excellence** | Run and monitor systems |
| **Security** | Protect data and systems |
| **Reliability** | Recover from failures |
| **Performance Efficiency** | Use resources efficiently |
| **Cost Optimization** | Avoid unnecessary costs |
| **Sustainability** | Minimize environmental impact |

### Azure Pillars

| Pillar | Focus |
|--------|-------|
| **Reliability** | Resilience and recovery |
| **Security** | Defense in depth |
| **Cost Optimization** | Maximize value |
| **Operational Excellence** | Simplify operations |
| **Performance Efficiency** | Scale effectively |

## Step 2: Cloud Patterns

Before selecting a managed service, record its workload fit, regional and quota
dependencies, identity model, failure and recovery behavior, data residency,
egress/data-gravity cost, operational ownership and exit implications. Prefer a
managed service when its operational reduction outweighs lock-in and platform
coupling for the stated requirements.

### Compute Patterns

| Pattern | Use Case | Services |
|---------|----------|----------|
| **Containers** | Microservices, portability | ECS, EKS, AKS, GKE |
| **Serverless** | Event-driven, APIs | Lambda, Functions |
| **VMs** | Legacy, specific OS | EC2, VMs, Compute Engine |

### Data Patterns

| Pattern | Use Case | Services |
|---------|----------|----------|
| **Managed Database** | Traditional workloads | RDS, Cloud SQL |
| **NoSQL** | Flexible schema, scale | DynamoDB, Cosmos DB |
| **Data Warehouse** | Analytics | Redshift, BigQuery |
| **Cache** | Performance | ElastiCache, Memorystore |

### Integration Patterns

| Pattern | Use Case | Services |
|---------|----------|----------|
| **Message Queue** | Async communication | SQS, Service Bus |
| **Event Streaming** | Event-driven | Kafka, EventBridge |
| **API Gateway** | External APIs | API Gateway, APIM |

## Step 3: Multi-Cloud Strategy

| Strategy | Description | When to Use |
|----------|-------------|-------------|
| **Cloud-Agnostic** | Use abstractions | Portability needed |
| **Best-of-Breed** | Pick best per service | Specific requirements |
| **Hybrid** | On-prem + cloud | Compliance, gradual migration |

### Cloud-Agnostic Tools

- **Terraform** — Infrastructure as Code
- **Kubernetes** — Container orchestration
- **Pulumi** — IaC with programming languages
- **Docker** — Containerization

## Step 4: Cost Optimization

### FinOps Practices

1. **Visibility** — Track all costs
2. **Allocation** — Tag resources by team/project
3. **Optimization** — Right-size, reserved instances
4. **Governance** — Budgets, alerts, policies

### Cost Reduction Strategies

| Strategy | Savings | Effort |
|----------|---------|--------|
| Reserved instances | 30-60% | Low |
| Spot instances | 60-90% | Medium |
| Right-sizing | 20-40% | Low |
| Auto-scaling | 10-30% | Medium |
| Storage tiering | 30-50% | Low |

Savings percentages are illustrative only. Validate them against current provider
rates, utilization, workload shape, commitments, egress and reliability impact.

## Examples

- Run a Well-Architected review of an AWS workload before a compliance audit.
- Choose between serverless and containers for a spiky background workload.
- Design a hybrid architecture keeping regulated data on-premises.

## Common Gotchas

- Cloud-agnostic abstractions cost real engineering effort; only pay for portability you actually need.
- Lift-and-shift without re-architecting usually raises costs instead of lowering them.
- Egress fees and cross-AZ traffic are the silent budget killers.
- A landing zone is not secure by default; verify identity boundaries, policy enforcement, logging, recovery and break-glass access.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)
- `references/cloud-deep-dive.md` — Cloud Architecture Deep Dive
- `references/cloud-patterns.md` — Cloud Patterns Reference

## Related Skills

- **arch-migration** - Legacy modernization, strangler fig, rollback strategies
- **arch-devops** - IaC, CI/CD, Kubernetes, and deployment strategies
- **arch-cost** - FinOps practices and cost governance in depth
- **arch-observability** - Logging, metrics, tracing, alerting
- **arch-data** - Data modeling, pipelines, governance
- **arch-perf** - Caching, capacity planning, load testing

## Output template

Use `assets/architecture-template.md`. Populate its scope and evidence fields for DAP work;
keep missing measurements and approvals explicit.
