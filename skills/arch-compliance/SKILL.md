---
name: arch-compliance
description: "Design regulatory controls and auditability architecture. Use when implementing GDPR, HIPAA, SOC 2, PCI DSS, ISO 27001, CCPA or SOX controls, designing audit trails and retention, classifying data, or mapping versioned obligations to evidence. Use arch-governance for board, standards and exception processes."
---

# Compliance Architecture

Systematic approach to regulatory compliance and auditability.

## Workflow

```
1. Identify Regulations → What applies?
2. Map Requirements → What must we do?
3. Design Controls → How to comply?
4. Implement Audit Trails → Track all actions
5. Monitor → Continuous compliance
6. Report → Evidence for auditors
```

## Step 1: Regulatory Landscape

| Regulation | Scope | Key Requirements |
|------------|-------|------------------|
| **GDPR** | EU data subjects | Data protection, consent, rights |
| **HIPAA** | Health information | PHI protection, BAAs |
| **PCI DSS** | Payment card data | Cardholder data protection |
| **SOC 2** | Service organizations | Trust service criteria |
| **ISO 27001** | Information security | ISMS implementation |
| **CCPA** | California consumers | Privacy rights |
| **SOX** | Financial reporting | Internal controls |

Confirm the jurisdiction, effective date, scope, contractual obligations and
authoritative version before treating a regulation or framework as applicable.
Translate obligations into control objectives, owners, evidence sources,
frequency, retention and exception handling; do not treat a checklist as legal
advice or as proof of compliance.

## Step 2: GDPR Requirements

### Data Protection Principles

| Principle | Description |
|-----------|-------------|
| **Lawfulness** | Valid legal basis for processing |
| **Purpose Limitation** | Collect for specified purposes |
| **Data Minimization** | Only necessary data |
| **Accuracy** | Keep data accurate and up-to-date |
| **Storage Limitation** | Keep only as long as needed |
| **Integrity & Confidentiality** | Secure processing |
| **Accountability** | Demonstrate compliance |

### Data Subject Rights

| Right | Description | Implementation |
|-------|-------------|----------------|
| **Access** | Know what data is held | Data export |
| **Rectification** | Correct inaccurate data | Edit interface |
| **Erasure** | Delete data | Data deletion |
| **Portability** | Transfer data | Data export |
| **Objection** | Object to processing | Opt-out mechanism |

### Privacy by Design

- Data protection from design inception
- Default to most privacy-friendly settings
- Privacy as default, not opt-in

## Step 3: HIPAA Requirements

### Protected Health Information (PHI)

- Names, dates, email addresses
- Medical records and history
- Insurance information
- Biometric identifiers

### Technical Safeguards

| Control | Description |
|---------|-------------|
| **Access Control** | Unique user identification, emergency access |
| **Audit Controls** | Record and examine access |
| **Integrity** | Prevent improper alteration |
| **Transmission Security** | Encrypt PHI in transit |

### Administrative Safeguards

- Risk analysis and management
- Workforce training
- Security incident procedures
- Contingency plan

## Step 4: SOC 2 Trust Service Criteria

| Criteria | Description |
|----------|-------------|
| **Security** | Protection against unauthorized access |
| **Availability** | System operational and usable |
| **Processing Integrity** | System processing is complete and accurate |
| **Confidentiality** | Designated information is protected |
| **Privacy** | Personal information is collected and used appropriately |

## Step 5: Audit Trail Design

### What to Log

| Event Type | Examples |
|------------|----------|
| **Authentication** | Login, logout, failed attempts |
| **Authorization** | Permission changes, access denials |
| **Data Access** | Read, write, delete operations |
| **Configuration** | System changes, setting updates |
| **Business Events** | Orders, payments, refunds |

### Log Format

```json
{
  "timestamp": "2024-01-15T10:30:00Z",
  "event": "user.login",
  "userId": "123",
  "ip": "192.168.1.1",
  "userAgent": "Mozilla/5.0",
  "result": "success",
  "details": {
    "method": "password"
  }
}
```

### Log Retention

| Regulation | Minimum Retention |
|------------|-------------------|
| GDPR | Purpose-dependent |
| HIPAA | 6 years |
| PCI DSS | 1 year |
| SOX | 7 years |

Retention periods are examples, not universal minima. Resolve the applicable
law, regulator, contract, litigation hold, deletion requirement and business
need for each record class, then document the conflict-resolution authority.

## Step 6: Data Classification

| Level | Description | Controls |
|-------|-------------|----------|
| **Public** | No restrictions | None |
| **Internal** | Business use only | Access control |
| **Confidential** | Sensitive data | Encryption, audit |
| **Restricted** | Highly sensitive | Strict controls, MFA |

## Examples

- Map GDPR data subject rights to concrete features (export, deletion, consent).
- Design an audit trail that satisfies SOC 2 without logging PII into it.
- Scope PCI DSS by isolating cardholder data behind a tokenization boundary.

## Common Gotchas

- Logging sensitive data into audit trails creates a new compliance problem inside the solution.
- GDPR deletion must reach backups and downstream copies, not just the primary database.
- Compliance scope grows with data spread; minimize where regulated data lives to shrink audits.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)
- `references/compliance-deep-dive.md` — Compliance Deep Dive
- `references/regulatory-compliance.md` — Regulatory Compliance Reference

## Related Skills

- **arch-security** - Controls that compliance frameworks require
- **arch-data** - Classification, retention, lineage
- **arch-governance** - Processes that keep compliance continuous

## Compliance Review Template

```markdown
## Compliance Review: [System]

### Applicable Regulations
| Regulation | Applicability | Status |
|------------|---------------|--------|

### Data Inventory
| Data Type | Classification | Retention | Purpose |
|-----------|---------------|-----------|---------|

### Controls Assessment
| Control | Implemented | Verified | Evidence |
|---------|-------------|----------|----------|

### Audit Trail
- Logging: [Configured?]
- Retention: [Period]
- Access: [Who can view?]

### Recommendations
1. [Critical gap]
2. [High priority]
```
