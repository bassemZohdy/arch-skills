---
name: arch-deployment
description: Guide deployment architecture and release engineering. Use when designing CI/CD pipelines, planning deployment strategies, implementing blue-green deployments, or establishing release management processes.
---

# Deployment Architecture

Systematic approach to deployment and release engineering.

## Workflow

```
1. Define Pipeline → Build, test, deploy stages
2. Choose Strategy → Blue-green, canary, rolling
3. Plan Environments → Dev, staging, production
4. Implement Automation → CI/CD pipelines
5. Monitor → Deployment health
6. Rollback → Recovery procedures
```

## Step 1: CI/CD Pipeline

### Pipeline Stages

```
Code → Build → Test → Security → Stage → Deploy → Monitor
```

| Stage | Purpose | Tools |
|-------|---------|-------|
| **Code** | Version control | Git |
| **Build** | Compile, package | Maven, npm, Docker |
| **Test** | Automated tests | JUnit, pytest, Jest |
| **Security** | Vulnerability scan | Snyk, Trivy, SonarQube |
| **Stage** | Deploy to staging | Terraform, Ansible |
| **Deploy** | Deploy to production | Kubernetes, ECS |
| **Monitor** | Health checks | Prometheus, Datadog |

### Pipeline Principles

- **Fast feedback**: Fail early, fail fast
- **Parallel execution**: Run independent stages in parallel
- **Artifact immutability**: Same artifact across environments
- **Environment parity**: Staging ≈ Production

## Step 2: Deployment Strategies

### Blue-Green Deployment

```
Production (Blue) → Load Balancer ← Production (Green)
                    [Switch]
```

| Pros | Cons |
|------|------|
| Zero downtime | Double infrastructure |
| Easy rollback | Cost |
| Full testing | Complexity |

### Canary Deployment

```
Production → 95% ← Current Version
           → 5%  ← New Version (canary)
```

| Pros | Cons |
|------|------|
| Gradual rollout | Complex routing |
| Risk mitigation | Monitoring overhead |
| Quick rollback | Slower full deployment |

### Rolling Deployment

```
Batch 1: [New] [New] [Old] [Old]
Batch 2: [New] [New] [New] [Old]
Batch 3: [New] [New] [New] [New]
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

| Pros | Cons |
|------|------|
| Simple | Downtime |
| Clean state | Risk |

## Step 3: Environment Strategy

### Environment Types

| Environment | Purpose | Data |
|-------------|---------|------|
| **Local** | Developer workstations | Mock/local |
| **Development** | Integration testing | Test data |
| **Staging** | Pre-production validation | Production-like |
| **Production** | Live system | Real data |

### Environment Configuration

- **Infrastructure as Code**: Terraform, Pulumi
- **Configuration Management**: Ansible, Chef
- **Secrets Management**: Vault, AWS Secrets Manager
- **Feature Flags**: LaunchDarkly, Unleash

## Step 4: Release Management

### Release Types

| Type | Description | Frequency |
|------|-------------|-----------|
| **Major** | Breaking changes | Quarterly/Yearly |
| **Minor** | New features | Monthly/Weekly |
| **Patch** | Bug fixes | As needed |
| **Hotfix** | Critical fixes | Immediate |

### Release Process

1. **Feature freeze**: No new features
2. **Code freeze**: No code changes
3. **Testing**: Final validation
4. **Approval**: Release sign-off
5. **Deployment**: Execute rollout
6. **Monitoring**: Watch for issues
7. **Communication**: Notify stakeholders

## Step 5: Rollback Strategies

### Rollback Triggers

- Error rate exceeds threshold
- Performance degradation
- Critical bug discovered
- Security vulnerability

### Rollback Types

| Type | Description | Speed |
|------|-------------|-------|
| **Code rollback** | Revert to previous version | Fast |
| **Database rollback** | Revert schema changes | Slow |
| **Configuration rollback** | Revert config changes | Fast |
| **Full rollback** | Complete system revert | Variable |

## Step 6: Deployment Automation

### GitOps Pattern

```
Git Push → Controller → Diff → Apply → Kubernetes
```

**Benefits:**
- Audit trail in Git
- Automated reconciliation
- Easy rollback

### Infrastructure as Code

```yaml
# Terraform example
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  
  tags = {
    Name = "WebServer"
  }
}
```

## Deployment Review Template

```markdown
## Deployment Review: [System]

### Pipeline
- Stages: [List]
- Average duration: [Time]
- Success rate: [Percentage]

### Strategy
- Type: [Blue-Green/Canary/Rolling]
- Rollback time: [Time]

### Environments
| Environment | Purpose | Status |
|-------------|---------|--------|

### Recommendations
1. [Improvement]
```
