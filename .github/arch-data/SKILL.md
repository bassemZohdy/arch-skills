---
name: arch-data
description: Guide data architecture design. Use when modeling databases, designing data pipelines, implementing data governance, planning data lakes, or establishing data architecture standards.
---

# Data Architecture

Systematic approach to designing data systems.

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

## Data Architecture Review Template

```markdown
## Data Architecture Review: [System]

### Data Domains
| Domain | Type | Volume | Retention |
|--------|------|--------|-----------|

### Storage
| Data | Store | Justification |
|------|-------|---------------|

### Pipelines
| Pipeline | Type | Frequency | SLA |
|----------|------|-----------|-----|

### Governance
- Classification: [List]
- Quality metrics: [List]

### Recommendations
1. [Improvement]
```
