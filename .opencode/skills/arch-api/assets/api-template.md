# API Design Template

## API Design: [API Name]

### Style
- Type: [REST/GraphQL/gRPC]
- Base URL: [URL]

### Endpoints
| Method | Path | Description | Auth |
|--------|------|-------------|------|

### Data Models
```json
{
  "ModelName": {
    "field": "type"
  }
}
```

### Error Format
```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Description"
  }
}
```

### Versioning
- Strategy: [URI/Header]
- Current version: [Version]
