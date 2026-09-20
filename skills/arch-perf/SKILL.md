---
name: arch-perf
description: Engineer performance and plan capacity. Use when designing for performance, analyzing bottlenecks, planning capacity, defining SLAs/SLOs, designing caching strategies, or conducting load testing.
---

# Performance Engineering

Systematic approach to designing and validating performant systems.

## DAP contribution

For a DAP invocation, read `framework/contribution-contract.md` from the outer
package root (the repository root in a source checkout). Keep standalone tasks
within their requested scope. Use `assets/review-template.md` and record stimulus/environment/response/threshold scenarios, workload and dataset revisions, measured percentiles, uncertainty and benchmark owner.
Return evidence-linked proposals and VER plans, not invented approvals or delivery proof.

## Workflow

```
1. Define Requirements → What performance do we need?
2. Profile Baseline → Where are we now?
3. Identify Bottlenecks → What's limiting performance?
4. Design Solutions → How to improve?
5. Validate → Does it meet requirements?
6. Monitor → Continuously track performance
```

## Step 1: Define Performance Requirements

| Metric | Description | Example |
|--------|-------------|---------|
| **Latency** | Time for single request | p95 < 200ms |
| **Throughput** | Requests per time unit | 1000 req/s |
| **Concurrency** | Simultaneous users | 10,000 users |
| **Availability** | Uptime percentage | 99.9% |
| **Scalability** | Handle growth | 10x in 6 months |

### SLA/SLO/Error Budget

| Term | Definition | Example |
|------|------------|---------|
| **SLA** | Contractual commitment | 99.9% uptime |
| **SLO** | Internal target | 99.95% uptime |
| **Error Budget** | Allowed failures | 0.05% = 22 min/month |

## Step 2: Performance Patterns

### Caching

| Layer | Tool | Use Case |
|-------|------|----------|
| **Browser** | Cache-Control headers | Static assets |
| **CDN** | CloudFront, Cloudflare | Global static content |
| **Application** | Redis, Memcached | Session, queries |
| **Database** | Query cache, materialized views | Frequent queries |

### Async Processing

| Pattern | Use Case | Example |
|---------|----------|---------|
| **Message Queue** | Decouple producers/consumers | Order processing |
| **Event Streaming** | High-volume events | Clickstream |
| **Background Jobs** | Long-running tasks | Email sending |
| **CQRS** | Separate read/write | Reporting |

### Connection Management

- Connection pooling (database, HTTP)
- Keep-alive connections
- Connection limits and timeouts
- Circuit breakers for downstream

### Database Optimization

- Indexing strategy
- Query optimization
- Read replicas
- Sharding for scale
- Connection pooling

## Step 3: Capacity Planning

### Sizing Formula

```
Required Capacity = Peak Load × (1 + Safety Margin)
Safety Margin = 20-50% depending on criticality
```

Replace the illustrative margin with a workload model that includes peak shape,
arrival rate, service time, concurrency, saturation, dependency limits, failure
headroom and cost. Validate it with production-like load and tail-latency data.

### Scaling Strategies

| Strategy | When | Pros | Cons |
|----------|------|------|------|
| **Vertical** | Single resource bound | Simple | Limited, downtime |
| **Horizontal** | Stateless services | Linear scale | Complexity |
| **Auto-scaling** | Variable load | Cost-efficient | Cold start latency |

## Step 4: Load Testing

### Test Types

| Type | Purpose | Duration |
|------|---------|----------|
| **Load** | Expected traffic | 30-60 min |
| **Stress** | Beyond capacity | Until failure |
| **Spike** | Sudden bursts | Minutes |
| **Soak** | Sustained load | Hours/days |

### Metrics to Capture

- Response time (p50, p95, p99)
- Throughput (req/s)
- Error rate
- CPU/Memory utilization
- Database connections
- Queue depth

### Tools

- **k6** — Developer-centric load testing
- **JMeter** — Enterprise load testing
- **Locust** — Python-based load testing
- **Gatling** — Scala-based performance testing

## Step 5: Performance Budgets

| Resource | Budget | Measurement |
|----------|--------|-------------|
| **Page Load** | < 3s | Lighthouse |
| **API Response** | < 200ms p95 | APM |
| **Database Query** | < 50ms | Query analyzer |
| **Bundle Size** | < 200KB | Webpack |

Budgets are hypotheses until tied to a user journey, device/network class and
business SLO. Keep p50, p95 and p99 visible and record the measurement method.

## Examples

- Define SLOs and an error budget for a checkout API, then design the caching strategy to meet them.
- Plan capacity for a 10x traffic spike during a product launch.
- Diagnose p99 latency spikes caused by connection pool exhaustion.

## Common Gotchas

- Averages hide tail latency; always look at p95/p99, not means.
- Caching without an invalidation strategy trades a latency bug for a correctness bug.
- Load tests against staging with production-unlike data give false confidence.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)
- `references/performance-deep-dive.md` — Performance Engineering Deep Dive
- `references/performance-patterns.md` — Performance Patterns Reference

## Related Skills

- **arch-resilience** - Timeouts and circuit breakers that bound latency
- **arch-observability** - Measuring latency, throughput, and saturation
- **arch-cost** - Trading performance headroom against spend

## Output template

Use `assets/review-template.md`. Populate its scope and evidence fields for DAP work;
keep missing measurements and approvals explicit.
