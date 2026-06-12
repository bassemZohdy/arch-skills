# Microservices Patterns Reference

## Decomposition Strategies

| Strategy | Description | Use Case |
|----------|-------------|----------|
| **By Business Capability** | Align with business functions | Standard approach |
| **By Subdomain** | DDD bounded contexts | Complex domains |
| **By Data Ownership** | Separate data per service | Data-intensive |
| **By Team** | Conway's Law alignment | Large organizations |

## Communication Patterns

| Pattern | Use Case | Trade-off |
|---------|----------|-----------|
| **REST** | Simple CRUD | Easy, but synchronous |
| **gRPC** | High performance | Fast, but complex |
| **GraphQL** | Flexible queries | Flexible, but complex |
| **Message Queue** | Task distribution | Reliable, but eventual |
| **Event Streaming** | Event sourcing | Ordered, but complex |

## Data Management Patterns

| Pattern | Description | Trade-off |
|---------|-------------|-----------|
| **Database per Service** | Each service owns its data | Strong isolation, eventual consistency |
| **Shared Database** | Multiple services share DB | Simple, tight coupling |
| **CQRS** | Separate read/write models | Performance, complexity |
| **Saga** | Distributed transaction | Multi-service writes |

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Distributed Monolith** | Services coupled | Loosen coupling |
| **Nano Services** | Too many tiny services | Merge related services |
| **Data Duplication** | Same data in multiple services | Accept eventual consistency |
| **Shared Database** | Multiple services share DB | Separate databases |
