# DevOps Practices Reference

**Source:** Kubernetes documentation, GitOps best practices

## Infrastructure as Code

| Tool | Type | Use Case |
|------|------|----------|
| **Terraform** | Multi-cloud | Infrastructure provisioning |
| **Pulumi** | Multi-cloud | IaC with programming languages |
| **CloudFormation** | AWS | AWS-specific provisioning |
| **Ansible** | Config mgmt | Configuration and deployment |

## IaC Best Practices

| Practice | Description |
|----------|-------------|
| **Version Control** | Store IaC in Git |
| **Modular Design** | Reusable modules |
| **State Management** | Remote state with locking |
| **Plan/Apply** | Review changes before apply |
| **Testing** | Validate before deploy |
| **Immutable Infrastructure** | Replace, don't modify |

## Kubernetes Architecture

### Core Components

| Component | Description |
|-----------|-------------|
| **Pod** | Smallest deployable unit |
| **Deployment** | Manages pod replicas |
| **Service** | Network endpoint for pods |
| **Ingress** | External access routing |
| **ConfigMap** | Configuration data |
| **Secret** | Sensitive configuration |
| **StatefulSet** | Stateful applications |
| **DaemonSet** | Node-level services |
| **Job/CronJob** | Batch workloads |

### Kubernetes Best Practices

| Practice | Description |
|----------|-------------|
| **Resource Limits** | Set CPU/memory requests and limits |
| **Health Checks** | Liveness, readiness, startup probes |
| **Rolling Updates** | Validate capacity, readiness, draining and mixed-version compatibility before claiming no downtime |
| **Horizontal Scaling** | HPA based on metrics |
| **Network Policies** | Restrict pod communication |
| **Pod Security Standards** | Enforce security policies |
| **RBAC** | Role-based access control |
| **Secrets Management** | External secrets operators |

### Kubernetes Objects

| Object | Purpose |
|--------|---------|
| **Namespace** | Resource isolation |
| **Label** | Resource organization |
| **Annotation** | Non-identifying metadata |
| **Finalizer** | Deletion prevention |
| **Owner Reference** | Garbage collection |

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

## Configuration Management

| Pattern | Description |
|---------|-------------|
| **Immutable Infrastructure** | Replace, don't modify |
| **Configuration as Code** | Version-controlled configs |
| **Secrets Management** | Vault, AWS Secrets Manager |
| **Feature Flags** | Runtime feature control |
| **Externalized Configuration** | Config outside code |

## CI/CD Pipeline

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

## Infrastructure Security

| Concern | Solution |
|---------|----------|
| **Secrets** | HashiCorp Vault, AWS Secrets Manager |
| **Network** | Network policies, security groups |
| **Image Scanning** | Trivy, Clair, Snyk |
| **Runtime Security** | Falco, Sysdig |
| **Compliance** | Open Policy Agent, Kyverno |
