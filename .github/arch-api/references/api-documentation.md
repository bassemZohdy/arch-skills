# API Documentation Best Practices

## OpenAPI/Swagger Specification

### OpenAPI 3.1 Structure

```yaml
openapi: 3.1.0
info:
  title: API Title
  version: 1.0.0
paths:
  /resource:
    get:
      summary: Get resource
      responses:
        '200':
          description: Success
components:
  schemas:
    Resource:
      type: object
      properties:
        id:
          type: string
```

### Documentation Best Practices

| Practice | Description |
|----------|-------------|
| **Version API** | Use URI or header versioning |
| **Document Errors** | Include all error responses |
| **Provide Examples** | Request/response examples |
| **Use Descriptive Names** | Clear endpoint naming |
| **Document Auth** | Security requirements |
| **Rate Limiting** | Document limits |

## Documentation as Code

### Tools

| Tool | Description |
|------|-------------|
| **OpenAPI Generator** | Generate client SDKs |
| **Redocly** | Beautiful API docs |
| **Swagger UI** | Interactive API explorer |
| **Stoplight** | API design platform |

### Automation

```yaml
# GitHub Actions workflow
- name: Generate API docs
  run: |
    npx @redocly/cli build-docs openapi.yaml
    npx openapi-generator generate -i openapi.yaml -g html
```

## Documentation Quality Checklist

- [ ] All endpoints documented
- [ ] All parameters described
- [ ] All responses documented
- [ ] Error responses included
- [ ] Examples provided
- [ ] Authentication documented
- [ ] Rate limits documented
- [ ] Versioning documented
