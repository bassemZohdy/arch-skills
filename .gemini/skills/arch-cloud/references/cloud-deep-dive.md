# Cloud Architecture Deep Dive

**Source:** AWS Well-Architected, Azure Well-Architected, GCP Architecture Center

## Well-Architected Framework Pillars

### AWS Pillars

| Pillar | Focus | Key Questions |
|--------|-------|---------------|
| **Operational Excellence** | Run and monitor systems | How do you run and monitor systems? |
| **Security** | Protect data and systems | How do you protect data and systems? |
| **Reliability** | Recover from failures | How do you recover from failures? |
| **Performance Efficiency** | Use resources efficiently | How do you use resources efficiently? |
| **Cost Optimization** | Avoid unnecessary costs | How do you avoid unnecessary costs? |
| **Sustainability** | Minimize environmental impact | How do you minimize environmental impact? |

### Azure Pillars

| Pillar | Focus |
|--------|-------|
| **Reliability** | Resilience and recovery |
| **Security** | Defense in depth |
| **Cost Optimization** | Maximize value |
| **Operational Excellence** | Simplify operations |
| **Performance Efficiency** | Scale effectively |

## Cloud Design Patterns

### Compute Patterns

| Pattern | Use Case | Services |
|---------|----------|----------|
| **Containers** | Microservices | ECS, EKS, AKS, GKE |
| **Serverless** | Event-driven | Lambda, Functions |
| **VMs** | Legacy, specific OS | EC2, VMs |

### Data Patterns

| Pattern | Use Case | Services |
|---------|----------|----------|
| **Managed DB** | Traditional workloads | RDS, Cloud SQL |
| **NoSQL** | Flexible schema | DynamoDB, Cosmos DB |
| **Data Warehouse** | Analytics | Redshift, BigQuery |
| **Cache** | Performance | ElastiCache, Memorystore |

### Integration Patterns

| Pattern | Use Case | Services |
|---------|----------|----------|
| **Message Queue** | Async communication | SQS, Service Bus |
| **Event Streaming** | Event-driven | Kafka, EventBridge |
| **API Gateway** | External APIs | API Gateway, APIM |

## Cloud Migration Strategies

### 6 R's

| Strategy | Description | Effort |
|----------|-------------|--------|
| **Rehost** | Lift and shift | Low |
| **Replatform** | Minor optimizations | Medium |
| **Repurchase** | Move to SaaS | Medium |
| **Refactor** | Re-architecture | High |
| **Retire** | Turn off | Low |
| **Retain** | Keep as-is | None |

## Cloud Cost Optimization

### Strategies

| Strategy | Savings | Effort |
|----------|---------|--------|
| Reserved Instances | 30-60% | Low |
| Spot Instances | 60-90% | Medium |
| Right-sizing | 20-40% | Low |
| Auto-scaling | 10-30% | Medium |
| Storage tiering | 30-50% | Low |

## Cloud Security

| Concern | Solution |
|---------|----------|
| **Identity** | IAM, SSO, MFA |
| **Network** | VPC, security groups |
| **Data** | Encryption at rest/transit |
| **Compliance** | CloudTrail, Config |
