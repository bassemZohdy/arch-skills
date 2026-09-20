---
name: arch-data
description: Design data architecture. Use when modeling databases, designing data pipelines, implementing data governance, planning data lakes, or establishing data architecture standards.
---

# Data Architecture

Systematic approach to designing data systems.

## DAP contribution

For a DAP invocation, read `framework/contribution-contract.md` from the outer
package root (the repository root in a source checkout). Keep standalone tasks
within their requested scope. Use `assets/review-template.md` and record data authority, lineage/source revisions, classification, schema/lifecycle decisions, retention, quality/freshness and restore criteria.
Return evidence-linked proposals and VER plans, not invented approvals or delivery proof.

## Workflow

```
1. Understand Data → What data do we have?
2. Model → How to structure it?
3. Store → Where to persist it?
4. Process → How to transform it?
5. Govern → How to control it?
6. Secure → How to protect it?
```

## Step 1: Data Types

| Type | Characteristics | Example |
|------|-----------------|---------|
| **Transactional** | ACID, high consistency | Orders, payments |
| **Analytical** | Read-heavy, aggregations | Reports, dashboards |
| **Temporal** | Time-series, append-only | Logs, metrics |
| **Document** | Semi-structured, flexible | JSON, XML |
| **Graph** | Relationships, traversal | Social networks |

## Step 2: Data Modeling

### Relational Modeling

| Concept | Description |
|---------|-------------|
| **Entities** | Business objects (Customer, Order) |
| **Attributes** | Properties (name, email) |
| **Relationships** | Connections (Customer has Orders) |
| **Normalization** | Reduce redundancy (1NF, 2NF, 3NF) |

### Dimensional Modeling

| Concept | Description | Use Case |
|---------|-------------|----------|
| **Fact** | Measures/events | Sales, clicks |
| **Dimension** | Context | Time, product, location |
| **Star Schema** | Facts + dimensions | Data warehouses |
| **Snowflake** | Normalized dimensions | Complex hierarchies |

### NoSQL Modeling

| Type | Model | Use Case |
|------|-------|----------|
| **Document** | JSON/BSON | Content management |
| **Key-Value** | Simple lookup | Caching, sessions |
| **Column-Family** | Wide columns | Time-series, IoT |
| **Graph** | Nodes + edges | Social, recommendations |

### Ownership and Data Contracts

Assign a data owner and steward for each domain. Define schema, quality
expectations, freshness, compatibility, classification, retention, deletion and
lineage at the producer/consumer boundary. A data mesh is an organizational and
governance choice, not a reason to distribute storage without ownership.

## Step 3: Storage Selection

| Need | Solution | Examples |
|------|----------|----------|
| **OLTP** | Relational DB | PostgreSQL, MySQL |
| **OLAP** | Data warehouse | Redshift, BigQuery |
| **NoSQL** | Document/Key-Value | MongoDB, DynamoDB |
| **Cache** | In-memory | Redis, Memcached |
| **Search** | Full-text | Elasticsearch |
| **Object** | Blob storage | S3, Azure Blob |
| **Time-series** | TSDB | InfluxDB, TimescaleDB |

## Step 4: Data Pipeline Patterns

### ETL (Extract, Transform, Load)

```
Source → Extract → Transform → Load → Destination
```

**Use when:** Transformation needed before storage.

### ELT (Extract, Load, Transform)

```
Source → Extract → Load → Transform → Destination
```

**Use when:** Storage can handle transformation (data lakes).

### Streaming

```
Source → Stream → Process → Sink
```

**Use when:** Real-time processing needed.

### Batch

```
Source → Schedule → Process → Destination
```

**Use when:** Periodic processing acceptable.

## Step 5: Data Governance

### Data Quality Dimensions

| Dimension | Description | Measurement |
|-----------|-------------|-------------|
| **Accuracy** | Correct values | Validation rules |
| **Completeness** | No missing data | Null checks |
| **Consistency** | Same across systems | Cross-reference |
| **Timeliness** | Up-to-date | Freshness metrics |
| **Uniqueness** | No duplicates | Dedup checks |

### Data Lineage

Track data flow from source to destination:

```
Source System → Ingestion → Processing → Storage → Consumption
     ↓              ↓           ↓          ↓          ↓
   Audit Log    Quality    Transform   Catalog   Access Log
```

### Data Classification

| Level | Description | Controls |
|-------|-------------|----------|
| **Public** | No restrictions | None |
| **Internal** | Business use only | Access control |
| **Confidential** | Sensitive data | Encryption, audit |
| **Restricted** | Highly sensitive | Strict controls |

## Step 6: Data Security

| Control | Purpose |
|---------|---------|
| **Encryption at rest** | Protect stored data |
| **Encryption in transit** | Protect moving data |
| **Access control** | Limit who can access |
| **Data masking** | Hide sensitive values |
| **Audit logging** | Track access |

Also model backup, restore, regional failure, deletion propagation and recovery
verification. For analytical or replicated data, distinguish the source of truth
from derived copies and state the maximum acceptable staleness.

## Examples

- Choose storage per data domain for an analytics-heavy SaaS product.
- Design an ELT pipeline into a warehouse with data quality checks.
- Classify data and define retention for a system holding PII.

## Common Gotchas

- Schema-on-read defers, not removes, the modeling work; someone still pays it at query time.
- One database rarely fits all access patterns; but every extra store adds operational cost.
- Data lineage retrofitted after an audit request is painful; capture it in the pipeline from day one.
- A schema registry or catalog does not make data quality true; publish executable checks and owner-visible failures.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)
- `references/data-deep-dive.md` — Data Architecture Deep Dive
- `references/data-modeling.md` — Data Modeling Reference

## Related Skills

- **arch-event** - Streaming pipelines and CDC
- **arch-compliance** - Retention, classification, and audit requirements
- **arch-ai** - Embedding pipelines and training data

## Output template

Use `assets/review-template.md`. Populate its scope and evidence fields for DAP work;
keep missing measurements and approvals explicit.
