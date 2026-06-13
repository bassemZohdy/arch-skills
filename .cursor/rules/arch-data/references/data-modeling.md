# Data Modeling Reference

## Relational Modeling

### Normal Forms

| Form | Rule |
|------|------|
| **1NF** | Atomic values, no repeating groups |
| **2NF** | 1NF + no partial dependencies |
| **3NF** | 2NF + no transitive dependencies |

### Cardinality

| Type | Symbol | Example |
|------|--------|---------|
| One-to-One | 1:1 | User ↔ Profile |
| One-to-Many | 1:N | User → Orders |
| Many-to-Many | M:N | Students ↔ Courses |

## Dimensional Modeling

### Star Schema

```
        ┌──────────┐
        │   Time   │
        └────┬─────┘
             │
┌──────────┐ │ ┌──────────┐
│ Product  ├─┴─┤ Location │
└────┬─────┘   └────┬─────┘
     │              │
     └──────┬───────┘
            │
     ┌──────┴───────┐
     │   Fact_Sales │
     └──────────────┘
```

## NoSQL Modeling

| Type | Data Model | Query Pattern |
|------|------------|---------------|
| Document | JSON/BSON | Flexible queries |
| Key-Value | Simple lookup | Get/Put by key |
| Column-Family | Sparse columns | Range scans |
| Graph | Nodes + edges | Traversal |
