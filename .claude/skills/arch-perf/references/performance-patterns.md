# Performance Patterns Reference

## SLA/SLO/Error Budget (Google SRE)

| Term | Definition | Example |
|------|------------|---------|
| **SLA** | Contractual commitment | 99.9% uptime |
| **SLO** | Internal target | 99.95% uptime |
| **SLI** | Measured metric | Success rate, latency |
| **Error Budget** | Allowed failures | 0.05% = 22 min/month |

### Error Budget Policy

| Budget Remaining | Action |
|------------------|--------|
| > 50% | Normal development |
| 25-50% | Caution, extra testing |
| < 25% | Feature freeze, reliability focus |
| 0% | Stop all changes, fix reliability |

## Caching Patterns

| Layer | Tool | TTL | Use Case |
|-------|------|-----|----------|
| **Browser** | Cache-Control | Configurable | Static assets |
| **CDN** | CloudFront | Minutes-hours | Global content |
| **Application** | Redis | Seconds-minutes | Sessions, queries |
| **Database** | Query cache | Varies | Frequent queries |

### Cache Strategies

| Strategy | Description | Use Case |
|----------|-------------|----------|
| **Cache-Aside** | App manages cache | General purpose |
| **Write-Through** | Write to cache and DB | Strong consistency |
| **Write-Behind** | Write to cache, async to DB | High write throughput |
| **Read-Through** | Cache loads on miss | Read-heavy workloads |

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

## Load Testing Best Practices

| Test Type | Purpose | Duration |
|-----------|---------|----------|
| **Load** | Expected traffic | 30-60 min |
| **Stress** | Beyond capacity | Until failure |
| **Spike** | Sudden bursts | Minutes |
| **Soak** | Sustained load | Hours/days |

## Performance Budgets

| Metric | Budget | Tool |
|--------|--------|------|
| **Page Load** | < 3s | Lighthouse |
| **API Response** | < 200ms p95 | APM |
| **First Contentful Paint** | < 1.8s | Lighthouse |
| **Time to Interactive** | < 3.8s | Lighthouse |
