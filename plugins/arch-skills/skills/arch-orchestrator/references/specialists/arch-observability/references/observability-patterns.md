# Observability Reference

## Three Pillars

| Pillar | Data | Tools |
|--------|------|-------|
| Logs | Discrete events | ELK, Loki, CloudWatch |
| Metrics | Aggregations | Prometheus, Datadog |
| Traces | Request flow | Jaeger, X-Ray, Zipkin |

## Golden Signals

| Signal | What | How |
|--------|------|-----|
| Latency | Time to serve | p50, p95, p99 |
| Traffic | Demand | Requests/sec |
| Errors | Failure rate | Errors/sec |
| Saturation | Resource usage | CPU, memory, disk |

## RED Method

- **Rate** — Requests per second
- **Errors** — Errors per second
- **Duration** — Request latency

## USE Method

- **Utilization** — % resource in use
- **Saturation** — Queue depth
- **Errors** — Error count

## OpenTelemetry

Standard for telemetry collection:

```python
from opentelemetry import trace, metrics

tracer = trace.get_tracer("service")
meter = metrics.get_meter("service")

# Traces
with tracer.start_as_current_span("operation") as span:
    span.set_attribute("key", "value")

# Metrics
counter = meter.create_counter("requests")
counter.add(1, {"method": "GET"})
```
