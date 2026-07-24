---
name: arch-security
description: Design and review secure architectures with threat modeling, OWASP, authentication, authorization, and compliance. Use when assessing security posture, hardening APIs and systems, or reviewing SOC 2, GDPR, HIPAA, or PCI DSS requirements.
---

# Security Architecture

Systematic approach to designing and reviewing secure architectures.

## Workflow

```
1. Identify Assets → What are we protecting?
2. Threat Model → What can go wrong? (STRIDE)
3. Assess Risk → How likely and impactful? (DREAD)
4. Design Controls → How to mitigate?
5. Review Implementation → Are controls effective?
6. Document → Security architecture record
```

## Step 1: Identify Assets

Categorize what needs protection:

| Asset Type | Examples | Sensitivity |
|------------|----------|-------------|
| **Data** | PII, credentials, secrets, health records | Critical |
| **Services** | APIs, payment processing, auth systems | High |
| **Infrastructure** | Servers, databases, networks | High |
| **Code** | Source code, algorithms, IP | Medium |
| **Users** | Accounts, sessions, tokens | High |

## Step 2: Threat Model (STRIDE)

| Threat | Description | Example |
|--------|-------------|---------|
| **S**poofing | Impersonating someone | Fake login, phishing |
| **T**ampering | Modifying data | SQL injection, XSS |
| **R**epudiation | Denying actions | Log forgery, no audit trail |
| **I**nformation Disclosure | Leaking data | Data breach, verbose errors |
| **D**enial of Service | Availability attack | DDoS, resource exhaustion |
| **E**levation of Privilege | Gaining unauthorized access | Privilege escalation, JWT forgery |

**Process:**
1. List all entry points (APIs, UI, files)
2. Apply STRIDE to each entry point
3. Document threats with severity

## Step 3: Risk Assessment (DREAD)

| Factor | Question | Scale |
|--------|----------|-------|
| **D**amage | How bad if exploited? | 1-10 |
| **R**eproducibility | How easy to reproduce? | 1-10 |
| **E**xploitability | How easy to exploit? | 1-10 |
| **A**ffected users | How many impacted? | 1-10 |
| **D**iscoverability | How easy to find? | 1-10 |

**Risk Score:** (D + R + E + A + D) / 5

| Score | Severity | Action |
|-------|----------|--------|
| 8-10 | Critical | Fix immediately |
| 6-7 | High | Fix before release |
| 4-5 | Medium | Plan fix |
| 1-3 | Low | Accept or monitor |

## Step 4: Security Patterns

### Authentication
- OAuth 2.0 / OpenID Connect
- Multi-factor authentication (MFA)
- Passwordless (WebAuthn, FIDO2)
- JWT with short expiry + refresh tokens

### Authorization
- Role-Based Access Control (RBAC)
- Attribute-Based Access Control (ABAC)
- Policy-Based Access Control (PBAC)
- Principle of least privilege

### Data Protection
- Encryption at rest (AES-256)
- Encryption in transit (TLS 1.3)
- Key management (HSM, KMS)
- Data masking and tokenization

### API Security
- Rate limiting and throttling
- API key management
- OAuth 2.0 flows
- Input validation and sanitization

## Step 5: OWASP Top 10 Checklist

- [ ] A01: Broken Access Control
- [ ] A02: Cryptographic Failures
- [ ] A03: Injection (SQL, XSS, LDAP)
- [ ] A04: Insecure Design
- [ ] A05: Security Misconfiguration
- [ ] A06: Vulnerable Components
- [ ] A07: Authentication Failures
- [ ] A08: Data Integrity Failures
- [ ] A09: Logging and Monitoring Failures
- [ ] A10: Server-Side Request Forgery

## Step 6: Compliance Requirements

| Standard | Scope | Key Requirements |
|----------|-------|------------------|
| **SOC 2** | Service organizations | Trust service criteria, audits |
| **GDPR** | EU data subjects | Data protection, consent, rights |
| **HIPAA** | Health information | PHI protection, BAAs |
| **PCI DSS** | Payment card data | Cardholder data protection |
| **ISO 27001** | Information security | ISMS implementation |

For control mapping, audit trails, and evidence collection, see **arch-compliance**.

## Examples

- Threat model a new public API using STRIDE and the OWASP Top 10.
- Review authorization for a multi-tenant SaaS app.
- Assess compliance requirements for a payment system handling card data.

## Common Gotchas

- Do not write generic "best practice" advice without naming the threat and the control.
- Separate authentication from authorization when analyzing failures.
- Treat logging and monitoring as security controls, not just operational concerns.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)

## Related Skills

- **arch-compliance** - Regulatory requirements and audit trails
- **arch-api** - API-specific security controls
- **arch-ai** - Prompt injection and AI-specific threats
- **arch-devops** - Secrets management and pipeline security

## Security Review Template

```markdown
## Security Review: [System Name]

### Assets Protected
- [List assets]

### Threats Identified
| ID | Threat | STRIDE | Risk (DREAD) | Mitigation |
|----|--------|--------|--------------|------------|

### Controls Implemented
- [ ] Authentication: [Pattern used]
- [ ] Authorization: [Pattern used]
- [ ] Encryption: [At rest/in transit]
- [ ] Logging: [Audit trail]

### OWASP Compliance
- [ ] All Top 10 addressed

### Recommendations
1. [Critical finding]
2. [High finding]
```
