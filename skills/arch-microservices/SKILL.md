---
name: arch-microservices
description: Design microservices architecture. Use when decomposing monoliths, designing service boundaries, implementing service communication, or establishing microservices patterns.
---

# Microservices Architecture

Systematic approach to designing microservices systems.

## Workflow

```
1. Define Bounded Contexts → Where to draw boundaries?
2. Design Services → What each service does?
3. Choose Communication → Sync vs async?
4. Implement Patterns → API gateway, service discovery
5. Ensure Resilience → Circuit breakers, retries
6. Monitor → Distributed tracing, logging
```

## Step 1: Service Decomposition

### Decomposition Strategies

| Strategy | Description | Use Case |
|----------|-------------|----------|
| **By Business Capability** | Align with business functions | Standard approach |
| **By Subdomain** | DDD bounded contexts | Complex domains |
| **By Data Ownership** | Separate data per service | Data-intensive |
| **By Team** | Conway's Law alignment | Large organizations |

### Service Size Guidelines

| Guideline | Recommendation |
|-----------|----------------|
| **Team Size** | 2-pizza team (5-8 people) |
| **Code Size** | Small enough to understand quickly |
| **Deployment** | Independent deployment |
| **Database** | Database per service |

### Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Distributed Monolith** | Services coupled | Loosen coupling |
| **Nano Services** | Too many tiny services | Merge related services |
| **Data Duplication** | Same data in multiple services | Accept eventual consistency |
| **Shared Database** | Multiple services share DB | Separate databases |

## Step 2: Service Communication

### Synchronous Communication

| Pattern | Use Case | Trade-offs |
|---------|----------|------------|
| **REST** | Simple CRUD | Easy, but synchronous |
| **gRPC** | High performance | Fast, but complex |
| **GraphQL** | Flexible queries | Flexible, but complex |

### Asynchronous Communication

| Pattern | Use Case | Trade-offs |
|---------|----------|------------|
| **Message Queue** | Task distribution | Reliable, but eventual |
| **Event Streaming** | Event sourcing | Ordered, but complex |
| **Pub/Sub** | Broadcasting | Decoupled, but no guarantee |

### Communication Selection

```
Need real-time response? → Synchronous (REST/gRPC)
Need reliability? → Asynchronous (Queue/Stream)
Need decoupling? → Pub/Sub
Need ordering? → Event Streaming
```

## Step 3: Service Patterns

### API Gateway

```mermaid
graph LR
    Client --> Gateway[API Gateway]
    Gateway --> SvcA[Service A]
    Gateway --> SvcB[Service B]
    Gateway --> SvcC[Service C]
```

**Responsibilities:**
- Request routing
- Authentication
- Rate limiting
- Load balancing

### Service Discovery

| Type | Description | Tools |
|------|-------------|-------|
| **Client-Side** | Client queries registry | Eureka, Consul |
| **Server-Side** | Load balancer queries | AWS ELB |
| **DNS-Based** | DNS resolution | CoreDNS |

### Circuit Breaker

```mermaid
stateDiagram-v2
    [*] --> CLOSED
    CLOSED --> OPEN: failures exceed threshold
    OPEN --> HALF_OPEN: timeout elapses
    HALF_OPEN --> CLOSED: probe succeeds
    HALF_OPEN --> OPEN: probe fails
```

## Step 4: Data Management

### Database per Service

| Pattern | Description | Trade-off |
|---------|-------------|-----------|
| **Database per Service** | Each service owns its data | Strong isolation, eventual consistency |
| **Shared Database** | Multiple services share DB | Simple, tight coupling |
| **CQRS** | Separate read/write models | Performance, complexity |

### Data Consistency

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Saga** | Distributed transaction | Multi-service writes |
| **Event Sourcing** | Store events, not state | Audit trail |
| **CQRS** | Separate reads from writes | Different read/write patterns |

## Step 5: Deployment Patterns

| Pattern | Description |
|---------|-------------|
| **Containerization** | Docker, Kubernetes |
| **Service Mesh** | Istio, Linkerd |
| **GitOps** | ArgoCD, Flux |
| **Blue-Green** | Zero-downtime deploys |

## Step 6: Monitoring & Observability

| Concern | Solution |
|---------|----------|
| **Distributed Tracing** | Jaeger, Zipkin, X-Ray |
| **Centralized Logging** | ELK, Loki |
| **Metrics** | Prometheus, Datadog |
| **Service Health** | Health checks, readiness probes |

## Examples

- Decompose an e-commerce monolith along bounded contexts using the strangler fig.
- Fix a distributed monolith where every deploy requires four services to release together.
- Choose sync vs async communication per interaction in a new platform.

## Common Gotchas

- Services that must deploy together are a distributed monolith - the worst of both worlds.
- Start with a modular monolith unless team scale demands independent deployment.
- Synchronous call chains across services multiply latency and failure probability.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)
- `references/microservices-patterns.md` — Microservices Patterns Reference

## Related Skills

- **arch-ddd** - Finding service boundaries
- **arch-resilience** - Circuit breakers, retries, bulkheads
- **arch-event** - Sagas and async communication
- **arch-integration** - Gateways and service mesh

## Microservices Review Template

```markdown
## Microservices Review: [System]

### Service Inventory
| Service | Responsibility | Owner | Database |
|---------|---------------|-------|----------|

### Communication
| From | To | Pattern | Protocol |
|------|----|---------|----------|

### Data Management
| Service | Data Owned | Consistency Model |
|---------|------------|-------------------|

### Deployment
| Service | Instances | Scaling Strategy |
|---------|------------|------------------|

### Recommendations
1. [Improvement]
```
