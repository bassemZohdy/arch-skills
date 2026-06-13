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
| **Event Streaming** | Ordered event log | Event sourcing |
| **Saga** | Distributed transaction | Multi-service operations |
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
| **Data Plane** | Sidecar proxies handle communication |
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
| **AWS App Mesh** | AWS-managed mesh |
| **Cilium** | eBPF-based networking |

## Integration Security

| Concern | Solution |
|---------|----------|
| **Authentication** | mTLS, OAuth 2.0, API keys |
| **Authorization** | RBAC, ABAC at gateway |
| **Encryption** | TLS in transit, encryption at rest |
| **Rate Limiting** | Per-client, per-endpoint |
| **Input Validation** | Schema validation at gateway |
| **API Versioning** | Backward compatibility |

## Integration Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Point-to-Point** | Tangled dependencies | Use middleware |
| **Integration Monolith** | Single integration point | Decompose |
| **Shared Database** | Tight coupling | Separate data |
| **Synchronous Everything** | Cascading failures | Use async |
| **No Schema Evolution** | Breaking changes | Version schemas |
