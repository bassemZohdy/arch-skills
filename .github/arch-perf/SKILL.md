---
name: arch-perf
description: Guide performance engineering and capacity planning. Use when designing for performance, analyzing bottlenecks, planning capacity, defining SLAs/SLOs, designing caching strategies, or conducting load testing.
---

# Performance Engineering

Systematic approach to designing and validating performant systems.

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

## Performance Review Template

```markdown
## Performance Review: [System Name]

### Requirements
- Latency: [Target]
- Throughput: [Target]
- Availability: [Target]

### Current State
- Measured latency: [Value]
- Measured throughput: [Value]
- Bottlenecks: [List]

### Recommendations
1. [High impact improvement]
2. [Medium impact improvement]

### Performance Budget
| Metric | Budget | Current | Status |
|--------|--------|---------|--------|
```
