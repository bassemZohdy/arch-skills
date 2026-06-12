# Performance Patterns Reference

## Caching Patterns

| Layer | Tool | TTL | Use Case |
|-------|------|-----|----------|
| **Browser** | Cache-Control | Configurable | Static assets |
| **CDN** | CloudFront | Minutes-hours | Global content |
| **Application** | Redis | Seconds-minutes | Sessions, queries |
| **Database** | Query cache | Varies | Frequent queries |

## Async Processing

| Pattern | Tool | Use Case |
|---------|------|----------|
| **Queue** | SQS, RabbitMQ | Task distribution |
| **Stream** | Kafka, Kinesis | Event processing |
| **Pub/Sub** | SNS, EventBridge | Notifications |
| **Scheduler** | Cron, EventBridge | Periodic tasks |

## Database Optimization

| Technique | Impact | Effort |
|-----------|--------|--------|
| **Indexing** | High | Low |
| **Query optimization** | High | Medium |
| **Read replicas** | High | Medium |
| **Connection pooling** | Medium | Low |
| **Caching** | High | Medium |
| **Sharding** | High | High |

## Scaling Patterns

| Pattern | Trigger | Action |
|---------|---------|--------|
| **Horizontal** | Load increase | Add instances |
| **Vertical** | Resource limit | Upgrade instance |
| **Auto-scaling** | Metric threshold | Dynamic adjustment |
