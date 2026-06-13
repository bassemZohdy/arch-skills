---
name: arch-devops
description: Guide DevOps and infrastructure architecture. Use when designing Infrastructure as Code, implementing configuration management, setting up Kubernetes clusters, or establishing DevOps practices.
---

# DevOps Architecture

Systematic approach to DevOps and infrastructure.

## Workflow

```
1. Define Infrastructure → What do we need?
2. Automate provisioning → IaC tools
3. Configure Management → Config as code
4. Implement CI/CD → Pipeline automation
5. Container Orchestration → Kubernetes
6. Monitor & Secure → Observability and security
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
| **Testing** | Validate before deploy |

## Step 2: Configuration Management

### Tools

| Tool | Approach | Use Case |
|------|----------|----------|
| **Ansible** | Agentless, SSH | Configuration, deployment |
| **Chef** | Agent-based | Configuration management |
| **Puppet** | Agent-based | Configuration management |
| **SaltStack** | Agent-based | Remote execution |

### Configuration Patterns

| Pattern | Description |
|---------|-------------|
| **Immutable Infrastructure** | Replace, don't modify |
| **Configuration as Code** | Version-controlled configs |
| **Secrets Management** | Vault, AWS Secrets Manager |
| **Feature Flags** | Runtime feature control |

## Step 3: Container Orchestration

### Kubernetes Architecture

| Component | Description |
|-----------|-------------|
| **Pod** | Smallest deployable unit |
| **Deployment** | Manages pod replicas |
| **Service** | Network endpoint for pods |
| **Ingress** | External access routing |
| **ConfigMap** | Configuration data |
| **Secret** | Sensitive configuration |

### Kubernetes Best Practices

| Practice | Description |
|----------|-------------|
| **Resource Limits** | Set CPU/memory limits |
| **Health Checks** | Liveness and readiness probes |
| **Rolling Updates** | Zero-downtime deployments |
| **Horizontal Scaling** | Auto-scaling based on metrics |
| **Network Policies** | Restrict pod communication |

## Step 4: CI/CD Pipeline

### Pipeline Stages

```
Code → Build → Test → Security → Stage → Deploy → Monitor
```

### Pipeline Tools

| Stage | Tools |
|-------|-------|
| **Version Control** | Git, GitHub, GitLab |
| **Build** | Maven, npm, Docker |
| **Test** | JUnit, pytest, Jest |
| **Security** | Snyk, Trivy, SonarQube |
| **Deploy** | ArgoCD, Flux, Jenkins |
| **Monitor** | Prometheus, Grafana |

## Step 5: GitOps

### GitOps Principles

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

## Step 6: Infrastructure Security

| Concern | Solution |
|---------|----------|
| **Secrets** | HashiCorp Vault, AWS Secrets Manager |
| **Network** | Network policies, security groups |
| **Image Scanning** | Trivy, Clair, Snyk |
| **Runtime Security** | Falco, Sysdig |
| **Compliance** | Open Policy Agent, Kyverno |

## DevOps Review Template

```markdown
## DevOps Review: [System]

### Infrastructure
| Component | Tool | Status |
|-----------|------|--------|

### CI/CD Pipeline
| Stage | Tool | Duration | Success Rate |
|-------|------|----------|--------------|

### Kubernetes
| Aspect | Configuration | Status |
|--------|--------------|--------|

### Security
| Concern | Implementation | Verified |
|---------|---------------|----------|

### Recommendations
1. [Improvement]
```
