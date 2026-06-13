# Security Architecture Deep Dive

**Source:** OWASP ASVS 5.0, NIST Cybersecurity Framework

## Security Architecture Principles

| Principle | Description | Implementation |
|-----------|-------------|----------------|
| **Defense in Depth** | Multiple security layers | WAF + Auth + Encryption |
| **Least Privilege** | Minimum required access | RBAC, just-in-time access |
| **Zero Trust** | Never trust, always verify | mTLS, continuous auth |
| **Fail Secure** | Default to secure state | Deny by default |
| **Separation of Duties** | Divide critical operations | Multi-person approval |
| **Economy of Mechanism** | Keep design simple | Minimal attack surface |
| **Complete Mediation** | Check every access | Authorization on every request |
| **Open Design** | Don't rely on obscurity | Security through transparency |
| **Psychological Acceptability** | Security shouldn't hinder usability | SSO, passwordless |
| **Weakest Link** | Strengthen the weakest point | Holistic security |

## OWASP ASVS 5.0 Verification Levels

| Level | Description | Use Case | Requirements |
|-------|-------------|----------|--------------|
| **Level 1** | Minimum | Low-value data apps | Basic security controls |
| **Level 2** | Standard | Most web applications | Standard security controls |
| **Level 3** | Advanced | Sensitive data apps | Advanced security controls |

## Threat Modeling Frameworks

### STRIDE + DREAD

| Threat | DREAD Factor | Mitigation |
|--------|--------------|------------|
| **Spoofing** | Damage: High | MFA, certificates |
| **Tampering** | Reproducibility: Medium | HMAC, signing |
| **Repudiation** | Discoverability: Low | Audit logging |
| **Info Disclosure** | Damage: High | Encryption, access control |
| **DoS** | Affected Users: High | Rate limiting, DDoS protection |
| **EoP** | Exploitability: Medium | Least privilege, RBAC |

### Attack Trees

```
Goal: Compromise System
├── Physical Access
│   ├── Theft
│   └── Social Engineering
├── Network Access
│   ├── Man-in-the-Middle
│   └── DNS Spoofing
├── Application Attack
│   ├── Injection (SQL, XSS)
│   ├── Broken Authentication
│   └── Insecure Deserialization
└── Social Engineering
    ├── Phishing
    └── Pretexting
```

## Security Testing Checklist

### Static Analysis
- [ ] SAST tools configured (SonarQube, Checkmarx)
- [ ] Dependency scanning (Snyk, OWASP Dependency-Check)
- [ ] Secret detection (GitLeaks, TruffleHog)
- [ ] Container scanning (Trivy, Clair)

### Dynamic Analysis
- [ ] DAST tools configured (OWASP ZAP, Burp Suite)
- [ ] Penetration testing scheduled
- [ ] Vulnerability scanning automated
- [ ] Security headers validated

### Compliance Checks
- [ ] OWASP Top 10 addressed
- [ ] ASVS level verified
- [ ] Privacy regulations compliant
- [ ] Security logging complete
