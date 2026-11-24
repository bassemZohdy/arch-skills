# Deployment Strategies Reference

## Strategy Comparison

| Strategy | Downtime | Cost | Complexity | Rollback | Use Case |
|----------|----------|------|------------|----------|----------|
| **Blue-Green** | Low when cutover is validated | Parallel capacity | High | Traffic switch only while state-compatible | Rehearsed environment switch |
| **Canary** | Depends on routing, capacity and health | Variable | Medium | Stop exposure; reconcile affected state | Gradual rollout |
| **Rolling** | Depends on readiness, draining and capacity | May need surge capacity | Medium | Requires mixed-version/state compatibility | Incremental fleet updates |
| **Recreate** | Yes | Low | Low | Slow | Development |

Separate application rollback from data recovery. Account for writes since cutover,
schema compatibility, replay and reconciliation before restoring or switching back.
Use expand/migrate/contract changes and verify quantitative promotion/abort criteria.

## CI/CD Best Practices

| Practice | Description |
|----------|-------------|
| **Fast builds** | Keep commit-stage feedback short (about 10 minutes is a common goal); set the target from measured team feedback needs |
| **Parallel stages** | Run independent tests together |
| **Artifact immutability** | Same artifact across environments |
| **Automated rollback** | Quick recovery capability |
| **Feature flags** | Decouple deploy from release |
| **Canary releases** | Gradual rollout |
| **Infrastructure as Code** | Version-controlled infrastructure |

## GitOps Pattern

```
Git Push → Controller → Diff → Apply → Kubernetes
```

**Benefits:**
- Audit trail in Git
- Automated reconciliation
- Auditable desired-state changes; rollback still requires compatible application/data state
- Version control for infrastructure

## Environment Strategy

| Environment | Purpose | Data | Parity |
|-------------|---------|------|--------|
| **Local** | Developer workstations | Mock/local | Low |
| **Development** | Integration testing | Test data | Medium |
| **Staging** | Pre-production validation | Production-like | High |
| **Production** | Live system | Real data | Target |

## Deployment Automation Tools

| Category | Tools |
|----------|-------|
| **CI/CD** | GitHub Actions, GitLab CI, Jenkins, CircleCI |
| **IaC** | Terraform, Pulumi, CloudFormation |
| **Config Mgmt** | Ansible, Chef, Puppet |
| **Containers** | Docker, Kubernetes, ECS |
| **GitOps** | ArgoCD, Flux, Jenkins X |

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
- Performance or error-budget degradation beyond the workload's adopted threshold
- Critical bug discovered
- Security vulnerability identified
- Data integrity issue
