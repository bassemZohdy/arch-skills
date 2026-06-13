# Strategic Design Reference

## Bounded Context

A boundary within which a particular domain model applies.

```
┌─────────────────────┐     ┌─────────────────────┐
│   Sales Context     │     │   Shipping Context   │
│  - Order            │────▶│  - Shipment         │
│  - Customer         │     │  - Tracking         │
└─────────────────────┘     └─────────────────────┘
```

## Context Mapping Patterns

| Pattern | Description | Use When |
|---------|-------------|----------|
| **Shared Kernel** | Shared model | Tight collaboration |
| **Customer-Supplier** | Upstream/downstream | Service dependency |
| **Conformist** | Downstream conforms | No control over upstream |
| **Anti-Corruption Layer** | Translation layer | Integrating legacy |
| **Open Host Service** | Public API | Multiple consumers |
| **Published Language** | Shared specification | Cross-team |

## Ubiquitous Language

Create shared language between developers and domain experts. Document in glossary.
