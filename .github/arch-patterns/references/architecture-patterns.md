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
