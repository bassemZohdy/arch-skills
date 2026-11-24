# Resilience Patterns Reference

Derive timeouts, retry limits and queue sizes from the end-to-end deadline,
dependency latency and load tests. Use one retry owner and bounded full jitter;
retry only transient failures with safe operation semantics. An unknown write
outcome requires idempotency or reconciliation, not a blind retry. Agree blast
radius, abort conditions and recovery before a chaos experiment.

## Circuit Breaker

| Setting | Illustrative starting point | Description |
|---------|-------------|-------------|
| Failure threshold | 5 failures / 60s | Trip after failures |
| Open duration | 30s | Time before half-open |
| Half-open calls | 3 | Calls to test recovery |

## Retry

| Strategy | Formula | Use Case |
|----------|---------|----------|
| Fixed | delay = constant | Simple retry |
| Exponential | delay = base × 2^attempt | Load reduction |
| Exponential + Jitter | delay = uniform(0, min(cap, base × 2^attempt)) | Prevent thundering herd |

## Bulkhead

| Setting | Illustrative starting point | Description |
|---------|-------------|-------------|
| Max concurrent | 10-20 | Per dependency |
| Queue size | 5-10 | Waiting requests |
| Timeout | 5s | Queue wait limit |

## Timeout

| Type | Illustrative starting point | Use Case |
|------|-------------|----------|
| Connection | 2-5s | Establish connection |
| Read | 5-30s | Wait for response |
| Total | 10-60s | End-to-end limit |
