# Architecture Patterns Reference

## Clean Architecture

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

- Domain → Nothing (innermost)
- Application → Domain
- Interface Adapters → Application, Domain
- Frameworks → All (outermost)

## Hexagonal Architecture

### Ports and Adapters

| Port Type | Description | Examples |
|-----------|-------------|----------|
| **Primary** | Drives the application | REST API, CLI, UI |
| **Secondary** | Driven by the application | Database, Email, File |

## Layered Architecture

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

- Dependencies point downward only
- Don't skip layers
- Communicate via interfaces
- Single responsibility per layer

## Pipes and Filters

```
Input → [Filter 1] → [Filter 2] → [Filter 3] → Output
```

| Filter Type | Description | Use Case |
|-------------|-------------|----------|
| **Transform** | Convert data format | Data transformation |
| **Filter** | Selectively pass data | Data filtering |
| **Aggregate** | Combine multiple inputs | Data aggregation |
| **Route** | Direct to different paths | Content-based routing |

## Vertical Slice Architecture

Organize code by feature instead of by technical layer. Each slice owns its
API endpoint, business logic, and data access end to end.

```
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│  Feature A  │ │  Feature B  │ │  Feature C  │
│  ┌───────┐  │ │  ┌───────┐  │ │  ┌───────┐  │
│  │  API  │  │ │  │  API  │  │ │  │  API  │  │
│  │ Logic │  │ │  │ Logic │  │ │  │ Logic │  │
│  │ Data  │  │ │  │ Data  │  │ │  │ Data  │  │
│  └───────┘  │ │  └───────┘  │ │  └───────┘  │
└─────────────┘ └─────────────┘ └─────────────┘
```

### Slice Rules

- Keep slices independent; changes to one feature must not ripple into others.
- Share code only when it is genuinely common; prefer duplication over the wrong abstraction.
- Handle cross-cutting concerns (logging, validation, auth) via pipeline behaviors, not base classes.
- Pairs naturally with CQRS (a slice = one command or query handler).

### When to Use

| Use When | Avoid When |
|----------|------------|
| Feature-focused teams delivering independently | Heavy reuse of complex domain logic across features |
| Requirements change per feature, not per layer | The domain needs a single, deeply unified model |
| Combining with CQRS / mediator pipelines | Simple CRUD where any structure is overhead |

## Modular Monolith

A single deployable unit split into autonomous modules with explicit,
enforced boundaries — monolith operational simplicity with module isolation.

```
┌──────────────────────────────────────────────┐
│                 Single Process               │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ Module A │  │ Module B │  │ Module C │   │
│  │ (owns    │  │ (owns    │  │ (owns    │   │
│  │ its data)│  │ its data)│  │ its data)│   │
│  └──────────┘  └──────────┘  └──────────┘   │
│        contracts + in-process events         │
└──────────────────────────────────────────────┘
```

### Module Rules

- Each module owns its schema/data; no cross-module table joins.
- Expose a public contract per module; hide internals behind it.
- Communicate between modules via contracts or in-process domain events.
- Enforce boundaries with architecture tests (see arch-fitness) or they erode.

### When to Use

| Use When | Avoid When |
|----------|------------|
| Want monolith simplicity with a path to extract services later | Independent scaling or deployment per module is required now |
| Team is small but the domain has clear bounded contexts | Organization needs hard team/service ownership boundaries |
| Migrating away from a big ball of mud incrementally | Latency-sensitive modules need process isolation |

## External Resources

- [Vertical Slice Architecture](https://awesome-architecture.com/vertical-slice-architecture/) — curated articles, videos, and samples
- [Modular Monolith](https://awesome-architecture.com/modular-monolith/) — curated articles, videos, and samples
