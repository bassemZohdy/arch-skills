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
