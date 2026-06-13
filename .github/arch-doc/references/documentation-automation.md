# Documentation Automation Reference

## Documentation as Code

### Principles

1. **Version Control** - Store docs in Git
2. **Automated Generation** - Generate from code/specs
3. **Continuous Integration** - Build docs in CI/CD
4. **Single Source of Truth** - One place for each fact
5. **Review Process** - Review docs like code

### Tools

| Tool | Purpose |
|------|---------|
| **MkDocs** | Static site generator |
| **Docusaurus** | Documentation framework |
| **Sphinx** | Python documentation |
| **Jekyll** | Ruby static site |
| **Hugo** | Fast static site |

## Documentation Automation

### From Code

| Source | Tool | Output |
|--------|------|--------|
| **API Specs** | OpenAPI Generator | Client SDKs |
| **Code Comments** | JSDoc, Javadoc | API Reference |
| **Database Schema** | SchemaSpy | ER Diagrams |
| **Architecture** | Structurizr | C4 Diagrams |

### CI/CD Integration

```yaml
# GitHub Actions
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

## Documentation Quality

### Metrics

| Metric | Target |
|--------|--------|
| **Coverage** | 100% of public APIs |
| **Freshness** | Updated within 30 days |
| **Accuracy** | Matches implementation |
| **Completeness** | All sections filled |

### Review Checklist

- [ ] All sections complete
- [ ] Code examples tested
- [ ] Links verified
- [ ] Spelling checked
- [ ] Formatting consistent
