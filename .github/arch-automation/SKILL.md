---
name: arch-automation
description: Guide architecture automation across all skills. Use when setting up CI/CD pipelines for architecture validation, automating documentation generation, implementing infrastructure as code, or establishing architecture automation workflows.
---

# Architecture Automation

Orchestrate automation across all architecture skills.

## Workflow

```
1. Identify Automation Needs → What to automate?
2. Select Tools → Which tools to use?
3. Implement Pipelines → CI/CD integration
4. Configure Monitoring → Track automation health
5. Optimize → Improve automation efficiency
6. Govern → Ensure automation compliance
```

## Step 1: Automation Categories

| Category | Skills | Automation |
|----------|--------|------------|
| **Documentation** | arch-doc | Generate docs from code/specs |
| **Review** | arch-review | Automated review checks |
| **Testing** | arch-test, arch-fitness | Test automation |
| **Deployment** | arch-deployment, arch-devops | CI/CD pipelines |
| **Infrastructure** | arch-cloud, arch-devops | IaC automation |
| **Monitoring** | arch-observability | Alert automation |
| **Cost** | arch-cost | Cost optimization automation |

## Step 2: CI/CD Pipeline Automation

### Pipeline Stages

```
Code → Build → Test → Security → Stage → Deploy → Monitor
```

### Architecture Validation in CI

| Stage | Validation | Tools |
|-------|------------|-------|
| **Lint** | Code style, architecture rules | ESLint, ArchUnit |
| **Test** | Unit, integration, contract | Jest, Pact |
| **Security** | Vulnerability scanning | Snyk, Trivy |
| **Architecture** | Pattern compliance | Custom scripts |
| **Documentation** | Doc generation | MkDocs, Docusaurus |

### GitHub Actions Template

```yaml
name: Architecture Validation

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run architecture tests
        run: ./run-tests.sh
      
      - name: Validate documentation
        run: npm run build:docs
      
      - name: Security scan
        run: npm audit
```

## Step 3: Documentation Automation

### Generate from Code

| Source | Tool | Output |
|--------|------|--------|
| **API Specs** | OpenAPI Generator | Client SDKs |
| **Code Comments** | JSDoc, Javadoc | API Reference |
| **Database Schema** | SchemaSpy | ER Diagrams |
| **Architecture** | Structurizr | C4 Diagrams |

### Documentation Pipeline

```yaml
- name: Build docs
  run: |
    npm run build:docs
    npm run test:docs
    
- name: Deploy docs
  uses: peaceiris/actions-gh-pages@v3
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}
    publish_dir: ./docs
```

## Step 4: Infrastructure Automation

### IaC Pipeline

```yaml
- name: Terraform Plan
  run: terraform plan -out=tfplan

- name: Terraform Apply
  run: terraform apply tfplan
  if: github.ref == 'refs/heads/main'
```

### Configuration Management

| Tool | Use Case |
|------|----------|
| **Ansible** | Server configuration |
| **Terraform** | Infrastructure provisioning |
| **Pulumi** | IaC with code |

## Step 5: Monitoring Automation

### Alert Automation

```yaml
- name: Create alert
  run: |
    aws cloudwatch put-metric-alarm \
      --alarm-name "HighErrorRate" \
      --metric-name "Errors" \
      --threshold 5
```

### Health Check Automation

```yaml
- name: Health check
  run: |
    curl -f https://api.example.com/health || exit 1
```

## Step 6: Cost Automation

### Cost Alerts

```yaml
- name: Budget alert
  run: |
    aws budgets create-budget \
      --budget '{"budgetLimit":{"amount":"1000","unit":"USD"}}'
```

### Optimization Automation

```yaml
- name: Right-size instances
  run: |
    aws compute-optimizer get-recommendation \
      --resource-type EC2Instance
```

## Automation Review Template

```markdown
## Automation Review: [System]

### Automation Coverage
| Category | Automated | Coverage |
|----------|-----------|----------|

### CI/CD Pipeline
| Stage | Tool | Status |
|-------|------|--------|

### Documentation
| Source | Tool | Output |
|--------|------|--------|

### Infrastructure
| Component | Tool | Status |
|-----------|------|--------|

### Recommendations
1. [Improvement]
```
