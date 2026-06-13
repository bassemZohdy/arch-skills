# Observability Deep Dive

**Source:** Google SRE, OpenTelemetry, Distributed Tracing in Practice

## Three Pillars

| Pillar | Purpose | Data |
|--------|---------|------|
| **Logs** | Discrete events | Application logs |
| **Metrics** | Aggregated measurements | Counters, gauges |
| **Traces** | Request flow | Distributed traces |

## RED Method (Google SRE)

| Metric | Description | Measurement |
|--------|-------------|-------------|
| **Rate** | Requests per second | Counter |
| **Errors** | Errors per second | Counter |
| **Duration** | Request latency | Histogram |

## USE Method

| Metric | Description | Measurement |
|--------|-------------|-------------|
| **Utilization** | % resource in use | Gauge |
| **Saturation** | Queue depth | Gauge |
| **Errors** | Error count | Counter |

## Golden Signals (Google SRE)

| Signal | What to Measure | How to Measure |
|--------|-----------------|----------------|
| **Latency** | Time to serve request | p50, p95, p99 |
| **Traffic** | Demand on system | Requests/sec |
| **Errors** | Failure rate | Errors/sec |
| **Saturation** | How full is service | CPU, memory, disk |

## OpenTelemetry

### Instrumentation

```python
from opentelemetry import trace, metrics

tracer = trace.get_tracer("service")
meter = metrics.get_meter("service")

# Traces
with tracer.start_as_current_span("operation") as span:
    span.set_attribute("key", "value")
    # Process operation

# Metrics
counter = meter.create_counter("requests")
counter.add(1, {"method": "GET"})
```

### Sampling Strategies

| Strategy | Description | Use Case |
|----------|-------------|----------|
| **Always** | Sample all | Debugging |
| **Never** | Sample none | High volume |
| **Probability** | Random % | General |
| **Rate Limit** | Max per second | Cost control |

## Alerting Best Practices

### Alert Design

| Level | Response Time | Example |
|-------|---------------|---------|
| **Critical** | Immediate | Service down |
| **High** | < 1 hour | Error rate spike |
| **Medium** | < 4 hours | High latency |
| **Low** | Next day | Warning threshold |

### On-Call Best Practices

- Runbooks for every alert
- Escalation policies
- Post-incident reviews
- Alert fatigue reduction
