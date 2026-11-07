# Microservices Deep Dive

Extended patterns, sizing heuristics, and operational guidance.

## Service Decomposition Heuristics

### When to Extract a Service

| Heuristic | Threshold |
|-----------|-----------|
| Team owns multiple bounded contexts | Assess ownership and change coupling; context count alone does not justify extraction |
| Module changes independently | Candidate for extraction |
| Module has different scaling needs | Candidate for extraction |
| Module has different security/regulatory requirements | Candidate for extraction |
| Two modules never change together | They can be separate services |
| Two modules always change together | Keep them together |

### When NOT to Extract

| Anti-Pattern | Why It Fails |
|--------------|--------------|
| **Nano Services** | More services than developers; overhead dominates |
| **Entity Services** | CRUD wrappers around single tables — no business logic |
| **Tech Services** | "The Redis service", "The Email service" — utility, not business |
| **Sync Chain** | A→B→C→D synchronous calls; latency multiplies, failures cascade |

### Sizing Signals

Size follows business capability, cohesion and team ownership, not code or
endpoint counts. Treat the signals below as prompts for review, not limits.

| Signal | Healthy indication |
|--------|--------------------|
| **Ownership** | One team can own, understand and operate the service end to end |
| **Cohesion** | Most changes for one business capability touch only this service |
| **Data** | The service owns its data; other services do not read its tables |
| **Release cadence** | Deployable independently on the owning team's schedule |
| **Build and test time** | Short enough for the team's feedback loop; measure trend rather than a fixed limit |

## Communication Patterns Deep Dive

### Synchronous: When and When Not

| Use Sync When | Use Async When |
|---------------|----------------|
| Caller needs immediate response | Caller can continue without response |
| Operation is fast (<100ms) | Operation takes seconds or minutes |
| Result is required to continue | Result is informative/fire-and-forget |
| Caller must observe completion before proceeding | Completion can be tracked through a durable status/event contract |
| Single service involved | Multiple services must react |

Neither synchronous calls nor asynchronous delivery alone guarantee exactly-once
business effects. A timeout can leave a completed write unobserved. Define stable
operation IDs, atomic state changes, deduplication and reconciliation before retrying.

### Async Reliability Patterns

#### Outbox Pattern

```
Service → DB Transaction (INSERT business_data + INSERT outbox_message) → Outbox Poller → Message Broker
```

Prevents dual-write problem: message published but DB transaction rolled back.

#### Idempotent Consumer

```
Consumer receives event → Transaction: claim unique (consumer, event ID) + apply business update → Commit → Acknowledge
```

Enforce the claim and business update in one atomic transaction; separate
check-then-write operations race under concurrent delivery. External effects need
their own idempotency keys or reconciliation. Retain deduplication records for the
supported retry, late-arrival and replay horizon; intentional replay after expiry
must not silently repeat business effects.

#### Ordering Guarantees

| Need | Solution |
|------|----------|
| Global order | Single partition — don't do this at scale |
| Per-entity order | Partition by entity ID (order_id, user_id) |
| Causal order | Carry dependency metadata and enforce delivery/application order; timestamps alone do not enforce it |
| No ordering needed | Any partition strategy |

## Data Ownership Patterns

### Database per Service — Migration Strategies

| Pattern | Description | Risk |
|---------|-------------|------|
| **Separate schema** | Same DB, different schemas per service | Low isolation; easy to cheat |
| **Separate database** | Separate logical databases, optionally on shared infrastructure | Enforce access ownership; physical fault isolation depends on placement |
| **Separate technology** | Service A uses PostgreSQL, B uses DynamoDB | Polyglot persistence; DBA skills spread thin |

### Data Duplication: When It's OK

Intentional duplication IS acceptable when:
- Data is owned by one service (source of truth)
- Other services cache a read-only projection
- Cache invalidation strategy exists (CDC, TTL, event-driven)
- Consumers treat cached data as eventually consistent

### Shared Data Anti-Patterns

| Anti-Pattern | Fix |
|--------------|-----|
| Multiple services writing to same table | Assign table ownership to one service; others use API |
| Direct DB access across services | Expose API; enforce at network/firewall level |
| JOINs across service databases | Create a read-projection service or use CQRS |
| Foreign keys to another service's table | Reference by ID only; no FK constraint |

## Testing Microservices

### Test Pyramid for Microservices

| Level | Scope | Tool |
|-------|-------|------|
| **Unit** | Single service internals | JUnit, pytest |
| **Integration** | Service + real DB/messaging | Testcontainers |
| **Contract** | Service boundaries | Pact, Spring Cloud Contract |
| **Component** | Service + stubbed dependencies | WireMock, Mountebank |
| **E2E** | Critical business flows only | Playwright, Cypress |

### Contract Testing Workflow

1. Consumer defines expectations (Pact)  
2. Provider verifies against expectations  
3. CI gates merge if contracts pass  
4. Provider publishes verification results to Pact Broker  
5. Consumer checks broker before deploy (`can-i-deploy`)

## Observability in Microservices

| Concern | Pattern |
|---------|---------|
| **Distributed tracing** | Propagate trace ID via headers (W3C Trace Context) |
| **Log correlation** | Include trace ID + service name in every log line |
| **Health checks** | Liveness (am I alive?) + Readiness (can I serve?) |
| **Service mesh telemetry** | Istio/Linkerd auto-instrument HTTP/gRPC |

## Organizational Patterns

### Team Topologies for Microservices

| Topology | Description |
|----------|-------------|
| **Stream-aligned** | Team owns full vertical slice: UI → API → DB |
| **Platform** | Provides internal platform for stream teams |
| **Enabling** | Coaches stream teams; temporary |
| **Complicated Subsystem** | Specialized team for complex component |

### Conway's Law Alignment

- If two teams own services that constantly coordinate → merge teams or merge services
- If one team owns services that rarely coordinate, assess ownership and cognitive
  load before changing the organization; lack of coordination is not a split mandate
- Organizational coupling = architectural coupling (Conway's Law works both ways)

## Migration from Monolith

### Strangler Fig Applied to Microservices

1. Identify a bounded context in the monolith
2. Add a facade/router that diverts specific routes to new service
3. Extract data with a named authoritative writer, restartable backfill and CDC/outbox
   or another verified replication boundary; reconcile before switching readers/writers
4. Iterate: one bounded context at a time
5. Decommission monolith when all contexts migrated

### Modular Monolith as Alternative

Before extracting microservices, try:
1. Enforce module boundaries in the monolith (ArchUnit/dependency-cruiser)
2. Separate database schemas within the same DB
3. Use async messaging between modules
4. Only extract when team scale or independent deployment forces it

Compare a modular monolith against the same requirements and measured operating
costs. Do not assume a fixed benefit or cost percentage for either topology.
