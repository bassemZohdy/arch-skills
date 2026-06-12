# Integration Patterns Reference

## Synchronous Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Request/Reply** | Direct call and response | Real-time queries |
| **API Gateway** | Central entry point | External APIs |
| **Service Mesh** | Infrastructure-level communication | Microservices |
| **Façade** | Unified interface to subsystems | Legacy integration |

## Asynchronous Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Message Queue** | Point-to-point messaging | Task distribution |
| **Pub/Sub** | Topic-based messaging | Event broadcasting |
| **Event Streaming** | Ordered event log | Event sourcing |
| **Saga** | Distributed transaction | Multi-service operations |

## Mediation Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Content-Based Router** | Route by message content | Multi-consumer |
| **Message Translator** | Convert message format | Protocol bridging |
| **Message Filter** | Selectively process messages | Filtering |
| **Aggregator** | Combine multiple messages | Response aggregation |

## Integration Security

| Concern | Solution |
|---------|----------|
| Authentication | mTLS, OAuth 2.0, API keys |
| Authorization | RBAC, ABAC at gateway |
| Encryption | TLS in transit, encryption at rest |
| Rate Limiting | Per-client, per-endpoint |
| Input Validation | Schema validation at gateway |
