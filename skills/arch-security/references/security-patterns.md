# Security Patterns Reference

## Authentication Patterns

| Pattern | Use Case | Complexity |
|---------|----------|------------|
| **OAuth 2.0** | Delegated authorization; not an identity protocol | Medium |
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

## Identity and delegation

Apply the [OAuth security BCP (RFC 9700)](https://www.rfc-editor.org/rfc/rfc9700.html)
to the chosen client/flow. Use OIDC for user authentication, scoped access tokens
for authorization, and independent workload credentials where appropriate. Do
not forward a user token to an audience it was not issued for. Define revocation,
session lifetime, tenant isolation and delegated action limits.
