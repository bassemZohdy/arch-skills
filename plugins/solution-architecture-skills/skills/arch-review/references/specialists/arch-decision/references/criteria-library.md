# Criteria Library — Reusable Evaluation Criteria Bundles

Copy criteria from this library into your DAR document's Section 4 (Evaluation Criteria).
Adjust weights to sum to 100 for your specific context.

These are prompts for evidence collection, not preset rankings. Turn mandatory
license, residency, security and production-use requirements into eligibility gates.
Score only eligible editions and their actual deployment/support model. Do not
award incumbent contracts or team familiarity in a greenfield comparison unless
the evaluation scope explicitly includes those factors. Replace illustrative
weights, thresholds and time horizons with the decision owner's criteria.

---

## Bundle 1: Cloud Service Evaluation

Use when selecting between cloud services or SaaS products.

| # | Criterion | Typical Weight | What **5** looks like | What **1** looks like |
|---|-----------|:--------------:|-----------------------|-----------------------|
| C1 | Security & Compliance | 25–30 | SOC 2 Type II, ISO 27001, GDPR DPA included; pen test reports published | No compliance certifications; self-audited only |
| C2 | Data Residency & Sovereignty | 15–20 | Configurable region lock; contractual data residency guarantee | Data may be processed in any region with no guarantee |
| C3 | API Quality & SDK Coverage | 15–20 | OpenAPI spec; SDKs for 5+ languages; <1 hour quickstart | Contract/tooling poorly fits required consumers; costly integration |
| C4 | Pricing Predictability | 10–15 | Transparent per-unit pricing with calculator; free tier for dev | Opaque pricing; enterprise-only; no public price list |
| C5 | Operational Model | 10–15 | Meets adopted operating model and SLO with evidenced ownership | Unfunded operational burden or failure to meet required SLO |
| C6 | Vendor Lock-in Risk | 5–10 | Open standards; easy export; multi-cloud portable | Proprietary APIs; data export is painful or impossible |
| C7 | Support & SLA | 5–10 | Dedicated support; <1 hr response for P1; community forum | Community-only support; no SLA; best-effort response |

---

## Bundle 2: Open Source Library Selection

Use when choosing between open source libraries or frameworks.

| # | Criterion | Typical Weight | What **5** looks like | What **1** looks like |
|---|-----------|:--------------:|-----------------------|-----------------------|
| C1 | Community & Momentum | 25–30 | Evidenced maintainer capacity, release quality and issue response | Unresolved maintenance/security risk or insufficient continuity |
| C2 | API Stability & Documentation | 20–25 | Semantic versioning; zero breaking changes in minors; excellent API docs | No versioning policy; frequent breaking changes; docs are auto-generated only |
| C3 | Performance & Benchmarks | 15–20 | Published benchmarks; meets throughput/latency targets with headroom | No benchmarks; performance unknown until production |
| C4 | Licence Compatibility | 10–15 | License and dependency obligations compatible with intended use | Incompatible or unresolved obligations for intended distribution/service use |
| C5 | Security Track Record | 10–15 | Timely vulnerability response, maintained versions and verifiable releases | Multiple unpatched CVEs; no security contact; unsigned |
| C6 | Integration with Our Stack | 5–10 | Drop-in compatible with our framework/language; existing team expertise | Requires adapter layer; new language or runtime; no team experience |

---

## Bundle 3: Build vs Buy

Use when deciding whether to build a solution in-house or buy/adopt an existing one.

| # | Criterion | Typical Weight | What **5** looks like | What **1** looks like |
|---|-----------|:--------------:|-----------------------|-----------------------|
| C1 | Time to Value | 20–25 | Delivery in <2 weeks; immediate ROI | 6+ months development; ROI uncertain |
| C2 | Total Cost of Ownership (3-year) | 20–25 | Clear cost model; < $50K total over 3 years | Hidden costs; > $200K total; cost grows non-linearly |
| C3 | Customisation & Control | 15–20 | Full source code; unlimited customisation; no vendor dependency | Black box; customisation via support tickets only |
| C4 | Maintenance Burden | 15–20 | Measured sustainable maintenance effort including vendor upgrades | Dedicated 0.5+ FTE for maintenance; on-call required |
| C5 | Strategic Fit | 10–15 | Core to our product; builds competitive advantage | Commodity capability; no differentiation |
| C6 | Risk of Vendor Failure | 5–10 | Established vendor; multiple exit paths; data is portable | Startup vendor; single point of failure; data locked in |
| C7 | Team Skill Alignment | 5–10 | Team has deep expertise in required technology | Team would need to hire or train for unfamiliar tech |

---

## Bundle 4: Infrastructure & Tooling Selection

Use when choosing infrastructure components (databases, message brokers, observability stacks).

| # | Criterion | Typical Weight | What **5** looks like | What **1** looks like |
|---|-----------|:--------------:|-----------------------|-----------------------|
| C1 | Performance & Scalability | 25–30 | Handles projected 10× growth; sub-ms latency; horizontal scaling | Hits ceiling at 2× current load; vertical scaling only |
| C2 | Operational Complexity | 20–25 | Single binary or managed service; minimal config; self-healing | Complex cluster setup; external dependencies; dedicated ops required |
| C3 | Observability & Debugging | 15–20 | Built-in metrics/tracing; Prometheus/OpenTelemetry compatible | Black box; logs only; no structured telemetry |
| C4 | Team Familiarity | 10–15 | Team has production experience; zero ramp-up | Entirely new technology; 6+ months to proficiency |
| C5 | Ecosystem & Integrations | 10–15 | Rich client libraries; broad tool integration | Limited integrations; custom adapters required |
| C6 | Cost | 5–10 | Open source or low-cost managed; fits budget with headroom | Expensive licensing or large infra footprint |

---

## Bundle 5: Security Tool Selection

Use when evaluating security tools (SAST, DAST, SIEM, WAF, etc.).

| # | Criterion | Typical Weight | What **5** looks like | What **1** looks like |
|---|-----------|:--------------:|-----------------------|-----------------------|
| C1 | Detection Accuracy | 25–30 | <5% false positive rate; covers OWASP Top 10; real-time alerts | >30% false positive rate; misses known vulnerability classes |
| C2 | Integration & Deployment | 20–25 | CI/CD native; agentless option; API-first; 1-day rollout | Requires agents on every host; 4+ week rollout; manual configuration |
| C3 | Compliance Coverage | 15–20 | Built-in reports for SOC 2, PCI-DSS, HIPAA, ISO 27001 | No compliance reporting; manual evidence collection required |
| C4 | Alert Triage Workflow | 10–15 | Risk-scored alerts; auto-suppression of known false positives; ticketing integration | Untriaged flood of alerts; no prioritisation; manual review required |
| C5 | Vendor Security Posture | 10–15 | SOC 2 Type II; bug bounty program; transparent incident history | No security certifications; history of breaches |
| C6 | Cost per Asset | 5–10 | Per-agent or per-scan pricing that scales linearly; free tier for small teams | Per-seat pricing; expensive at scale; no free evaluation |

---

## How to Use This Library

1. **Select the bundle** that best matches your decision category
2. **Copy the criteria** into your DAR document's Section 4
3. **Adjust weights** to reflect your team's priorities (must sum to 100)
4. **Remove or merge** criteria that overlap
5. **Customise** the "What 5 looks like" and "What 1 looks like" columns

### Weight Adjustment Tips

- Small team → Increase **Operational Complexity** / **Maintenance Burden** weight
- Regulated industry → Gate mandatory **Security & Compliance** requirements before scoring optional benefits
- Speed critical → Increase **Time to Value** weight
- Early-stage startup → Increase **Cost**, decrease **Scalability** weight
- Hard to reverse → Increase **Vendor Lock-in Risk** weight
