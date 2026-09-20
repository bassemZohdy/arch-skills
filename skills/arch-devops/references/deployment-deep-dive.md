# Deployment Deep Dive

**Source:** DORA Metrics, Google SRE, Continuous Delivery

## DORA Metrics

Use the [current five-metric model](https://dora.dev/guides/dora-metrics/).
Measure deployment frequency, change lead time, failed-deployment recovery,
change-failure proportion and deployment rework. Keep deployment-specific
recovery separate from broad service MTTR, and record definition/version,
sampling window and system scope. Adopt targets from local evidence rather
than treating historical performance bands as universal gates.

## Deployment Strategies

| Strategy | Downtime | Cost | Rollback | Use Case |
|----------|----------|------|----------|----------|
| **Blue-Green** | None | High | Instant | Critical systems |
| **Canary** | None | Low | Quick | Gradual rollout |
| **Rolling** | None | Low | Medium | Standard updates |
| **Recreate** | Yes | Low | Slow | Development |

## CI/CD Pipeline Best Practices

### Pipeline Stages

```
Code → Build → Test → Security → Stage → Deploy → Monitor
```

### Quality Gates

| Gate | Metric | Threshold |
|------|--------|-----------|
| **Coverage** | Line coverage | > 80% |
| **Security** | Vulnerabilities | 0 critical |
| **Performance** | Response time | < 200ms |
| **Complexity** | Cyclomatic | < 10 |

## GitOps Principles

1. **Declarative** - System state described declaratively
2. **Versioned** - Entire state stored in Git
3. **Automated** - Changes applied automatically
4. **Self-healing** - System reconciles to desired state

### GitOps Tools

| Tool | Description |
|------|-------------|
| **ArgoCD** | Kubernetes GitOps |
| **Flux** | GitOps toolkit |
| **Jenkins X** | Cloud-native CI/CD |

## Release Management

### Release Types

| Type | Description | Frequency |
|------|-------------|-----------|
| **Major** | Breaking changes | Quarterly/Yearly |
| **Minor** | New features | Monthly/Weekly |
| **Patch** | Bug fixes | As needed |
| **Hotfix** | Critical fixes | Immediate |

### Rollback Triggers

- Error rate exceeds threshold
- Performance degradation > 50%
- Critical bug discovered
- Security vulnerability identified
- Data integrity issue
