---
name: arch-security
description: Design and review secure architectures with threat modeling, zero-trust controls, identity, supply-chain security, OWASP verification and compliance. Use when assessing security posture, hardening APIs and systems, protecting secrets, or reviewing SOC 2, GDPR, HIPAA or PCI DSS requirements.
---

# Security Architecture

Systematic approach to designing and reviewing secure architectures.

## DAP contribution

For a DAP invocation, read `framework/contribution-contract.md` from the outer
package root (the repository root in a source checkout). Keep standalone tasks
within their requested scope. Use `assets/review-template.md` and record threat/control IDs and selected standard edition, trust boundaries, residual risk, verification evidence and human security disposition.
Return evidence-linked proposals and VER plans, not invented approvals or delivery proof.

## Workflow

```
1. Identify Assets → What are we protecting?
2. Threat Model → What can go wrong? (STRIDE)
3. Assess Risk → How likely, impactful and evidenced?
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
2. Trace assets through processes, stores, data flows and trust boundaries;
   apply relevant STRIDE threats beyond the entry points
3. Document threats with severity

## Step 3: Risk Register

Use a documented, scenario-specific likelihood × impact rubric. Include
preconditions, affected assets, attack paths, existing controls, residual risk,
confidence and owner. Do not present a numeric score as objective truth or as a
substitute for a security decision.

| Likelihood | Impact | Disposition |
|------------|--------|-------------|
| High | High | Block or require explicit risk acceptance |
| High | Low / Medium | Mitigate, monitor and time-box residual risk |
| Low / Medium | High | Add defense-in-depth and verify recovery |
| Low | Low | Record rationale and monitor for change |

## Step 4: Security Patterns

### Authentication
- OpenID Connect for federated user authentication; OAuth 2.0 for delegated API authorization
- Multi-factor authentication (MFA)
- Passwordless (WebAuthn, FIDO2)
- Choose opaque sessions or JWT access tokens from revocation, client and threat requirements; protect refresh credentials and validate token purpose

### Authorization
- Role-Based Access Control (RBAC)
- Attribute-Based Access Control (ABAC)
- Policy-Based Access Control (PBAC)
- Principle of least privilege
- Deny by default and recheck resource/tenant permission on every access path,
  including background jobs, exports and support/admin operations.

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

### Supply Chain and Platform Security
- Pin and verify dependencies, base images, actions and model artifacts.
- Produce and verify SBOMs and build provenance for release artifacts.
- Keep secrets out of source, logs, prompts and telemetry; rotate and revoke them.
- Apply least privilege at workload, service-account and deployment boundaries.

## Step 5: OWASP Top 10:2025 Checklist

- [ ] A01:2025 Broken Access Control
- [ ] A02:2025 Security Misconfiguration
- [ ] A03:2025 Software Supply Chain Failures
- [ ] A04:2025 Cryptographic Failures
- [ ] A05:2025 Injection
- [ ] A06:2025 Insecure Design
- [ ] A07:2025 Authentication Failures
- [ ] A08:2025 Software or Data Integrity Failures
- [ ] A09:2025 Security Logging and Alerting Failures
- [ ] A10:2025 Mishandling of Exceptional Conditions

## Step 6: Compliance Requirements

| Standard | Scope | Key Requirements |
|----------|-------|------------------|
| **SOC 2** | Service organizations | Trust service criteria, audits |
| **GDPR** | Establishment/targeting/monitoring scope under Article 3 | Lawful processing, protection and rights |
| **HIPAA** | Covered entities/business associates and applicable PHI | Safeguards and applicable agreements |
| **PCI DSS** | Payment card data | Cardholder data protection |
| **ISO 27001** | Information security | ISMS implementation |

For control mapping, audit trails, and evidence collection, see **arch-compliance**.

For web-application verification, map controls to a pinned OWASP ASVS version;
for AI systems, add the current OWASP GenAI risk set to the threat model rather
than treating the general web Top 10 as sufficient.

## Examples

- Threat model a new public API using STRIDE and the OWASP Top 10.
- Review authorization for a multi-tenant SaaS app.
- Assess compliance requirements for a payment system handling card data.

## Common Gotchas

- Do not write generic "best practice" advice without naming the threat and the control.
- Separate authentication from authorization when analyzing failures.
- Treat logging and monitoring as security controls, not just operational concerns.
- Do not use DREAD or another universal score without documenting its scale, evidence and decision authority.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)
- `references/security-deep-dive.md` — Security Architecture Deep Dive
- `references/security-patterns.md` — Security Patterns Reference
- `references/threat-modeling.md` — Threat Modeling Reference

## Cross-skill handoff

Consume data flows, actors and trust boundaries from arch-data, arch-api and arch-integration. Distinguish user identity, workload identity and delegated authority;
validate issuer, audience, token purpose and tenant/resource authorization at each
boundary. Give arch-test negative authorization and revocation cases and arch-observability redacted security signals. OAuth authorization alone is not user
authentication; use an identity protocol such as OpenID Connect when needed.

## Related Skills

- **arch-compliance** - Regulatory requirements and audit trails
- **arch-api** - API-specific security controls
- **arch-ai** - Prompt injection and AI-specific threats
- **arch-devops** - Secrets management and pipeline security

- [OWASP ASVS](https://github.com/OWASP/ASVS) — Versioned application verification requirements
- [OWASP Top 10:2025](https://owasp.org/www-project-top-ten/) — Current web application risk categories
