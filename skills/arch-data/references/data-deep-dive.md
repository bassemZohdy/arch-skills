# Data Architecture Deep Dive

**Source:** DAMA-DMBOK, Data Mesh, Data Lakehouse

## Data Architecture Principles

| Principle | Description |
|-----------|-------------|
| **Data as an Asset** | Data has value, must be managed |
| **Data Quality** | Accurate, complete, timely |
| **Data Governance** | Policies and processes |
| **Data Security** | Protect sensitive data |
| **Data Integration** | Connect data sources |
| **Data Privacy** | Respect user privacy |

## Data Modeling Patterns

### Relational Modeling

| Form | Rule |
|------|------|
| **1NF** | Atomic values, no repeating groups |
| **2NF** | 1NF + no partial dependencies |
| **3NF** | 2NF + no transitive dependencies |

### Dimensional Modeling

| Concept | Description | Use Case |
|---------|-------------|----------|
| **Fact** | Measures/events | Sales, clicks |
| **Dimension** | Context | Time, product, location |
| **Star Schema** | Facts + dimensions | Data warehouses |
| **Snowflake** | Normalized dimensions | Complex hierarchies |

### NoSQL Patterns

| Type | Data Model | Query Pattern |
|------|------------|---------------|
| **Document** | JSON/BSON | Flexible queries |
| **Key-Value** | Simple lookup | Get/Put by key |
| **Column-Family** | Sparse columns | Range scans |
| **Graph** | Nodes + edges | Traversal |

## Data Quality Dimensions

| Dimension | Description | Measurement |
|-----------|-------------|-------------|
| **Accuracy** | Correct values | Validation rules |
| **Completeness** | No missing data | Null checks |
| **Consistency** | Same across systems | Cross-reference |
| **Timeliness** | Up-to-date | Freshness metrics |
| **Uniqueness** | No duplicates | Dedup checks |

## Data Governance

### Data Classification

| Level | Description | Controls |
|-------|-------------|----------|
| **Public** | Publicly readable | Integrity, availability and controlled writes |
| **Internal** | Business use only | Access control |
| **Confidential** | Sensitive data | Encryption, audit |
| **Restricted** | Highly sensitive | Strict controls, MFA |

### Data Lineage

```
Source System → Ingestion → Processing → Storage → Consumption
     ↓              ↓           ↓          ↓          ↓
   Audit Log    Quality    Transform   Catalog   Access Log
```

## Data Pipeline Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **ETL** | Extract, Transform, Load | Traditional |
| **ELT** | Extract, Load, Transform | Data lakes |
| **Streaming** | Real-time processing | Events |
| **Batch** | Periodic processing | Reports |

## Data Tools

| Category | Tools |
|----------|-------|
| **Orchestration** | Airflow, Prefect, Dagster |
| **Processing** | Spark, Flink, Kafka Streams |
| **Storage** | S3, Delta Lake, Iceberg |
| **Catalog** | DataHub, Amundsen, OpenMetadata |
| **Quality** | Great Expectations, dbt tests |
