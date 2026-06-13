# Performance Engineering Deep Dive

**Source:** Google SRE Book, High Performance Browser Networking

## SLA/SLO/Error Budget (Google SRE)

### Terminology

| Term | Definition | Example |
|------|------------|---------|
| **SLI** | Service Level Indicator | Request latency, error rate |
| **SLO** | Service Level Objective | 99% of requests < 200ms |
| **SLA** | Service Level Agreement | Contractual commitment |
| **Error Budget** | Allowed failures | 0.01% = 4.3 min/month |

### Error Budget Policy

| Budget Remaining | Action |
|------------------|--------|
| > 50% | Normal development |
| 25-50% | Caution, extra testing |
| < 25% | Feature freeze, reliability focus |
| 0% | Stop all changes, fix reliability |

### SLI Selection by System Type

| System Type | Key SLIs |
|-------------|----------|
| **User-facing** | Availability, Latency, Throughput |
| **Storage** | Latency, Availability, Durability |
| **Big Data** | Throughput, End-to-end Latency |
| **All Systems** | Correctness |

## Performance Patterns

### Caching Strategies

| Strategy | Description | Use Case |
|----------|-------------|----------|
| **Cache-Aside** | App manages cache | General purpose |
| **Write-Through** | Write to cache and DB | Strong consistency |
| **Write-Behind** | Write to cache, async to DB | High write throughput |
| **Read-Through** | Cache loads on miss | Read-heavy workloads |

### Database Optimization

| Technique | Impact | Effort |
|-----------|--------|--------|
| Indexing | High | Low |
| Query optimization | High | Medium |
| Read replicas | High | Medium |
| Connection pooling | Medium | Low |
| Caching | High | Medium |
| Sharding | High | High |

## Performance Testing

### Test Types

| Test Type | Purpose | Duration |
|-----------|---------|----------|
| **Load** | Expected traffic | 30-60 min |
| **Stress** | Beyond capacity | Until failure |
| **Spike** | Sudden bursts | Minutes |
| **Soak** | Sustained load | Hours/days |

### Key Metrics

| Metric | Target | Tool |
|--------|--------|------|
| Response Time (p95) | < 200ms | APM |
| Throughput | > 1000 req/s | Load testing |
| Error Rate | < 0.1% | Monitoring |
| CPU Utilization | < 70% | Monitoring |
| Memory Utilization | < 80% | Monitoring |
