# Resilience Engineering Deep Dive

Derive timeouts, retry limits and queue sizes from the end-to-end deadline,
dependency latency and load tests. Use one retry owner and bounded full jitter;
retry only transient failures with safe operation semantics. An unknown write
outcome requires idempotency or reconciliation, not a blind retry. Agree blast
radius, abort conditions and recovery before a chaos experiment.

**Source:** Google SRE, Release It!, Netflix Hystrix (historical; the library has been in maintenance mode since 2018, so use its concepts rather than adopting it)

## Circuit Breaker Pattern

### States

```
CLOSED → (failures exceed threshold) → OPEN
  ↑                                      ↓
  (success)                    (timeout expires)
  ↑                                      ↓
  └────────── HALF-OPEN ←────────────────┘
```

### Configuration

| Setting | Illustrative starting point | Description |
|---------|-------------|-------------|
| Failure threshold | 5 failures / 60s | Trip after failures |
| Open duration | 30s | Time before half-open |
| Half-open calls | 3 | Calls to test recovery |
| Timeout | 5s | Call timeout |

## Bulkhead Pattern

### Implementation

```
┌─────────────────────────────────────┐
│           Service Pool              │
├─────────────┬─────────────┬─────────┤
│  Pool A     │  Pool B     │ Pool C  │
│  (10 conns) │  (10 conns) │(10 conns)│
│  Payment    │  Shipping   │ Notification│
└─────────────┴─────────────┴─────────┘
```

### Configuration

| Setting | Illustrative starting point | Description |
|---------|-------------|-------------|
| Max concurrent | 10-20 | Per dependency |
| Queue size | 5-10 | Waiting requests |
| Timeout | 5s | Queue wait limit |

## Retry Patterns

| Pattern | Formula | Use Case |
|---------|---------|----------|
| Fixed | delay = constant | Simple retry |
| Exponential | delay = base × 2^attempt | Load reduction |
| Exponential + Jitter | delay = uniform(0, min(cap, base × 2^attempt)) | Prevent thundering herd |

## Timeout Configuration

| Type | Illustrative starting point | Use Case |
|------|-------------|----------|
| Connection | 2-5s | Establish connection |
| Read | 5-30s | Wait for response |
| Total | 10-60s | End-to-end limit |

## Chaos Engineering

### Principles

1. **Build Hypothesis** - Define steady state
2. **Introduce Real-World Events** - Network latency, service failures
3. **Observe Deviations** - Monitor system behavior
4. **Fix Weaknesses** - Address issues found
5. **Automate** - Run experiments continuously

### Game Day Checklist

- [ ] Define steady state hypothesis
- [ ] Inject realistic failures
- [ ] Observe system behavior
- [ ] Verify recovery
- [ ] Document findings
