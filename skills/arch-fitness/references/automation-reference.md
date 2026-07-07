# Architecture Automation Reference

## Automation Categories

| Category | Skills | Automation |
|----------|--------|------------|
| **Documentation** | arch-doc | Generate docs from code/specs |
| **Review** | arch-review | Automated review checks |
| **Testing** | arch-test, arch-fitness | Test automation |
| **Deployment** | arch-devops | CI/CD pipelines |
| **Infrastructure** | arch-cloud, arch-devops | IaC automation |
| **Monitoring** | arch-observability | Alert automation |
| **Cost** | arch-cost | Cost optimization automation |

## CI/CD Best Practices

| Practice | Description |
|----------|-------------|
| **Fast builds** | < 10 minutes target |
| **Parallel stages** | Run independent tests together |
| **Artifact immutability** | Same artifact across environments |
| **Automated rollback** | Quick recovery capability |
| **Feature flags** | Decouple deploy from release |

## Documentation Automation

| Source | Tool | Output |
|--------|------|--------|
| **API Specs** | OpenAPI Generator | Client SDKs |
| **Code Comments** | JSDoc, Javadoc | API Reference |
| **Database Schema** | SchemaSpy | ER Diagrams |
| **Architecture** | Structurizr | C4 Diagrams |

## Infrastructure Automation

| Tool | Use Case |
|------|----------|
| **Terraform** | Infrastructure provisioning |
| **Ansible** | Server configuration |
| **Pulumi** | IaC with code |
| **CloudFormation** | AWS provisioning |
