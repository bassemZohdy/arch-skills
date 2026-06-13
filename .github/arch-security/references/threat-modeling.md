# Threat Modeling Reference

## STRIDE Threat Model

| Threat | Description | Mitigation |
|--------|-------------|------------|
| **Spoofing** | Identity impersonation | MFA, certificates, tokens |
| **Tampering** | Data modification | HMAC, signing, checksums |
| **Repudiation** | Denying actions | Audit logging, non-repudiation |
| **Info Disclosure** | Data leakage | Encryption, access control |
| **Denial of Service** | Availability attack | Rate limiting, DDoS protection |
| **Elevation of Privilege** | Unauthorized access | Least privilege, RBAC |

## DREAD Risk Assessment

| Factor | Question | 1-3 (Low) | 4-6 (Medium) | 7-10 (High) |
|--------|----------|-----------|--------------|-------------|
| Damage | Impact if exploited | Minimal | Data exposure | Complete compromise |
| Reproducibility | How easy to reproduce | Random | Some conditions | Always works |
| Exploitability | Skill needed | Advanced | Moderate | Script kiddie |
| Affected Users | Scope | Few | Some | All |
| Discoverability | How easy to find | Obscure | Some research | Public knowledge |

## OWASP ASVS 5.0 Verification Levels

| Level | Description | Use Case |
|-------|-------------|----------|
| **Level 1** | Minimum | Applications handling low-value data |
| **Level 2** | Standard | Most web applications |
| **Level 3** | Advanced | Applications handling sensitive data |

## OWASP Top 10 2025

| # | Risk | Description |
|---|------|-------------|
| A01 | Broken Access Control | Unauthorized action execution |
| A02 | Cryptographic Failures | Sensitive data exposure |
| A03 | Injection | SQL, NoSQL, OS command injection |
| A04 | Insecure Design | Missing security architecture |
| A05 | Security Misconfiguration | Default configurations |
| A06 | Vulnerable Components | Known vulnerabilities |
| A07 | Authentication Failures | Broken authentication |
| A08 | Software and Data Integrity | Supply chain attacks |
| A09 | Security Logging Failures | Insufficient logging |
| A10 | Server-Side Request Forgery | SSRF attacks |

## Attack Trees

```
Goal: Steal User Data
├── Bypass Authentication
│   ├── Brute Force
│   ├── Credential Stuffing
│   └── Session Hijacking
├── Exploit Vulnerabilities
│   ├── SQL Injection
│   ├── XSS
│   └── SSRF
└── Social Engineering
    ├── Phishing
    └── Pretexting
```

## Security Design Principles

1. **Least Privilege** - Grant minimum required access
2. **Defense in Depth** - Multiple security layers
3. **Fail Secure** - Default to secure state
4. **Separation of Duties** - Divide critical operations
5. **Keep it Simple** - Simplicity reduces attack surface
6. **Zero Trust** - Never trust, always verify
