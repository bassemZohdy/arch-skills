# Performance Patterns Reference

## SLA/SLO/Error Budget (Google SRE)

| Term | Definition | Example |
|------|------------|---------|
| **SLA** | Contractual commitment | 99.9% uptime |
| **SLO** | Internal target | 99.95% uptime |
| **SLI** | Measured metric | Success rate, latency |
| **Error Budget** | Allowed failures | 1 minus the adopted SLO |

### Error Budget Policy

For a time-based availability SLI over exactly 30 days, 0.01% is 4.32 minutes
and 0.05% is 21.6 minutes. A request-based budget is instead a fraction of eligible
requests; it cannot be converted directly to downtime. The policy bands below are
illustrative and need an accountable owner and explicit emergency exceptions.

| Budget Remaining | Action |
|------------------|--------|
| > 50% | Normal development |
| 25-50% | Caution, extra testing |
| < 25% | Feature freeze, reliability focus |
| 0% | Restrict feature releases; permit recovery and authorized emergency/security changes |

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
| **Write-Through** | Coordinate cache and DB writes | Define failure, invalidation and reader consistency semantics |
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

Example budgets; replace them with values tied to a user journey, device/network
class and business SLO. The web thresholds are the published
[Core Web Vitals](https://web.dev/articles/vitals) "good" levels.

| Metric | Example budget | Tool |
|--------|----------------|------|
| **Largest Contentful Paint** | <= 2.5s at the 75th percentile | Field measurement; Lighthouse for lab checks |
| **Interaction to Next Paint** | <= 200ms at the 75th percentile | Field measurement |
| **Cumulative Layout Shift** | <= 0.1 at the 75th percentile | Field measurement |
| **First Contentful Paint** | <= 1.8s | Lighthouse |
| **API Response** | < 200ms p95 | APM |

Use workload-specific latency/load targets and representative samples. For web responsiveness, use [INP](https://web.dev/articles/inp); [TTI was removed from Lighthouse 10](https://web.dev/articles/tti).
