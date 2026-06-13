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
| **Breach notification** | 72-hour notification | Incident response plan |

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
| **Build secure networks** | Firewalls, secure configurations |
| **Protect cardholder data** | Encryption, access control |
| **Maintain vulnerability mgmt** | Anti-virus, secure development |
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

| Regulation | Minimum Retention |
|------------|-------------------|
| GDPR | Purpose-dependent |
| HIPAA | 6 years |
| PCI DSS | 1 year |
| SOX | 7 years |

## Data Classification

| Level | Description | Controls |
|-------|-------------|----------|
| **Public** | No restrictions | None |
| **Internal** | Business use only | Access control |
| **Confidential** | Sensitive data | Encryption, audit |
| **Restricted** | Highly sensitive | Strict controls, MFA |
