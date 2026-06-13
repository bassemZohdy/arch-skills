# Resilience Engineering Deep Dive

**Source:** Netflix Hystrix, Google SRE, Release It!

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

| Setting | Recommended | Description |
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

| Setting | Recommended | Description |
|---------|-------------|-------------|
| Max concurrent | 10-20 | Per dependency |
| Queue size | 5-10 | Waiting requests |
| Timeout | 5s | Queue wait limit |

## Retry Patterns

| Pattern | Formula | Use Case |
|---------|---------|----------|
| Fixed | delay = constant | Simple retry |
| Exponential | delay = base × 2^attempt | Load reduction |
| Exponential + Jitter | delay = base × 2^attempt + random | Prevent thundering herd |

## Timeout Configuration

| Type | Recommended | Use Case |
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
