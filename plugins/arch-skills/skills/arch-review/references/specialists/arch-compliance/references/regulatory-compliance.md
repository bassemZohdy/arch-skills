# Regulatory Compliance Reference

## GDPR Key Requirements

| Requirement | Description | Implementation |
|-------------|-------------|----------------|
| **Lawful basis** | Valid reason for processing | Consent, contract, legitimate interest |
| **Purpose limitation** | Specific, explicit purposes | Privacy policy, data mapping |
| **Data minimization** | Only necessary data | Field validation, retention policies |
| **Storage limitation** | No longer than needed | Automated deletion, retention schedules |
| **Data subject rights** | Access, rectification, erasure | Self-service portal, API |
| **Data protection by design** | Privacy from start | Privacy by design, default settings |
| **Breach notification** | Determine recipient, risk threshold and deadline under Articles 33–34 | Incident response plan |

Under [GDPR Articles 33–34](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng),
controllers notify the authority without undue delay and, where feasible, within
72 hours of awareness, unless risk to individuals is unlikely; explain delays.
Processors notify controllers without undue delay. High-risk breaches normally
require notifying affected people without undue delay, subject to Article 34 exceptions.

### GDPR Article 25 - Privacy by Design

1. Implement appropriate technical measures
2. Integrate data protection into processing activities
3. Apply data protection principles
4. Implement necessary safeguards

## HIPAA Key Requirements

| Category | Requirements |
|----------|-------------|
| **Technical** | Access controls, audit trails, encryption, integrity controls |
| **Administrative** | Risk analysis, training, policies, contingency plan |
| **Physical** | Facility access, workstation security, device controls |

## PCI DSS Requirements

| Requirement | Description |
|-------------|-------------|
| **Build secure networks** | Network security controls, secure configurations |
| **Protect account data** | Minimize storage, strong cryptography in storage and transit |
| **Maintain vulnerability mgmt** | Anti-malware, secure software development, patching |
| **Implement strong access** | Unique IDs, physical access control |
| **Monitor networks** | Track, monitor, audit |
| **Maintain policy** | Information security policy |

## SOC 2 Trust Criteria

| Criteria | Focus | Controls |
|----------|-------|----------|
| **Security** | Unauthorized access protection | Access controls, monitoring |
| **Availability** | System operational | Redundancy, disaster recovery |
| **Processing Integrity** | Complete, accurate processing | Validation, reconciliation |
| **Confidentiality** | Protected information | Encryption, access control |
| **Privacy** | Personal information handling | Consent, data minimization |

## Audit Trail Best Practices

### What to Log

| Event Type | Examples |
|------------|----------|
| **Authentication** | Login, logout, failed attempts |
| **Authorization** | Permission changes, access denials |
| **Data Access** | Read, write, delete operations |
| **Configuration** | System changes, setting updates |
| **Business Events** | Orders, payments, refunds |

### Log Format (JSON)

```json
{
  "timestamp": "2024-01-15T10:30:00Z",
  "event": "user.login",
  "userId": "123",
  "ip": "192.168.1.1",
  "result": "success",
  "details": {"method": "password"}
}
```

### Log Retention

| Obligation family | Record-specific retention decision |
|------------|-------------------|
| GDPR | Purpose-dependent |
| HIPAA | Identify the required documentation class; six-year documentation rules are not a blanket audit-log/medical-record retention rule |
| PCI DSS | Verify the adopted edition and applicable audit-log requirement, including immediate availability |
| SOX | Identify applicable financial/audit record obligations with the responsible authority; no blanket application-log duration |

## Data Classification

| Level | Description | Controls |
|-------|-------------|----------|
| **Public** | Publicly readable | Integrity, availability and controlled writes |
| **Internal** | Business use only | Access control |
| **Confidential** | Sensitive data | Encryption, audit |
| **Restricted** | Highly sensitive | Strict controls, MFA |

## Retention evidence

[45 CFR 164.316](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.316)
specifies retention for required Security Rule documentation. Identify the actual
record class and applicable policy before applying that period to logs or medical
records. Retention and erasure decisions need a documented applicability owner.
