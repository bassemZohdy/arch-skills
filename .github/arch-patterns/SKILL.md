---
name: arch-patterns
description: Guide architecture pattern selection and application. Use when choosing between Clean Architecture, Hexagonal Architecture, Layered Architecture, Pipes & Filters, or other architectural patterns.
---

# Architecture Patterns

Systematic approach to selecting and applying architecture patterns.

## Workflow

```
1. Understand Requirements → What qualities matter?
2. Evaluate Patterns → Which patterns fit?
3. Select Pattern → Choose based on trade-offs
4. Apply Pattern → Implement with best practices
5. Validate → Ensure pattern is followed
6. Document → Record pattern usage
```

## Step 1: Pattern Categories

### Structural Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Layered** | Horizontal layers (UI, Business, Data) | Traditional apps |
| **Hexagonal** | Ports and adapters | Testable systems |
| **Clean Architecture** | Concentric circles with dependencies inward | Complex business logic |
| **Onion Architecture** | Similar to Clean, emphasizes domain |

### Behavioral Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Event-Driven** | Events trigger processing | Async systems |
| **CQRS** | Separate read/write models | Different read/write patterns |
| **Saga** | Distributed transactions | Multi-service operations |
| **State Machine** | State transitions | Workflow systems |

### Integration Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **API Gateway** | Single entry point | External APIs |
| **Service Mesh** | Infrastructure communication | Microservices |
| **Message Broker** | Async communication | Decoupled systems |
| **Event Streaming** | Ordered event log | Event sourcing |

## Step 2: Clean Architecture

### Concentric Circles

```
┌─────────────────────────────────────┐
│           Frameworks               │
│  ┌───────────────────────────────┐  │
│  │        Interface Adapters     │  │
│  │  ┌───────────────────────┐    │  │
│  │  │     Application        │    │  │
│  │  │  ┌───────────────┐    │    │  │
│  │  │  │   Domain       │    │    │  │
│  │  │  └───────────────┘    │    │  │
│  │  └───────────────────────┘    │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

### Dependency Rule

Dependencies point inward only:
- **Domain** → Nothing (innermost)
- **Application** → Domain
- **Interface Adapters** → Application, Domain
- **Frameworks** → All (outermost)

### Key Principles

| Principle | Description |
|-----------|-------------|
| **Independence** | Frameworks are plugins |
| **Testability** | Business logic testable without UI/DB |
| **UI Independence** | UI can change without affecting business |
| **Database Independence** | Business logic unaware of storage |

## Step 3: Hexagonal Architecture

### Ports and Adapters

```
┌─────────────────────────────────────┐
│            Primary Ports            │
│  ┌───────────────────────────────┐  │
│  │        Application Core       │  │
│  │  ┌───────────────────────┐    │  │
│  │  │     Domain Model       │    │  │
│  │  └───────────────────────┘    │  │
│  └───────────────────────────────┘  │
│            Secondary Ports          │
└─────────────────────────────────────┘
```

### Port Types

| Port Type | Description | Examples |
|-----------|-------------|----------|
| **Primary** | Drives the application | REST API, CLI, UI |
| **Secondary** | Driven by the application | Database, Email, File |

### Adapter Types

| Adapter Type | Description | Examples |
|--------------|-------------|----------|
| **Driving** | Implements primary ports | REST controller, CLI handler |
| **Driven** | Implements secondary ports | Database adapter, Email adapter |

## Step 4: Layered Architecture

### Traditional Layers

```
┌─────────────────────────┐
│    Presentation Layer   │
├─────────────────────────┤
│    Business Layer       │
├─────────────────────────┤
│    Persistence Layer    │
├─────────────────────────┤
│    Database Layer       │
└─────────────────────────┘
```

### Layer Rules

| Rule | Description |
|------|-------------|
| **Dependency Direction** | Upper layers depend on lower |
| **No Skip Layers** | Don't bypass intermediate layers |
| **Interface Contracts** | Layers communicate via interfaces |
| **Single Responsibility** | Each layer has one purpose |

## Step 5: Pipes and Filters

### Pattern Structure

```
Input → [Filter 1] → [Filter 2] → [Filter 3] → Output
```

### Filter Types

| Type | Description | Use Case |
|------|-------------|----------|
| **Transform** | Convert data format | Data transformation |
| **Filter** | Selectively pass data | Data filtering |
| **Aggregate** | Combine multiple inputs | Data aggregation |
| **Route** | Direct to different paths | Content-based routing |

## Step 6: Pattern Selection Matrix

| Requirement | Recommended Pattern |
|-------------|---------------------|
| **Testability** | Hexagonal, Clean |
| **Complex Business Logic** | Clean Architecture |
| **Simple CRUD** | Layered |
| **Event Processing** | Event-Driven, CQRS |
| **Distributed Systems** | Service Mesh, Saga |
| **Legacy Integration** | Hexagonal, Adapter |

## Pattern Review Template

```markdown
## Pattern Review: [System]

### Selected Pattern
- Pattern: [Name]
- Rationale: [Why this pattern]

### Implementation
| Component | Pattern Element | Status |
|-----------|----------------|--------|

### Compliance
| Rule | Status | Violations |
|------|--------|------------|

### Recommendations
1. [Improvement]
```
