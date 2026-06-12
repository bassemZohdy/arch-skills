# DevOps Practices Reference

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

## Kubernetes Best Practices

| Practice | Description |
|----------|-------------|
| **Resource Limits** | Set CPU/memory limits |
| **Health Checks** | Liveness and readiness probes |
| **Rolling Updates** | Zero-downtime deployments |
| **Horizontal Scaling** | Auto-scaling based on metrics |
| **Network Policies** | Restrict pod communication |

## GitOps Principles

1. **Declarative** - System state described declaratively
2. **Versioned** - Entire state stored in Git
3. **Automated** - Changes applied automatically
4. **Self-healing** - System reconciles to desired state
