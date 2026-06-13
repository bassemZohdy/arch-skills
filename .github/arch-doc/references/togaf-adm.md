# TOGAF ADM Reference

The Open Group Architecture Framework (TOGAF) Architecture Development Method (ADM) provides a systematic approach to developing enterprise architectures.

## ADM Phases

### Preliminary Phase
**Purpose:** Define architecture capability, framework, and principles.

**Activities:**
- Define enterprise scope and boundaries
- Establish architecture principles
- Select and tailor framework
- Define governance structure

**Outputs:**
- Architecture principles
- Framework selection
- Governance model

### Phase A: Architecture Vision
**Purpose:** Establish project scope, constraints, and expectations.

**Activities:**
- Define target architecture vision
- Identify stakeholders and concerns
- Confirm and elaborate architecture principles
- Develop Statement of Architecture Work

**Key Artifacts:**
- Architecture Vision document
- Stakeholder map
- Statement of Architecture Work

### Phase B: Business Architecture
**Purpose:** Develop baseline and target business architecture.

**Activities:**
- Develop business architecture models
- Identify gaps between baseline and target
- Define candidate roadmap components

**Key Artifacts:**
- Business process models
- Organization decomposition
- Business use cases

**Example:**
```markdown
## Business Architecture Summary

### Current State
- Manual order processing
- Siloed departments
- Paper-based approvals

### Target State
- Automated workflows
- Integrated departments
- Digital approvals

### Gap Analysis
| Area | Current | Target | Gap |
|------|---------|--------|-----|
| Order Processing | Manual | Automated | New system needed |
| Approvals | Paper | Digital | Workflow engine |
```

### Phase C: Information Systems Architecture
**Purpose:** Develop data and application architectures.

**Sub-phases:**
- **C1: Data Architecture** - Logical and physical data models
- **C2: Application Architecture** - Application portfolio and interactions

**Key Artifacts:**
- Data entity/data component catalog
- Application portfolio
- Interface catalog

**Use C4 diagrams** to visualize application architecture.

### Phase D: Technology Architecture
**Purpose:** Define technology infrastructure and platform.

**Activities:**
- Map application components to technology
- Define platform standards
- Identify technology capabilities

**Key Artifacts:**
- Technology standards catalog
- Platform decomposition
- Deployment diagrams

**Use deployment diagrams** from `assets/mermaid-templates/deployment.mmd`.

### Phase E: Opportunities and Solutions
**Purpose:** Identify delivery vehicles and transition architectues.

**Activities:**
- Identify work packages
- Create implementation plan
- Define transition architectures

**Key Artifacts:**
- Implementation plan
- Transition architecture definitions
- Project portfolio

### Phase F: Migration Planning
**Purpose:** Develop detailed implementation plan.

**Activities:**
- Prioritize work packages
- Define migration phases
- Estimate costs and benefits

**Key Artifacts:**
- Migration plan
- Cost-benefit analysis
- Risk assessment

### Phase G: Implementation Governance
**Purpose:** Oversee implementation to ensure alignment.

**Activities:**
- Conduct architecture compliance reviews
- Monitor implementation progress
- Manage architecture contracts

**Key Artifacts:**
- Architecture compliance reports
- Architecture contracts
- Change requests

### Phase H: Architecture Change Management
**Purpose:** Monitor changes and manage architecture evolution.

**Activities:**
- Monitor technology changes
- Assess change impact
- Implement change governance

**Key Artifacts:**
- Change requests
- Architecture update reports
- New business requirements

### Requirements Management
**Purpose:** Manage requirements throughout ADM cycle.

**Activities:**
- Identify requirements
- Prioritize requirements
- Track requirements through ADM

## Architecture Principles

Define principles to guide decision-making:

```markdown
## Architecture Principles

### PRINCIPLE 1: Reuse Before Buy
**Statement:** Prefer existing solutions over new development.
**Rationale:** Reduces cost, time, and risk.
**Implications:** 
- Evaluate existing solutions first
- Document exceptions with justification

### PRINCIPLE 2: Data is an Asset
**Statement:** Data has value and must be managed accordingly.
**Rationale:** Data is critical for business operations and decisions.
**Implications:**
- Implement data governance
- Ensure data quality
- Define ownership

### PRINCIPLE 3: Interoperability
**Statement:** Systems should communicate through standard interfaces.
**Rationale:** Enables integration and flexibility.
**Implications:**
- Use standard protocols (REST, gRPC)
- Define API contracts
- Version APIs
```

## ADM Artifacts Summary

| Phase | Key Artifacts | C4 Equivalent |
|-------|---------------|---------------|
| A: Vision | Vision, Stakeholder Map | - |
| B: Business | Process Models | - |
| C: Information | Application Portfolio | Container Diagram |
| D: Technology | Platform Decomposition | Deployment Diagram |
| E: Solutions | Implementation Plan | - |
| F: Migration | Migration Plan | - |
| G: Governance | Compliance Reports | - |
| H: Change | Change Requests | - |

## TOGAF vs C4 Model

| Aspect | TOGAF | C4 Model |
|--------|-------|----------|
| Scope | Enterprise-wide | System-focused |
| Audience | Architects, management | Developers, technical |
| Depth | Broad, strategic | Deep, technical |
| Diagrams | Multiple standards | C4-specific |
| Best for | Governance, compliance | System documentation |

**Recommendation:** Use TOGAF for enterprise governance, C4 for system documentation within TOGAF artifacts.
