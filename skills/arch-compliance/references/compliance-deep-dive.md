# Compliance Deep Dive

**Source:** GDPR Text, HIPAA Rules, PCI DSS 4.0, SOC 2

## GDPR Comprehensive Guide

### Data Protection Principles (Article 5)

| Principle | Description | Implementation |
|-----------|-------------|----------------|
| **Lawfulness** | Valid legal basis | Consent, contract, legitimate interest |
| **Purpose Limitation** | Specific purposes | Privacy policy, data mapping |
| **Data Minimization** | Only necessary | Field validation, retention |
| **Accuracy** | Keep accurate | User self-service, validation |
| **Storage Limitation** | No longer needed | Retention policies, auto-delete |
| **Integrity & Confidentiality** | Secure processing | Encryption, access control |
| **Accountability** | Demonstrate compliance | Documentation, audits |

### Data Subject Rights

| Right | Description | Response Time |
|-------|-------------|---------------|
| **Access** | Know what data is held | 1 month |
| **Rectification** | Correct inaccurate data | 1 month |
| **Erasure** | Delete data | 1 month |
| **Portability** | Transfer data | 1 month |
| **Objection** | Object to processing | 1 month |
| **Restriction** | Restrict processing | 1 month |

### Privacy by Design (Article 25)

1. Implement appropriate technical measures
2. Integrate data protection into processing
3. Apply data protection principles
4. Implement necessary safeguards

## HIPAA Comprehensive Guide

### Protected Health Information (PHI)

- Names, dates, email addresses
- Medical records and history
- Insurance information
- Biometric identifiers
- Device identifiers

### Technical Safeguards

| Control | Description |
|---------|-------------|
| **Access Control** | Unique ID, emergency access, auto-logoff |
| **Audit Controls** | Record and examine access |
| **Integrity** | Prevent improper alteration |
| **Transmission Security** | Encrypt PHI in transit |

### Administrative Safeguards

- Risk analysis and management
- Workforce training
- Security incident procedures
- Contingency plan

### Physical Safeguards

- Facility access controls
- Workstation use and security
- Device and media controls

## PCI DSS 4.0

### Requirements

| Requirement | Description |
|-------------|-------------|
| **Build secure networks** | Firewalls, secure configs |
| **Protect cardholder data** | Encryption, access control |
| **Maintain vulnerability mgmt** | Anti-virus, secure development |
| **Implement strong access** | Unique IDs, physical access |
| **Monitor networks** | Track, monitor, audit |
| **Maintain policy** | Information security policy |

### Cardholder Data Environment

- Card numbers (PAN)
- Cardholder names
- Expiration dates
- Service codes

## SOC 2 Trust Criteria

| Criteria | Focus | Controls |
|----------|-------|----------|
| **Security** | Unauthorized access | Access controls, monitoring |
| **Availability** | System operational | Redundancy, DR |
| **Processing Integrity** | Complete processing | Validation, reconciliation |
| **Confidentiality** | Protected info | Encryption, access control |
| **Privacy** | Personal info handling | Consent, minimization |

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

| Regulation | Minimum |
|------------|---------|
| GDPR | Purpose-dependent |
| HIPAA | Identify the required documentation class; six-year documentation rules are not a blanket audit-log/medical-record retention rule |
| PCI DSS | Verify the adopted edition and applicable audit-log requirement, including immediate availability |
| SOX | Identify applicable financial/audit record obligations with the responsible authority; no blanket application-log duration |
