---
name: arch-observability
description: Design observability architecture. Use when designing structured logging, metrics, distributed tracing or continuous profiling with OpenTelemetry, applying RED/USE and Golden Signals, defining SLOs and burn-rate alerts, or establishing telemetry standards.
---

# Observability Architecture

Systematic approach to making systems observable.

## DAP contribution

For a DAP invocation, read `framework/contribution-contract.md` from the outer
package root (the repository root in a source checkout). Keep standalone tasks
within their requested scope. Use `assets/review-template.md` and record signal definition and semantic-convention version, REQ/SLO mapping, cardinality/privacy/retention budgets, alert owner and runbook verification.
Return evidence-linked proposals and VER plans, not invented approvals or delivery proof.

## Workflow

```
1. Define Goals → What do we need to know?
2. Instrument → Add telemetry
3. Collect → Aggregate signals
4. Analyze → Understand behavior
5. Alert → Detect issues
6. Respond → Take action
```

## Step 1: Three Pillars

| Pillar | Purpose | Data |
|--------|---------|------|
| **Logs** | Discrete events | Application logs |
| **Metrics** | Aggregated measurements | Counters, gauges |
| **Traces** | Request flow | Distributed traces |
| **Profiles** | Code and resource hotspots | CPU, memory and runtime profiles; use when the signal is mature enough for the workload |

### Telemetry contract

Define service name, version, environment, deployment and ownership attributes;
pin the OpenTelemetry semantic-convention version; correlate logs, metrics and
traces with trace/span context; and set cardinality, retention, sampling and
privacy budgets. Never put secrets, raw tokens or unbounded user identifiers in
telemetry labels or attributes.

## Step 2: Logging Architecture

### Log Levels

| Level | When to Use |
|-------|-------------|
| **DEBUG** | Detailed diagnostic info |
| **INFO** | Normal operations |
| **WARN** | Unexpected but handled |
| **ERROR** | Failures requiring attention |
| **FATAL** | System cannot continue |

### Structured Logging

```json
{
  "timestamp": "2024-01-15T10:30:00Z",
  "level": "INFO",
  "service": "order-service",
  "traceId": "abc123",
  "message": "Order created",
  "orderId": "456",
  "customerId": "789"
}
```

### Log Aggregation

```
Services → Agent → Pipeline → Storage → Query
```

**Tools:**
- **Collection:** Fluentd, Filebeat, Fluent Bit
- **Pipeline:** Logstash, Vector
- **Storage:** Elasticsearch, Loki, CloudWatch
- **Query:** Kibana, Grafana, CloudWatch Insights

## Step 3: Metrics Architecture

### Metric Types

| Type | Description | Example |
|------|-------------|---------|
| **Counter** | Monotonically increasing | Request count |
| **Gauge** | Can go up/down | Temperature |
| **Histogram** | Distribution of values | Response time |
| **Summary** | Pre-calculated quantiles | p95 latency |

### RED Method

| Metric | Description |
|--------|-------------|
| **Rate** | Requests per second |
| **Errors** | Errors per second |
| **Duration** | Request latency |

### USE Method

| Metric | Description |
|--------|-------------|
| **Utilization** | % resource in use |
| **Saturation** | Queue depth |
| **Errors** | Error count |

### Metrics Collection

```
Services → Exporter → Scraper → Storage → Dashboard
```

**Tools:**
- **Export:** Prometheus client, StatsD
- **Scrape:** Prometheus, Datadog Agent
- **Storage:** Prometheus, InfluxDB, CloudWatch
- **Visualize:** Grafana, Datadog, CloudWatch

## Step 4: Distributed Tracing

### Trace Structure

```
Trace (abc123)
├── Span 1: API Gateway (100ms)
│   ├── Span 2: Auth Service (20ms)
│   └── Span 3: Order Service (80ms)
│       ├── Span 4: Database Query (30ms)
│       └── Span 5: Payment Service (40ms)
```

### Sampling Strategies

| Strategy | Description | Use Case |
|----------|-------------|----------|
| **Always** | Sample all | Debugging |
| **Never** | Sample none | High volume |
| **Probability** | Random % | General |
| **Rate Limit** | Max per second | Cost control |

### OpenTelemetry

Standard for traces, metrics, logs:

```python
from opentelemetry import trace

tracer = trace.get_tracer("order-service")

with tracer.start_as_current_span("process_order") as span:
    span.set_attribute("order.id", order_id)
    # Process order
```

Prefer a collector-based pipeline when routing, redaction, sampling or backend
fan-out is required. Treat OpenTelemetry profiles as an optional emerging signal,
not a replacement for the core logs/metrics/traces contract.

## Step 5: Alerting

### Alert Design

| Level | Response Time | Example |
|-------|---------------|---------|
| **Critical** | Immediate | Service down |
| **High** | < 1 hour | Error rate spike |
| **Medium** | < 4 hours | High latency |
| **Low** | Next day | Warning threshold |

### Alert Rules

```
IF error_budget_burn_rate breaches the service policy THEN page
IF user-facing latency SLO burn persists beyond the policy window THEN alert
IF saturation threatens the service's recovery target THEN alert
```

Thresholds are examples only. Derive them from user-facing SLIs, SLOs, error
budgets and recovery objectives; pair every page with a runbook and owner.

### On-Call Best Practices

- Runbooks for every alert
- Escalation policies
- Post-incident reviews
- Alert fatigue reduction

## Step 6: Dashboards

### Service Dashboard

```
┌─────────────────────────────────────────────┐
│  Service: order-service                     │
├─────────────────────────────────────────────┤
│  Requests    │  Errors      │  Latency     │
│  1.2k/s      │  0.1%        │  p95: 120ms  │
├──────────────┼──────────────┼──────────────┤
│  [Chart]     │  [Chart]     │  [Chart]     │
└─────────────────────────────────────────────┘
```

### Golden Signals

| Signal | What to Measure |
|--------|-----------------|
| **Latency** | Time to serve request |
| **Traffic** | Demand on system |
| **Errors** | Failure rate |
| **Saturation** | How full is service |

## Examples

- Design an OpenTelemetry rollout across a dozen services with trace propagation.
- Define RED-method dashboards and alert thresholds for a payment service.
- Cut log volume costs with sampling without losing incident forensics.

## Common Gotchas

- Alert on symptoms users feel (SLO burn), not on every internal metric - alert fatigue kills response.
- Logs without trace/correlation IDs make distributed debugging archaeology.
- Unbounded label cardinality (user IDs in metric labels) melts time-series databases.
- A dashboard with no SLO, owner or runbook is a report, not an operational control.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)
- `references/observability-deep-dive.md` — Observability Deep Dive
- `references/observability-patterns.md` — Observability Reference

Use the [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/specs/semconv/)
with a pinned version. Treat [OpenTelemetry profiles](https://opentelemetry.io/docs/concepts/signals/profiles/)
as an emerging optional signal whose maturity and backend support must be
verified for the workload.

## Related Skills

- **arch-resilience** - Failures observability must surface
- **arch-perf** - SLOs the dashboards track
- **arch-devops** - Deployment health and pipeline integration

## Output template

Use `assets/review-template.md`. Populate its scope and evidence fields for DAP work;
keep missing measurements and approvals explicit.
