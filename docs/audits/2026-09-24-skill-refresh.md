# Skill freshness and validation review — 2026-09-24

## Scope and outcome

Fetched GitHub and fast-forwarded the clean checkout to
`46302c8d282151cb33af67082ea048a757e81225`, then made the authorized
follow-up changes in the working branch. Reviewed all 34 entrypoints, their
routing and contribution boundaries, supporting domain guidance and representative
templates. Rechecked time-sensitive claims against the primary sources below.
This is a dated maintenance review, not certification of every linked external
article, every code example or every host's behavior. No global skills were installed.

## Skill-by-skill disposition

“Retained” means no actionable change identified in this pass; it does not imply
live-model validation. Domain references remain progressively loaded resources.

| Skill | Disposition | Review result |
| --- | --- | --- |
| arch-accessibility | Updated | Color-only failure example now actually lacks a text alternative; retained WCAG 2.2 baseline. |
| arch-ai | Updated | Unknown tool-write outcomes require reconciliation; model confidence is not grounding evidence. |
| arch-antipatterns | Retained | Smells remain contextual indicators; remedies preserve incremental change and measured trade-offs. |
| arch-api | Updated | Fixed path-parameter example, distinct nested IDs and generator package; edition/tool compatibility replaces unconditional proto3 guidance. |
| arch-cloud | Updated | Added relocate to the seven migration strategies; distinguished event bus/stream; qualified provider pillars and savings examples. |
| arch-compliance | Updated | PCI DSS 4.0.1 reference, GDPR timing/conditions and PHI applicability; summaries are not complete compliance checklists. |
| arch-cost | Updated | FinOps technology scope extends beyond cloud; costs/savings depend on the actual model and utilization. |
| arch-data | Updated | Accuracy differs from validity; completeness includes missing records; star dimensions join directly to the fact. |
| arch-ddd | Updated | Transaction boundaries follow invariants; illustrative Python methods are syntactically valid and expose concurrency requirements. |
| arch-decision | Retained | Hard gates, evidence-linked scoring, sensitivity and formal/expedited templates remain consistent; mathematical validation covered offline. |
| arch-devops | Updated | Removed guaranteed downtime/instant rollback claims, centralized strategy comparison, clarified namespace/finalizer semantics. |
| arch-diagrams | Retained | C4 levels, baseline identity, negative paths and source/render evidence distinction remain appropriate. |
| arch-doc | Updated | ISO mappings labeled illustrative, security scenario no longer claims Top 10 compliance, stale deployment action and popularity count removed, test-schema example labeled illustrative. |
| arch-evaluate | Retained | Read-only assessment, exact scoring, freshness and authority boundaries match the implemented contracts. |
| arch-event | Updated | CQRS can share a database; eventual consistency belongs to asynchronous projections, not every CQRS design. |
| arch-features | Updated | Flags complement authorization; timing alone does not lower risk; permanent flags need ongoing ownership. |
| arch-fitness | Retained | Dependency rules, representative performance measurement and project-adopted gates remain explicit. |
| arch-frontend | Updated | Deployment boundaries, module loading and rendering are separate decisions that can coexist. |
| arch-governance | Updated | Example authorities, cadences and targets do not establish organization policy or agent approval rights. |
| arch-integration | Updated | Saga compensation is not atomic rollback; ordering has scope; mesh data planes vary; App Mesh is existing-system context. |
| arch-metrics | Updated | Thresholds/weights are illustrative; coverage is not debt or substitutability proof. |
| arch-microservices | Updated | Removed synchronous exactly-once implication and unsupported 80/20 claim; atomic deduplication, ordering and migration conditions are explicit. |
| arch-migration | Retained | Single authoritative writer, suppressed shadow effects and post-cutover recovery/reconciliation are already covered. |
| arch-observability | Updated | Corrected RED attribution and distinguished resource saturation from utilization. |
| arch-orchestrator | Retained | Scoped selection, requirements/authority preservation, targeted rework and explicit fallback remain consistent. |
| arch-patterns | Updated | Strict versus relaxed layer skipping is consistent across the reference. |
| arch-perf | Updated | Request and time budgets differ; emergency recovery remains possible; cache writes do not alone establish strong consistency; INP replaces obsolete TTI guidance. |
| arch-principles | Updated | Consistency/session guarantees are not a single linear ladder with automatic availability gains. |
| arch-refactoring | Retained | Incremental behavior preservation and characterization evidence remain central. |
| arch-resilience | Updated | Example settings are not universal defaults; bounded jitter, deadline/retry ownership and unknown-write handling are explicit. |
| arch-review | Updated | Restored all nine ATAM steps; version-controlled configuration is legitimate; removed stale upgrade example. |
| arch-security | Updated | Removed fixed DREAD attribution and mandatory template score; unkeyed checksums do not protect against malicious tampering; JWT is a format. |
| arch-test | Updated | Testing Trophy is distinct from the pyramid; removed mandated percentages and clarified mutation denominator and example gates. |
| arch-usability | Updated | Rate observed problems by frequency, impact and persistence; heuristic categories have no inherent severity. |

## Automation corrections

- Link scanning ignores hidden local skill directories while continuing
  to validate canonical documentation.
- Diagram exclusions are relative to the scan root: a checkout under `.cache`
  still yields its sources.
- The Unicode link fixture explicitly writes UTF-8 on Windows.
- The behavioral runner detects adapter/model/mode/generation changes across
  steps and repetitions. The comparator validates each execution identity and
  supports a package-only override without relaxing execution settings. Candidate
  errors cannot pass and unavailable evidence remains unavailable.
- Added positive resource-read assertions and two resource-dependent scenarios,
  plus three activation scenarios for the actual default profile entrypoints.
  There are now 277 scenarios across 40 manifests; these counts describe validated
  scenarios, not live executions.

## Tool independence and live evidence boundary

The final change contains portable content, package validation, observation
contracts and host-neutral scenarios. Integrations for individual coding tools
belong outside this repository. Resource identities do not encode installation
paths, and generation settings remain opaque adapter-supplied JSON.

A local host experiment completed a model turn but did not establish resource
reads or skill activation. It supplies no live-quality baseline. Tool-specific
experimental code, tests and setup guidance were removed from the product change;
local experiment files remain only in the ignored validation cache. The next
validation step must use an external adapter with real observations rather than
adding a dependency on a particular coding tool.

## Primary sources checked

| Topic | Primary source and result |
| --- | --- |
| Accessibility | [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) supports retaining the adopted baseline and non-color meaning. |
| API contracts | [OpenAPI catalog](https://spec.openapis.org/oas/), [Protobuf Editions](https://protobuf.dev/editions/overview/), [generator installation](https://openapi-generator.tech/docs/installation/) support compatibility-aware tooling. |
| Cloud and operations | [AWS seven strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html), [App Mesh lifecycle](https://docs.aws.amazon.com/app-mesh/latest/userguide/what-is-app-mesh.html), [DORA metrics](https://dora.dev/guides/dora-metrics/) checked. |
| Compliance | [PCI SSC library](https://www.pcisecuritystandards.org/document_library/), [GDPR Articles 12/33/34](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng), [HHS Privacy Rule summary](https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html) establish edition and applicability distinctions. |
| FinOps | [Framework technology categories](https://www.finops.org/framework/technology-categories/) and [principles](https://www.finops.org/framework/principles/) support technology-wide scope. |
| Distributed behavior | [AWS idempotency guidance](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/), [Microsoft CQRS](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs), [Jepsen consistency models](https://jepsen.io/consistency) support the corrected guarantees. |
| Documentation and review | [ISO 42010:2022 overview](https://www.iso.org/standard/74393.html) and [SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/) checked; no claim of full paid-standard conformance. |
| Web responsiveness | [INP](https://web.dev/articles/inp) and [TTI retirement](https://web.dev/articles/tti) support the metric update. |
| Testing and usability | [Testing Trophy author](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications) and [Nielsen severity ratings](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/) support the distinctions. |
| Security | [OWASP Top 10:2025](https://top10.owasp.org/2025/) remains awareness guidance; adopted ASVS criteria need separate verification. |

## Verification

- `./run-tests.ps1`: passed on native Windows Python 3.13, without a UTF-8
  environment override. Structural validation covered all 34 skills; unittest
  discovery ran 127 tests with one existing skip; scenario validation covered
  277 cases in 40 manifests. The logged call-budget error is an expected negative
  test, not a release failure.
- Fresh default (3 entrypoints) and expert (34 skills) packages built successfully
  under `.cache/tool-neutral-default` and `.cache/tool-neutral-expert`.
- Static Mermaid inventory: 33 sources, zero errors. Rendering was not executed.
- The installed skill-creator validator passed both edited entrypoints. Its own
  default-encoding read failed for the Unicode accessibility file; invoking that
  external validator with `python -X utf8` succeeded. No installed validator was modified.
- `git diff --check`: passed.
- Public-link recheck: 369 probed, 363 reachable, zero confirmed broken and six
  unverified (one HTTP 401, five HTTP 403); zero local-link errors. See
  [dated evidence](2026-09-24-link-recheck.json). Access denials remain unverified,
  not broken; reachability does not prove content freshness.

The repository documentation pass replaced stale coverage counts and universal
metric targets with a manifest-derived inventory and project-defined gates.
The new documentation test checks the per-skill scenario table against the YAML
manifests. This pass also removed remaining fixed metric bands from `arch-metrics`,
`arch-test`, `arch-review` and deployment guidance; the performance examples are
now explicitly illustrative.

## Next task

Validate the portable observation contract through external host adapters, then
run the resource-loading and default/expert activation scenarios with bounded
execution. Compare evidence across intended hosts and establish repeatable
baselines before adopting a live release threshold. Keep host integration code
and configuration outside the canonical project.
