# Integration Patterns Reference

**Source:** Enterprise Integration Patterns (Hohpe & Woolf), microservices.io

## Synchronous Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Request/Reply** | Direct call and response | Real-time queries |
| **API Gateway** | Central entry point | External APIs |
| **Service Mesh** | Infrastructure-level communication | Microservices |
| **Façade** | Unified interface to subsystems | Legacy integration |
| **Remote Procedure Invocation** | Direct method calls | Simple integration |

## Asynchronous Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Message Queue** | Point-to-point messaging | Task distribution |
| **Pub/Sub** | Topic-based messaging | Event broadcasting |
| **Event Streaming** | Log ordered within a defined partition/key scope | Replay and stream processing |
| **Saga** | Local transactions with compensations; no global atomic rollback | Multi-service operations |
| **Message Channel** | Direct connection | Simple messaging |
| **Publish-Subscribe Channel** | One-to-many delivery | Broadcasting |
| **Datatype Channel** | Typed messages | Strong typing |
| **Invalid Message Channel** | Error handling | Dead letter queue |

## Mediation Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Content-Based Router** | Route by message content | Multi-consumer |
| **Message Translator** | Convert message format | Protocol bridging |
| **Message Filter** | Selectively process messages | Filtering |
| **Aggregator** | Combine multiple messages | Response aggregation |
| **Content Enricher** | Add missing information | Data enrichment |
| **Content Filter** | Remove unwanted information | Data filtering |
| **Splitter** | Break message into parts | Parallel processing |
| **Claim Check** | Store/retrieve large payloads | Payload management |

## Messaging Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Message Endpoint** | Application connection to channel | Integration |
| **Message Translator** | Format conversion | Heterogeneous systems |
| **Message Router** | Direct messages to handlers | Complex routing |
| **Message Filter** | Select messages | Selective processing |
| **Content-Based Router** | Route by content | Content-aware routing |

## Service Mesh

### Components

| Component | Description |
|-----------|-------------|
| **Data Plane** | Sidecar or ambient proxies handle communication, depending on the mesh |
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
| **AWS App Mesh** | Discontinued September 30, 2026; migration context only |
| **Cilium** | eBPF-based networking |

## Integration Security

| Concern | Solution |
|---------|----------|
| **Identity and access** | Workload mTLS, scoped OAuth access tokens; OIDC for user identity |
| **Authorization** | Enforce resource/tenant policy in the owning service and at the gateway |
| **Encryption** | TLS in transit, encryption at rest |
| **Rate Limiting** | Per-client, per-endpoint |
| **Input Validation** | Schema validation at gateway |
| **API Versioning** | Backward compatibility |

## Integration Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Unmanaged integration coupling** | Changes ripple through undocumented contracts | Establish ownership/contracts; add mediation only when it reduces measured coupling |
| **Integration Monolith** | Single integration point | Decompose |
| **Shared Database** | Tight coupling | Separate data |
| **Synchronous Everything** | Cascading failures | Use async |
| **No Schema Evolution** | Breaking changes | Version schemas |

## Product lifecycle

Before adopting a listed tool, verify its support lifecycle and target runtime.
[AWS App Mesh was discontinued on September 30, 2026](https://docs.aws.amazon.com/app-mesh/latest/userguide/what-is-app-mesh.html):
its console and resources are no longer accessible. Do not select it; treat any
remaining configuration as migration evidence and confirm the replacement mesh or
service-to-service networking option against the target runtime.
