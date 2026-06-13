# Security Patterns Reference

## Authentication Patterns

| Pattern | Use Case | Complexity |
|---------|----------|------------|
| **OAuth 2.0** | Third-party auth | Medium |
| **OpenID Connect** | Identity layer on OAuth | Medium |
| **SAML** | Enterprise SSO | High |
| **JWT** | Stateless tokens | Low |
| **API Keys** | Service-to-service | Low |

## Authorization Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **RBAC** | Role-based access | Standard apps |
| **ABAC** | Attribute-based | Complex rules |
| **PBAC** | Policy-based | Fine-grained control |
| **ACL** | Access control lists | File systems |

## Data Protection

| Layer | Method | Standard |
|-------|--------|----------|
| **At Rest** | AES-256 | Database, files |
| **In Transit** | TLS 1.3 | Network |
| **In Use** | Confidential computing | Specialized |
| **Key Management** | HSM, KMS | AWS KMS, Azure Key Vault |

## API Security

- Rate limiting per client/IP
- Input validation and sanitization
- Output encoding
- CORS configuration
- Content Security Policy
