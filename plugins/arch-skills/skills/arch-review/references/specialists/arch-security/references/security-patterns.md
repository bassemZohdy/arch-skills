# Security Patterns Reference

## Authentication Patterns

| Pattern | Use Case | Complexity |
|---------|----------|------------|
| **OAuth 2.0** | Delegated authorization; not an identity protocol | Medium |
| **OpenID Connect** | Identity layer on OAuth | Medium |
| **SAML** | Enterprise SSO | High |
| **JWT** | Token format, not an authentication protocol; validate issuer, audience, algorithm, expiry and revocation strategy | Context-dependent |
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
| **Post-quantum readiness** | Crypto inventory, hybrid key exchange, then PQC signatures | NIST FIPS 203/204/205 |

Prioritize post-quantum migration by data lifetime ("harvest now, decrypt later")
and by signing roots with long validity. NIST's transition guidance (IR 8547, a
draft at the time of review) proposes deprecating RSA-2048 and ECC P-256 by 2030
and disallowing them after 2035; confirm the current final dates and any sector or
government mandate before setting the project's timeline. Keep algorithms
configurable so a later change does not require redesign.

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
