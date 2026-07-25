---
name: arch-devops
description: Design DevOps, deployment, and release engineering architecture. Use when designing CI/CD pipelines, choosing deployment strategies (blue-green, canary, rolling), writing Infrastructure as Code, setting up Kubernetes, implementing GitOps, planning environments, or establishing release management and rollback processes.
---

# DevOps & Deployment Architecture

Systematic approach to infrastructure automation, CI/CD, deployment strategies, and release engineering.

## Workflow

```
1. Define Infrastructure → IaC for provisioning
2. Build Pipeline → CI/CD stages and gates
3. Choose Deployment Strategy → Blue-green, canary, rolling
4. Plan Environments → Dev, staging, production parity
5. Manage Releases → Versioning, approvals, communication
6. Prepare Rollback → Recovery procedures
7. Measure → DORA metrics, pipeline health
```

## Step 1: Infrastructure as Code

### IaC Tools

| Tool | Type | Use Case |
|------|------|----------|
| **Terraform** | Multi-cloud | Infrastructure provisioning |
| **Pulumi** | Multi-cloud | IaC with programming languages |
| **CloudFormation** | AWS | AWS-specific provisioning |
| **ARM/Bicep** | Azure | Azure-specific provisioning |
| **Ansible** | Config mgmt | Configuration and deployment |

### IaC Best Practices

| Practice | Description |
|----------|-------------|
| **Version Control** | Store IaC in Git |
| **Modular Design** | Reusable modules |
| **State Management** | Remote state with locking |
| **Plan/Apply** | Review changes before apply |
| **Immutable Infrastructure** | Replace, don't modify |

### Configuration Patterns

| Pattern | Description |
|---------|-------------|
| **Configuration as Code** | Version-controlled configs |
| **Secrets Management** | Vault, AWS Secrets Manager |
| **Feature Flags** | Runtime feature control (see arch-features) |

## Step 2: CI/CD Pipeline

### Pipeline Stages

```
Code → Build → Test → Security → Stage → Deploy → Monitor
```

| Stage | Purpose | Tools |
|-------|---------|-------|
| **Code** | Version control | Git, GitHub, GitLab |
| **Build** | Compile, package | Maven, npm, Docker |
| **Test** | Automated tests | JUnit, pytest, Jest |
| **Security** | Vulnerability scan | Snyk, Trivy, SonarQube |
| **Stage** | Deploy to staging | Terraform, Ansible |
| **Deploy** | Deploy to production | Kubernetes, ArgoCD, ECS |
| **Monitor** | Health checks | Prometheus, Datadog |

### Pipeline Principles

- **Fast feedback**: Fail early, fail fast
- **Parallel execution**: Run independent stages in parallel
- **Artifact immutability**: Same artifact promoted across environments
- **Environment parity**: Staging ≈ Production

## Step 3: Deployment Strategies

### Blue-Green Deployment

```mermaid
graph LR
    LB((Load Balancer))
    Blue["Production (Blue) - active"]
    Green["Production (Green) - idle / next release"]
    LB --> Blue
    LB -. "switch traffic" .-> Green
    Blue -. rollback .-> Green
```

| Pros | Cons |
|------|------|
| Zero downtime | Double infrastructure |
| Easy rollback | Cost |
| Full testing before switch | Stateful data cutover |

### Canary Deployment

```mermaid
graph LR
    Traffic((Traffic))
    Current["Current Version - 95%"]
    Canary["New Version (canary) - 5%"]
    Traffic -->|95%| Current
    Traffic -->|5%| Canary
```

| Pros | Cons |
|------|------|
| Gradual rollout | Complex routing |
| Risk limited to small percentage | Monitoring overhead |
| Quick rollback | Slower full deployment |

### Rolling Deployment

```mermaid
graph LR
    subgraph Batch1[Batch 1]
        B1a[New] --> B1b[New] --> B1c[Old] --> B1d[Old]
    end
    subgraph Batch2[Batch 2]
        B2a[New] --> B2b[New] --> B2c[New] --> B2d[Old]
    end
    subgraph Batch3[Batch 3]
        B3a[New] --> B3b[New] --> B3c[New] --> B3d[New]
    end
    Batch1 --> Batch2 --> Batch3
```

| Pros | Cons |
|------|------|
| No extra infrastructure | Rollback complicated |
| Gradual rollout | Version skew possible |
| Simple | Slower than blue-green |

### Recreate

```
[Old] → [Stop] → [Start] → [New]
```

Simple and clean-state, but causes downtime. Acceptable only for non-critical or internal systems.

### Strategy Selection

| Requirement | Strategy |
|-------------|----------|
| Zero downtime, instant rollback | Blue-green |
| Risk mitigation on user-facing change | Canary |
| Resource-constrained, tolerate skew | Rolling |
| Downtime acceptable | Recreate |

## Step 4: Container Orchestration

### Kubernetes Building Blocks

| Component | Description |
|-----------|-------------|
| **Pod** | Smallest deployable unit |
| **Deployment** | Manages pod replicas and rolling updates |
| **Service** | Network endpoint for pods |
| **Ingress** | External access routing |
| **ConfigMap / Secret** | Configuration and sensitive data |

### Kubernetes Best Practices

- Set CPU/memory resource requests and limits
- Configure liveness and readiness probes
- Use rolling updates for zero-downtime deployments
- Enable horizontal auto-scaling based on metrics
- Restrict pod communication with network policies

## Step 5: GitOps

### GitOps Principles

1. **Declarative** — System state described declaratively
2. **Versioned** — Entire state stored in Git
3. **Automated** — Changes applied automatically
4. **Self-healing** — System reconciles to desired state

```mermaid
graph LR
    Dev[Developer] -->|commit| Repo[Git Repo]
    Repo -->|detect change| Controller[GitOps Controller]
    Controller -->|diff| Diff[Diff desired vs live]
    Diff -->|apply| Cluster[Kubernetes Cluster]
    Cluster -. reconcile .-> Controller
```

| Tool | Description |
|------|-------------|
| **ArgoCD** | Kubernetes GitOps with UI |
| **Flux** | GitOps toolkit |
| **Jenkins X** | Cloud-native CI/CD |

## Step 6: Environments & Release Management

### Environment Types

| Environment | Purpose | Data |
|-------------|---------|------|
| **Local** | Developer workstations | Mock/local |
| **Development** | Integration testing | Test data |
| **Staging** | Pre-production validation | Production-like |
| **Production** | Live system | Real data |

### Release Types

| Type | Description | Frequency |
|------|-------------|-----------|
| **Major** | Breaking changes | Quarterly/Yearly |
| **Minor** | New features | Monthly/Weekly |
| **Patch** | Bug fixes | As needed |
| **Hotfix** | Critical fixes | Immediate |

### Rollback Strategy

| Trigger | Action |
|---------|--------|
| Error rate exceeds threshold | Automated rollback or traffic shift |
| Performance degradation | Route traffic to previous version |
| Critical bug | Toggle feature flag or code rollback |
| Schema issue | Database rollback (slow — design migrations to be backward compatible) |

## Step 7: DORA Metrics

Measure delivery performance with the four DORA metrics:

| Metric | Elite Performance |
|--------|-------------------|
| **Deployment frequency** | On-demand (multiple per day) |
| **Lead time for changes** | Less than one day |
| **Change failure rate** | 0-15% |
| **Time to restore service** | Less than one hour |

## Step 8: Infrastructure Security

| Concern | Solution |
|---------|----------|
| **Secrets** | HashiCorp Vault, AWS Secrets Manager |
| **Network** | Network policies, security groups |
| **Image Scanning** | Trivy, Clair, Snyk |
| **Runtime Security** | Falco, Sysdig |
| **Policy as Code** | Open Policy Agent, Kyverno |

## Examples

- Design a blue-green deployment for a payment service with instant rollback.
- Write a Terraform module and GitHub Actions pipeline for a new microservice.
- Set up GitOps with ArgoCD and measure the team against DORA metrics.

## Common Gotchas

- Database schema changes break simple rollbacks; make migrations backward compatible and decouple them from code deploys.
- Blue-green doubles infrastructure cost and does not solve stateful cutover by itself.
- Staging that diverges from production hides deployment bugs; enforce parity through IaC.
- A canary without automated health-based rollback is just a slow big-bang release.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)
- `references/devops-practices.md` — CI/CD, IaC, and release-management deep dive
- `references/deployment-strategies.md` — Blue-green, canary, and rolling comparison
- `references/deployment-deep-dive.md` — Kubernetes, GitOps, and advanced deployment

## Related Skills

- **arch-cloud** - Cloud provider selection and Well-Architected review
- **arch-observability** - Monitoring, alerting, and deployment health signals
- **arch-features** - Feature flags for decoupling deploy from release
- **arch-fitness** - Architecture checks enforced inside the pipeline
- **arch-migration** - Data and legacy system migration strategies

## DevOps Review Template

```markdown
## DevOps & Deployment Review: [System]

### Infrastructure
| Component | Tool | Status |
|-----------|------|--------|

### CI/CD Pipeline
| Stage | Tool | Duration | Success Rate |
|-------|------|----------|--------------|

### Deployment
- Strategy: [Blue-Green/Canary/Rolling]
- Rollback time: [Time]

### DORA Metrics
| Metric | Current | Target |
|--------|---------|--------|

### Security
| Concern | Implementation | Verified |
|---------|---------------|----------|

### Recommendations
1. [Improvement]
```
