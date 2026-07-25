---
name: arch-api
description: Design APIs and API governance. Use when designing REST, GraphQL, or gRPC APIs, authoring OpenAPI/Swagger contracts, setting API standards and style guides, implementing versioning, pagination, and error-handling conventions, planning deprecation, or creating API documentation and developer portals.
---

# API Design

Systematic approach to designing and governing APIs.

## Workflow

```
1. Define Consumers → Who will use this API?
2. Design Contract → What operations are needed?
3. Choose Style → REST, GraphQL, or gRPC?
4. Define Standards → Naming, versioning, errors
5. Document → OpenAPI/GraphQL schema
6. Govern → Linting, review, deprecation
```

## Step 1: API Style Selection

| Style | Best For | Trade-offs |
|-------|----------|------------|
| **REST** | CRUD, resource-oriented | Simple, widely supported |
| **GraphQL** | Complex queries, mobile | Flexible, single endpoint |
| **gRPC** | Internal services, performance | Binary, strongly typed |
| **WebSocket** | Real-time, bidirectional | Stateful, complex |

## Step 2: REST Design

### Resource Naming

```
GET    /users           → List users
POST   /users           → Create user
GET    /users/{id}      → Get user
PUT    /users/{id}      → Update user
DELETE /users/{id}      → Delete user
GET    /users/{id}/orders → List user's orders
```

### HTTP Methods

| Method | Idempotent | Safe | Use Case |
|--------|------------|------|----------|
| GET | Yes | Yes | Read |
| POST | No | No | Create |
| PUT | Yes | No | Full update |
| PATCH | No | No | Partial update |
| DELETE | Yes | No | Remove |

### Status Codes

| Code | Meaning | Use |
|------|---------|-----|
| 200 | OK | Success |
| 201 | Created | Resource created |
| 204 | No Content | Success, no body |
| 400 | Bad Request | Validation error |
| 401 | Unauthorized | Auth required |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource doesn't exist |
| 409 | Conflict | State conflict |
| 422 | Unprocessable | Business logic error |
| 429 | Too Many Requests | Rate limit |
| 500 | Internal Error | Server error |

### Pagination

```
GET /users?page=2&limit=20

Response:
{
  "data": [...],
  "pagination": {
    "page": 2,
    "limit": 20,
    "total": 150,
    "pages": 8
  }
}
```

## Step 3: GraphQL Design

### Schema Design

```graphql
type User {
  id: ID!
  name: String!
  email: String!
  orders: [Order!]!
}

type Query {
  user(id: ID!): User
  users(filter: UserFilter): [User!]!
}

type Mutation {
  createUser(input: CreateUserInput!): User!
  updateUser(id: ID!, input: UpdateUserInput!): User!
}
```

### GraphQL Best Practices

- Use input types for mutations
- Implement cursor-based pagination
- Add query complexity limits
- Use DataLoader for N+1 prevention

## Step 4: gRPC Design

### Service Definition

```protobuf
service UserService {
  rpc GetUser(GetUserRequest) returns (User);
  rpc ListUsers(ListUsersRequest) returns (ListUsersResponse);
  rpc CreateUser(CreateUserRequest) returns (User);
}

message User {
  string id = 1;
  string name = 2;
  string email = 3;
}
```

### gRPC Best Practices

- Use proto3 syntax
- Define meaningful error codes
- Implement health checks
- Use streaming for large data

## Step 5: API Versioning

| Strategy | Example | Pros | Cons |
|----------|---------|------|------|
| **URI** | /v1/users | Explicit | URL proliferation |
| **Header** | Accept: application/vnd.api.v1+json | Clean URLs | Hidden |
| **Query** | /users?version=1 | Simple | Messy |

**Recommendation:** URI versioning for public APIs, header for internal.

## Step 6: Error Handling

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input",
    "details": [
      {
        "field": "email",
        "message": "Must be valid email"
      }
    ]
  }
}
```

## Step 7: API Governance

- [ ] Naming conventions documented
- [ ] Versioning strategy defined
- [ ] Error format standardized
- [ ] Rate limiting configured
- [ ] Authentication/authorization implemented
- [ ] Documentation generated (OpenAPI)
- [ ] Linting rules configured
- [ ] Deprecation policy defined

## Examples

- Design a REST API for a multi-tenant invoicing system with cursor pagination.
- Choose between REST and gRPC for internal service-to-service calls.
- Define a deprecation policy and versioning strategy for a public API.

## Common Gotchas

- Breaking changes hide in behavior, not just schemas: stricter validation or changed defaults break clients too.
- Offset pagination degrades on large tables; prefer cursor-based for growing datasets.
- Do not expose internal domain models directly; API contracts outlive implementations.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)
- `references/api-deep-dive.md` — API Design Deep Dive
- `references/api-documentation.md` — API Documentation Best Practices
- `references/rest-patterns.md` — REST Patterns Reference

## Related Skills

- **arch-integration** - Gateways and cross-system contracts
- **arch-security** - AuthN/AuthZ and rate limiting for APIs
- **arch-event** - AsyncAPI and event contracts

## API Review Template

```markdown
## API Review: [API Name]

### Style
- Type: [REST/GraphQL/gRPC]
- Version: [Version]

### Endpoints
| Method | Path | Description |
|--------|------|-------------|

### Authentication
- Method: [OAuth/API Key/JWT]

### Rate Limiting
- Limit: [Requests per window]
- Window: [Time period]

### Documentation
- OpenAPI spec: [Link]
- Examples: [Link]
```
