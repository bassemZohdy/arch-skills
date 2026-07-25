---
name: arch-cloud
description: Design cloud-native architecture. Use when designing cloud architectures, implementing Well-Architected Framework principles, planning multi-cloud strategies, optimizing cloud costs, or migrating to cloud.
---

# Cloud-Native Architecture

Systematic approach to designing cloud-native systems.

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

## Examples

- Run a Well-Architected review of an AWS workload before a compliance audit.
- Choose between serverless and containers for a spiky background workload.
- Design a hybrid architecture keeping regulated data on-premises.

## Common Gotchas

- Cloud-agnostic abstractions cost real engineering effort; only pay for portability you actually need.
- Lift-and-shift without re-architecting usually raises costs instead of lowering them.
- Egress fees and cross-AZ traffic are the silent budget killers.

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

## Cloud Review Template

```markdown
## Cloud Architecture Review: [System]

### Provider
- Primary: [AWS/Azure/GCP]
- Services: [List]

### Well-Architected Assessment
| Pillar | Score | Issues |
|--------|-------|--------|

### Cost Analysis
- Monthly spend: [Amount]
- Optimization opportunities: [List]

### Recommendations
1. [High priority]
2. [Medium priority]
```
