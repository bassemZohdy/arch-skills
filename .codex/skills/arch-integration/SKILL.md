---
name: arch-integration
description: Guide system integration architecture. Use when designing service mesh, API gateway patterns, ESB integration, system-to-system communication, or establishing integration standards.
---

# Integration Architecture

Systematic approach to designing system integrations.

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

### synchronous Patterns

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

## Step 5: Integration Security

| Concern | Solution |
|---------|----------|
| **Authentication** | mTLS, OAuth 2.0, API keys |
| **Authorization** | RBAC, ABAC at gateway |
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

## Integration Review Template

```markdown
## Integration Review: [System]

### Systems Integrated
| System | Pattern | Protocol | Status |
|--------|---------|----------|--------|

### Integration Patterns
| Pattern | Use Case | Implementation |
|---------|----------|----------------|

### Contracts
| System | Specification | Version | Status |
|--------|--------------|---------|--------|

### Security
| Concern | Implementation | Verified |
|---------|---------------|----------|

### Recommendations
1. [Improvement]
```
