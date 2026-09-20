---
name: arch-integration
description: Design system integration architecture. Use when designing service mesh, API gateway patterns, ESB integration, system-to-system communication, or establishing integration standards.
---

# Integration Architecture

Systematic approach to designing system integrations.

## DAP contribution

For a DAP invocation, read `framework/contribution-contract.md` from the outer
package root (the repository root in a source checkout). Keep standalone tasks
within their requested scope. Use `assets/review-template.md` and record system/contract revisions, producer/consumer ownership, data authority, failure/ordering semantics and cross-team review.
Return evidence-linked proposals and VER plans, not invented approvals or delivery proof.

For DAP work, populate its scope and evidence fields; keep missing measurements and approvals explicit.

## Workflow

```
1. Identify Systems → What needs to connect?
2. Choose Pattern → Sync vs async, direct vs mediated
3. Design Contracts → API specifications, schemas
4. Implement Integration → Gateways, bridges, adapters
5. Monitor → Track flow health, latency
6. Govern → Versioning, deprecation, standards
```

## Step 1: Integration Patterns

### Synchronous Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Request/Reply** | Direct call and response | Real-time queries |
| **API Gateway** | Central entry point | External APIs |
| **Service Mesh** | Infrastructure-level communication | Microservices |
| **Façade** | Unified interface to subsystems | Legacy integration |

### Asynchronous Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Message Queue** | Point-to-point messaging | Task distribution |
| **Pub/Sub** | Topic-based messaging | Event broadcasting |
| **Event Streaming** | Ordered event log | Event sourcing |
| **Saga** | Distributed transaction | Multi-service operations |

### Mediation Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Content-Based Router** | Route by message content | Multi-consumer |
| **Message Translator** | Convert message format | Protocol bridging |
| **Message Filter** | Selectively process messages | Filtering |
| **Aggregator** | Combine multiple messages | Response aggregation |

## Step 2: API Gateway

### Responsibilities

| Responsibility | Description |
|----------------|-------------|
| **Routing** | Direct requests to services |
| **Authentication** | Verify identity |
| **Rate Limiting** | Control request volume |
| **Load Balancing** | Distribute traffic |
| **Caching** | Reduce latency |
| **Logging** | Track requests |

### Gateway Patterns

| Pattern | Description |
|---------|-------------|
| **Single Gateway** | One entry point for all |
| **Gateway per Domain** | Separate gateways per bounded context |
| **Backend for Frontend** | Gateway per client type |

## Step 3: Service Mesh

### Components

| Component | Description |
|-----------|-------------|
| **Data Plane** | Proxies handle traffic; placement can be sidecar or shared/ambient |
| **Control Plane** | Manages proxy configuration |

### Service Mesh Features

| Feature | Description |
|---------|-------------|
| **Traffic Management** | Routing, load balancing, retries |
| **Security** | mTLS, authorization |
| **Observability** | Metrics, tracing, logging |
| **Resilience** | Circuit breaking, timeouts |

### Tools

| Tool | Description |
|------|-------------|
| **Istio** | Full-featured service mesh |
| **Linkerd** | Lightweight service mesh |
| **Consul Connect** | HashiCorp service mesh |
| **AWS App Mesh** | Existing workloads only: support ends September 30, 2026; plan migration |

## Step 4: Integration Contracts

### API Specification

- **OpenAPI/Swagger** for REST
- **AsyncAPI** for event-driven
- **gRPC Proto** for gRPC

### Schema Management

| Strategy | Description |
|----------|-------------|
| **Schema Registry** | Central schema storage |
| **Schema Evolution** | Backward/forward compatibility |
| **Contract Testing** | Verify schema compliance |

For every integration, document ownership, idempotency, retry and timeout
semantics, ordering, replay or deduplication behavior, and the path for poison
messages or partial failure. Put translation at a boundary rather than leaking a
partner's schema into the domain model.

## Step 5: Integration Security

| Concern | Solution |
|---------|----------|
| **Identity and access** | Workload mTLS, scoped OAuth access tokens; OIDC for user identity |
| **Authorization** | Enforce resource/tenant policy in the owning service and at the gateway |
| **Encryption** | TLS in transit, encryption at rest |
| **Rate Limiting** | Per-client, per-endpoint |
| **Input Validation** | Schema validation at gateway |

## Step 6: Integration Monitoring

| Metric | Description |
|--------|-------------|
| **Latency** | Request/response time |
| **Throughput** | Messages per second |
| **Error Rate** | Failed integrations |
| **Availability** | Uptime of integration points |

## Examples

- Design an API gateway strategy with a BFF per client type.
- Evaluate whether a service mesh is justified for a 12-service platform.
- Bridge a legacy SOAP system into an event-driven platform with a translator.

## Common Gotchas

- Select a mesh from workload identity, traffic-policy and operational needs; no universal service-count threshold justifies it.
- Point-to-point integrations grow quadratically; mediate once pairs exceed a handful.
- Schema changes without a registry and compatibility rules break consumers silently.
- A gateway or mesh cannot make an unsafe retry safe; preserve operation semantics at the contract boundary.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)
- `references/integration-patterns.md` — Integration Patterns Reference

## Cross-skill handoff

Consume system owners, data authority and trust boundaries before drawing connections.
Give arch-api synchronous contracts and arch-event asynchronous contracts, including
deadline, retry owner, idempotency, ordering and schema compatibility. Reconcile
gateway, client and mesh retries with arch-resilience; enforce resource authorization in
the owning service as well as at the edge.

## Related Skills

- **arch-api** - Contract design for the integrated surfaces
- **arch-event** - Async messaging patterns
- **arch-microservices** - Service-to-service communication
