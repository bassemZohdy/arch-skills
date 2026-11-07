# API Design Deep Dive

**Source:** OpenAPI 3.1, REST Maturity Model, GraphQL Best Practices

## REST Maturity Model

| Level | Description | Characteristics |
|-------|-------------|-----------------|
| **0** | HTTP | Using HTTP as transport |
| **1** | Resources | URI-based resources |
| **2** | HTTP Verbs | Proper HTTP methods |
| **3** | HATEOAS | Hypermedia links |

## API Design Principles

### Richardson Maturity Model

| Level | Characteristics |
|-------|-----------------|
| **Level 0** | Single URI, single method |
| **Level 1** | Multiple URIs (resources) |
| **Level 2** | HTTP methods (GET, POST, PUT, DELETE) |
| **Level 3** | HATEOAS (hypermedia) |

### REST Best Practices

| Practice | Description |
|----------|-------------|
| **Use nouns** | /users, not /getUsers |
| **Use HTTP methods** | GET, POST, PUT, DELETE |
| **Version APIs** | /v1/users, /v2/users |
| **Paginate** | ?page=1&limit=20 |
| **Filter** | ?status=active&sort=name |
| **Error handling** | Consistent error format; RFC 9457 Problem Details for HTTP APIs |

## OpenAPI 3.1 Structure

This example targets 3.1-compatible tooling. OpenAPI 3.2.0 (September 2025) is a
compatible feature release that adds, for example, hierarchical tags, streaming
media types and additional HTTP methods; adopt it only after the generators,
linters, gateways and documentation tools in the toolchain support it. Select a
supported edition from the [OpenAPI publication catalog](https://spec.openapis.org/oas/);
do not confuse the contract format version with the API's own release version.

```yaml
openapi: 3.1.0
info:
  title: API Title
  version: 1.0.0
paths:
  /resource/{id}:
    get:
      summary: Get resource
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Resource'
components:
  schemas:
    Resource:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
```

## GraphQL Best Practices

| Practice | Description |
|----------|-------------|
| **Schema-first** | Design schema before implementation |
| **Use queries for reads** | Query for reading data |
| **Use mutations for writes** | Mutation for changing data |
| **Use subscriptions** | Real-time updates |
| **Pagination** | Cursor-based pagination |
| **Error handling** | GraphQL error format |

## gRPC Best Practices

| Practice | Description |
|----------|-------------|
| **Protobuf syntax** | Choose proto3 or a supported [Edition](https://protobuf.dev/editions/overview/) for the compiler and runtime fleet |
| **Meaningful names** | Clear service/method names |
| **Streaming** | Use streaming for large data |
| **Error handling** | gRPC status codes |
| **Health checks** | Implement health service |

## API Versioning

| Strategy | Example | Pros | Cons |
|----------|---------|------|------|
| **URI** | /v1/users | Explicit | URL proliferation |
| **Header** | Accept: v1 | Clean URLs | Hidden |
| **Query** | ?version=1 | Simple | Messy |

## API Documentation Tools

| Tool | Description |
|------|-------------|
| **OpenAPI Generator** | Generate client SDKs |
| **Redocly** | Beautiful API docs |
| **Swagger UI** | Interactive API explorer |
| **Stoplight** | API design platform |
| **Postman** | API development |
