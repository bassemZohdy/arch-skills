# Microservices Deep Dive

Extended patterns, sizing heuristics, and operational guidance.

## Service Decomposition Heuristics

### When to Extract a Service

| Heuristic | Threshold |
|-----------|-----------|
| Team owns ≥3 bounded contexts | Split by context |
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

### Sizing Rules of Thumb

| Metric | Guideline |
|--------|-----------|
| **Team size** | 4-8 people per service |
| **Code size** | 5K-50K LOC |
| **Endpoints** | 5-25 REST endpoints |
| **Database tables** | 5-25 tables owned |
| **Release cadence** | Independent (daily to weekly) |
| **Build time** | < 10 minutes |

## Communication Patterns Deep Dive

### Synchronous: When and When Not

| Use Sync When | Use Async When |
|---------------|----------------|
| Caller needs immediate response | Caller can continue without response |
| Operation is fast (<100ms) | Operation takes seconds or minutes |
| Result is required to continue | Result is informative/fire-and-forget |
| Exactly-once semantics needed | At-least-once is acceptable |
| Single service involved | Multiple services must react |

### Async Reliability Patterns

#### Outbox Pattern

```
Service → DB Transaction (INSERT business_data + INSERT outbox_message) → Outbox Poller → Message Broker
```

Prevents dual-write problem: message published but DB transaction rolled back.

#### Idempotent Consumer

```
Consumer receives event → Check processed_events table → If new: process + mark processed
```

Use event ID + consumer name as dedup key. TTL on dedup table = max redelivery window.

#### Ordering Guarantees

| Need | Solution |
|------|----------|
| Global order | Single partition — don't do this at scale |
| Per-entity order | Partition by entity ID (order_id, user_id) |
| Causal order | Vector clocks or Lamport timestamps |
| No ordering needed | Any partition strategy |

## Data Ownership Patterns

### Database per Service — Migration Strategies

| Pattern | Description | Risk |
|---------|-------------|------|
| **Separate schema** | Same DB, different schemas per service | Low isolation; easy to cheat |
| **Separate database** | Different DB instances | True isolation; operational overhead |
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
- If one team owns services that never coordinate → split the team
- Organizational coupling = architectural coupling (Conway's Law works both ways)

## Migration from Monolith

### Strangler Fig Applied to Microservices

1. Identify a bounded context in the monolith
2. Add a facade/router that diverts specific routes to new service
3. Extract data: dual-write + backfill → cut over reads → remove monolith code
4. Iterate: one bounded context at a time
5. Decommission monolith when all contexts migrated

### Modular Monolith as Alternative

Before extracting microservices, try:
1. Enforce module boundaries in the monolith (ArchUnit/dependency-cruiser)
2. Separate database schemas within the same DB
3. Use async messaging between modules
4. Only extract when team scale or independent deployment forces it

A modular monolith gives 80% of microservices benefits at 20% of the operational cost.
