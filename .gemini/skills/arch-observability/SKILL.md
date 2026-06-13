---
name: arch-observability
description: Guide observability architecture. Use when designing logging strategies, implementing distributed tracing, setting up monitoring dashboards, or establishing observability standards.
---

# Observability Architecture

Systematic approach to making systems observable.

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
IF error_rate > 5% FOR 5 minutes THEN alert:high
IF latency_p95 > 500ms FOR 10 minutes THEN alert:medium
IF disk_usage > 90% THEN alert:high
```

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

## Observability Review Template

```markdown
## Observability Review: [System]

### Current State
| Pillar | Coverage | Quality |
|--------|----------|---------|

### Gaps
- [Gap 1]
- [Gap 2]

### Recommendations
1. [High priority]
2. [Medium priority]

### Tool Stack
| Category | Tool |
|----------|------|
| Logs | [Tool] |
| Metrics | [Tool] |
| Traces | [Tool] |
| Alerts | [Tool] |
```
