# Resilience Patterns Reference

## Circuit Breaker

| Setting | Recommended | Description |
|---------|-------------|-------------|
| Failure threshold | 5 failures / 60s | Trip after failures |
| Open duration | 30s | Time before half-open |
| Half-open calls | 3 | Calls to test recovery |

## Retry

| Strategy | Formula | Use Case |
|----------|---------|----------|
| Fixed | delay = constant | Simple retry |
| Exponential | delay = base × 2^attempt | Load reduction |
| Exponential + Jitter | delay = base × 2^attempt + random | Prevent thundering herd |

## Bulkhead

| Setting | Recommended | Description |
|---------|-------------|-------------|
| Max concurrent | 10-20 | Per dependency |
| Queue size | 5-10 | Waiting requests |
| Timeout | 5s | Queue wait limit |

## Timeout

| Type | Recommended | Use Case |
|------|-------------|----------|
| Connection | 2-5s | Establish connection |
| Read | 5-30s | Wait for response |
| Total | 10-60s | End-to-end limit |
