# REST Patterns Reference

## Resource Naming

- Use nouns, not verbs
- Use plural for collections
- Use hierarchical paths for relationships

```
/users/{id}/orders/{id}/items
```

## HTTP Methods

| Method | Idempotent | Safe | Use Case |
|--------|------------|------|----------|
| GET | Yes | Yes | Read |
| POST | No | No | Create |
| PUT | Yes | No | Full update |
| PATCH | Not guaranteed | No | Partial update; define retry semantics |
| DELETE | Yes | No | Remove |

## Status Codes

| Code | Meaning | Use |
|------|---------|-----|
| 200 | OK | Success |
| 201 | Created | Resource created |
| 204 | No Content | Success, no body |
| 400 | Bad Request | Validation error |
| 401 | Unauthorized | Auth required |
| 403 | Forbidden | No permission |
| 404 | Not Found | Resource missing |
| 409 | Conflict | State conflict |
| 429 | Too Many Requests | Rate limit |

## Pagination

```
GET /items?page=2&limit=20&sort=-createdAt

{
  "data": [...],
  "pagination": {
    "page": 2,
    "limit": 20,
    "total": 150,
    "hasMore": true
  }
}
```

## Versioning

- URI: `/v1/users` (recommended for public)
- Header: `Accept: application/vnd.api.v1+json`
- Query: `/users?version=1`

## Protocol evidence

Use [HTTP semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110.html)
and [PATCH semantics (RFC 5789)](https://www.rfc-editor.org/rfc/rfc5789.html).
Idempotence concerns intended server effects, not identical response codes; a
particular POST/PATCH operation may define safe retry behavior explicitly.
