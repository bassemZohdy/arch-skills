# Microservices Patterns Reference

**Source:** microservices.io by Chris Richardson

## Decomposition Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Decompose by Business Capability** | Services aligned with business functions | Standard approach |
| **Decompose by Subdomain** | Services aligned with DDD subdomains | Complex domains |
| **Self-contained Service** | Handle sync requests without waiting | Performance critical |
| **Service per Team** | Conway's Law alignment | Large organizations |

## Data Management Patterns

| Pattern | Description | Trade-off |
|---------|-------------|-----------|
| **Database per Service** | Each service owns its data | Strong isolation, eventual consistency |
| **Shared Database** | Multiple services share DB | Simple, tight coupling |
| **Saga** | Sequence of local transactions | Distributed consistency |
| **CQRS** | Separate read/write models | Performance, complexity |
| **Event Sourcing** | Persist aggregates as events | Audit trail, complexity |
| **API Composition** | Invoke services, join in memory | Simple queries |
| **Command-side Replica** | Queryable replica for commands | Performance |

## Communication Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Remote Procedure Invocation** | Synchronous RPI protocol | Real-time |
| **Messaging** | Asynchronous messaging | Decoupled |
| **Domain-specific Protocol** | Custom protocol | Specialized needs |
| **Idempotent Consumer** | Handle duplicate messages | Reliability |

## Transactional Messaging

| Pattern | Description |
|---------|-------------|
| **Transactional Outbox** | Write to outbox in same transaction |
| **Transaction Log Tailing** | Tail database log for changes |
| **Polling Publisher** | Poll outbox for new messages |

## Service Discovery

| Pattern | Description |
|---------|-------------|
| **Client-Side Discovery** | Client queries registry |
| **Server-Side Discovery** | Router queries registry |
| **Service Registry** | Database of service locations |
| **Self Registration** | Service registers itself |
| **3rd Party Registration** | External registrar |

## Observability Patterns

| Pattern | Description |
|---------|-------------|
| **Log Aggregation** | Centralized logging |
| **Application Metrics** | Instrumented statistics |
| **Audit Logging** | User activity recording |
| **Distributed Tracing** | Request flow tracking |
| **Exception Tracking** | Centralized exception handling |
| **Health Check API** | Service health endpoint |

## Deployment Patterns

| Pattern | Description |
|---------|-------------|
| **Multiple Services per Host** | Shared host |
| **Service per Host** | Dedicated host |
| **Service per VM** | Virtual machine isolation |
| **Service per Container** | Container isolation |
| **Serverless Deployment** | Platform-managed |
| **Service Deployment Platform** | Automated platform |

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Distributed Monolith** | Services tightly coupled | Loosen coupling |
| **Nano Services** | Too many tiny services | Merge related services |
| **Data Duplication** | Same data in multiple services | Accept eventual consistency |
| **Shared Database** | Multiple services share DB | Separate databases |
| **Synchronous Everything** | All calls synchronous | Use async where possible |
