# Skill freshness follow-up — 2026-11-06

## Scope and outcome

Fetched GitHub and fast-forwarded the working branch to `origin/main`
(`253fb50`, including the arch-evaluate calibration from
[2026-11-02](2026-11-02-arch-evaluate-calibration.md)). Reapplied the
uncommitted [2026-09-24 refresh](2026-09-24-skill-refresh.md) on top of it,
resolved four documentation conflicts and recomputed the scenario inventory:
329 scenarios in 41 manifests (323 explicit skill cases, 6 activation cases); a later research pass in the same day added two, for 331.

This pass reviewed the 2026-09-24 skill changes and the merged arch-evaluate
scoring rules. It then rechecked time-sensitive claims that had changed since
September. Skills not listed below were not changed in this pass.

## Changes

| Skill | Change |
| --- | --- |
| arch-integration | AWS App Mesh is now described as discontinued on September 30, 2026, and kept only as migration context. |
| arch-devops | Recorded the March 2026 retirement of the community Ingress NGINX controller. Gateway API is preferred for new routing designs. Commit-stage build time is described as a goal, not a fixed limit. |
| arch-api | RFC 9457 Problem Details (`application/problem+json`, obsoleting RFC 7807) is now the default HTTP error format, in the skill and template. OpenAPI 3.2.0 is noted as a compatible release, to adopt once the toolchain supports it. |
| arch-perf | Replaced "page load" budgets with Core Web Vitals (LCP, INP, CLS at p75) and labelled all budgets as examples. |
| arch-compliance | Added the EU AI Act, NIS2, EU DORA, the Cyber Resilience Act and the European Accessibility Act to the screening landscape, without fixed dates. Updated PCI DSS terms to version 4 wording. |
| arch-governance, arch-review, arch-doc, arch-fitness | Numeric targets in the references are labelled as organization-specific examples, or turned into template placeholders. |
| arch-microservices | Replaced the unsupported LOC, endpoint, table and team-size "rules of thumb" with signals based on ownership and cohesion. |
| arch-resilience | Hystrix is cited as a historical source in maintenance mode, not as a library to adopt. |

The `designs error handling` scenario in `tests/test-arch-api.yaml` now accepts
Problem Details vocabulary. It no longer requires the old `code`/`message`
envelope.

## Primary sources checked

| Topic | Source |
| --- | --- |
| App Mesh | [AWS App Mesh user guide](https://docs.aws.amazon.com/app-mesh/latest/userguide/what-is-app-mesh.html) |
| Ingress NGINX | [Kubernetes retirement notice](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/) |
| Error format | [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457) |
| OpenAPI | [OpenAPI publication catalog](https://spec.openapis.org/oas/) |
| Web vitals | [web.dev Core Web Vitals](https://web.dev/articles/vitals) |

The first pass deliberately encoded no EU applicability dates. The research
pass below added only dates confirmed by several sources, and skills still direct
users to the current official text.

## Web research pass

A wider search for standards and ecosystem changes since the 2026-09-24 review
led to these updates. Several were confirmed only by secondary sources. Those are
worded to point readers at the primary source and to require pinning the adopted
version.

| Skill | Finding | Update |
| --- | --- | --- |
| arch-ai | [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/) (ASI01-ASI10, December 2025). [MCP specification 2026-07-28](https://blog.modelcontextprotocol.io/posts/2026-07-28/) is stateless. [A2A v1.0](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year) is under the Linux Foundation. | Agentic threat rows, protocol-boundary guidance and per-request authorization. Added one scenario. |
| arch-security | NIST FIPS 203/204/205 are final. Draft NIST IR 8547 proposes deprecating RSA-2048/ECC-256 by 2030 and disallowing them after 2035. | Cryptographic agility and post-quantum readiness guidance. Added one scenario. |
| arch-compliance | [AI Act Digital Omnibus, Regulation (EU) 2026/1744](https://www.orrick.com/en/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes): high-risk obligations moved to December 2027 / August 2028. [CRA reporting](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting) has applied since 11 September 2026. | Landscape rows updated. |
| arch-accessibility | [EN 301 549 V4.1.1](https://accessible-eu-centre.ec.europa.eu/content-corner/news/european-accessibility-standard-en-301-549-has-been-updated-2026-09-07_en) adopts WCAG 2.2, but is not yet cited in the Official Journal. | Edition note added. |
| arch-features | OpenFeature (CNCF incubating) and its OFREP remote evaluation protocol. | Listed as a vendor-neutral evaluation API. |
| arch-event | [AsyncAPI 3.1.0](https://www.asyncapi.com/blog/release-notes-3.1.0) is non-breaking. CloudEvents 1.0.2 is still the latest specification. | Envelope and contract guidance. |
| arch-cost | [FOCUS 1.4](https://www.finops.org/insights/introducing-focus-1-4/) was ratified in June 2026. | Billing-data normalization guidance. |
| arch-devops | The [2025 DORA report](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) links AI adoption to higher throughput and higher instability, and adds an AI Capabilities Model. | Interpretation note added. |

The following were checked and left unchanged:

- **Already current:** OWASP Top 10:2025 (final), ASVS 5.0, SLSA v1.2, RFC 9700.
- **Still current with no successor yet:** PCI DSS 4.0.1 (a successor is in RFC) and ISO/IEC 27001:2022.
- **Still a draft:** SSDF 1.2.
- **Not version-pinned in the skills:** Gateway API (v1.6 current).
- **Already described as emerging:** OpenTelemetry profiles (public alpha).
- **Unverified claims:** reported 2026 Core Web Vitals threshold changes appeared only on low-authority sites.

## Full-project review follow-up

A same-day review of the scripts, tests, workflows, docs and all 34 entry points
produced fixes that are now applied:

- Link probe: truncated responses, non-200 success responses and cross-host
  redirects are unverified, not reachable or fatal. Four permanently moved URLs
  were updated.
- Mermaid check accepts directives, front matter and newer diagram types.
- DAP evidence locators must be a heading, JSON pointer or a quote of at least
  12 characters; lock cleanup, RTM error stream and subject-hash caching fixed.
- Scenario validation rejects keyword assertions that echo their prompt; 267
  such assertions in 35 manifests were rewritten to guidance-specific terms.
- Documentation counts for diagrams and manifests are now test-guarded; the
  duplicate skill-testing reference in arch-doc was removed; nine small skill
  content fixes were made. Link evidence is in
  [2026-11-06-link-recheck.json](2026-11-06-link-recheck.json).

## Verification

See the commands in [project status](../project-status.md). Offline checks,
package builds and `git diff --check` were run after these changes. Live model
and host behavior were not evaluated.
