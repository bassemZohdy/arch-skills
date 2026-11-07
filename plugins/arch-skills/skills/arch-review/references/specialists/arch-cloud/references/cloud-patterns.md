# Cloud Patterns Reference

## Compute Patterns

| Pattern | Services | Use Case |
|---------|----------|----------|
| **Containers** | ECS, EKS, AKS, GKE | Microservices |
| **Serverless** | Lambda, Functions | Event-driven |
| **VMs** | EC2, VMs | Legacy, specific OS |

## Data Patterns

| Pattern | Services | Use Case |
|---------|----------|----------|
| **Managed DB** | RDS, Cloud SQL | Traditional workloads |
| **NoSQL** | DynamoDB, Cosmos DB | Flexible schema |
| **Data Warehouse** | Redshift, BigQuery | Analytics |
| **Cache** | ElastiCache, Memorystore | Performance |

## Well-Architected Pillars

These concerns are shared by AWS and Azure. AWS also includes sustainability;
use the provider-specific pillar sets in [cloud-deep-dive.md](cloud-deep-dive.md).

| Pillar | Key Questions |
|--------|---------------|
| **Operational Excellence** | How do you run and monitor systems? |
| **Security** | How do you protect data and systems? |
| **Reliability** | How do you recover from failures? |
| **Performance** | How do you use resources efficiently? |
| **Cost** | How do you avoid unnecessary costs? |

## Cost Optimization

Treat the following savings ranges as illustrative only. Model current prices,
commitment utilization, interruption tolerance and operating costs for the workload.

| Strategy | Savings | Effort |
|----------|---------|--------|
| Reserved instances | 30-60% | Low |
| Spot instances | 60-90% | Medium |
| Right-sizing | 20-40% | Low |
| Auto-scaling | 10-30% | Medium |
