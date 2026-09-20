# Full architecture skills review

Date: 2026-09-20. Baseline: `277fc80` on `main`.
Scope: all 33 skill entry points, resource and skill connections, templates,
packaging, deterministic helpers, test runners, CI configuration and repository
documentation. This is a repository/content review with deterministic validation;
no live-model execution or production architecture certification is claimed.

## Verdict

The three-entry-point distribution and separate process/design assessments remain
useful. The baseline passed 65 tests, but those tests missed widespread external
link rot, disconnected supporting resources and permissive decision arithmetic.
The main improvement is making skills exchange concrete evidence and contracts,
while keeping narrow specialist requests independent of the full DAP process.

## Findings and implemented corrections

| ID | Priority | Finding | Correction |
| --- | --- | --- | --- |
| R01 | High | The external catalog changed its URL structure; many deep links returned 404. | Mapped all 297 legacy topic URLs to current topic routes using the publisher's source files and route algorithm. Preserved topic specificity and explicit mappings for renamed AI subjects. |
| R02 | High | DAR validation ignored unknown/missing cells, allowed empty score populations and derived totals from rounded rows. | Validate complete matrices, unique criterion/JSON keys, finite non-boolean values, exact alternative sets, Decimal products, pre-rounding totals/rankings, ties and sensitivity transfers. |
| R03 | High | Formal DAR template automatically exempted the status quo and included an inconsistent, pre-approved JSON example. | Apply gates per alternative, keep unknown eligibility pending, remove automatic exemptions and supply a consistent synthetic draft example tested by the helper. |
| R04 | Medium | Decision deep dive, decision math script and microservices deep dive were disconnected; the orchestrator's optional external guide was unreachable. | Connect resources from entry points and recursively check reachability. Document specialist-local helper paths separately from shared DAP scripts. |
| R05 | Medium | Related-skill lists named neighbors without describing usable outputs; review routed patterns to itself. | Add domain-specific handoffs to all 33 skills and route structural review to patterns/principles/anti-patterns. Clarify optional specialist availability in selected expert installations. |
| R06 | High | Guidance included misleading auth, retention, delivery and rollback simplifications. | Separate OAuth authorization from identity, identify record-specific retention, qualify messaging guarantees/compensation, and describe data-aware migration/rollback verification. Update duplicate references where identified. |
| R07 | Medium | Universal thresholds/prescriptions could bias design decisions. | Remove fixed mesh/team thresholds, universal API-versioning choices, one-assertion testing, five-user completeness and mandatory AI escalation order. Make criteria contextual and evidence-driven. |
| R08 | Medium | Fitness examples contained a self-referencing TypeScript variable and a timer with no call. | Replace TypeScript examples with documented dependency-cruiser configuration, identify real call/environment requirements and distinguish one timing sample from percentile evidence. |
| R09 | Medium | The accessibility focus trap omitted important behavior; contrast guidance omitted bold large text. | Replace the incomplete trap with implementation/verification requirements and correct the contrast/reflow guidance. |
| R10 | Medium | Interview instructions promised control over model turns and assumed unrestricted host forms. | Preserve prepared batches and deferred reconciliation while respecting actual host turn/control limits and built-in custom-answer fields. |
| R11 | Medium | Local checks did not cover repository Markdown anchors or prevent resource orphans. | Add offline link/anchor validation, resource traversal, known-skill validation, regression tests and integration into both test runners. Existing CI invokes those runners. |
| R12 | Medium | AWS App Mesh was listed as a normal new-design option; a referenced ASVS page and an ArchUnitTS owner spelling were stale. | Record the App Mesh retirement date, link ASVS to its authoritative repository, and correct the library URL. |

## Changes across all skills

| Skill | Strengthened reasoning and handoff |
| --- | --- |
| arch-accessibility | Criterion-level barriers, keyboard/focus/reflow evidence and legal applicability boundary |
| arch-ai | Retrieval/memory/cache tenant isolation, evaluation slices, tool budgets and independent pattern choice |
| arch-antipatterns | Confirm smells through observed cost/change coupling; distinguish deliberate transaction scripts |
| arch-api | Consumer compatibility, object authorization, concurrency, asynchronous completion and retry semantics |
| arch-cloud | Deployment ownership, quotas, control-plane dependencies, failure capacity and exit assumptions |
| arch-compliance | Obligation applicability, record classes, control evidence and retention authority |
| arch-cost | Low/base/high demand, total ownership cost and recovery/latency trade-offs |
| arch-data | Authoritative/derived data, transaction boundaries, deletion, replay and restore contracts |
| arch-ddd | Business invariants, domain versus integration events and context versus deployment boundaries |
| arch-decision | Edition-specific evidence, lifecycle assessment, hard gates and arithmetic correctness |
| arch-devops | Mixed-version rollout, draining, capacity, data-compatible rollback and release signals |
| arch-doc | Consistent baseline and vocabulary across views; complementary C4/arc42 usage and template discovery |
| arch-evaluate | Evidence-gap ownership, unavailable-runtime reporting and independent design-review routing |
| arch-event | Delivery/ordering scope, duplicate/out-of-order/crash/replay verification and compensation limits |
| arch-features | Stable assignment, tenant scope, unavailable flag-service behavior and experiment validity |
| arch-fitness | Protected decisions, violating fixtures, empty measurement populations and explicit manual checks |
| arch-frontend | Session/cache ownership, remote-module failure and security isolation boundaries |
| arch-governance | Proportionate authority, exceptions and measurable policy enforcement without mandatory boards |
| arch-integration | Owning-service authorization, retry ownership, identity and tool lifecycle |
| arch-metrics | Population/window/units, dependency counts, measurement limits and corrected chart label |
| arch-microservices | Independent lifecycle, mixed-version evidence, communication guarantees and monolith comparison |
| arch-migration | Writer ownership, reconciliation, irreversible steps and post-cutover data recovery |
| arch-observability | SLI definitions, histogram aggregation, missing telemetry and operational handoffs |
| arch-orchestrator | Evidence-based specialist routing, early cross-cutting constraints and realistic host interaction |
| arch-patterns | Compile-time versus runtime arrows, driving-adapter correction and justified layer policies |
| arch-perf | Arrival profiles, active concurrency, measured capacity curves and coordinated omission |
| arch-principles | Concrete change costs, useful abstraction seams and intentional shared-kernel trade-offs |
| arch-refactoring | Characterization/differential verification and separation of behavior changes from restructuring |
| arch-resilience | Retry amplification, propagated deadlines and tested recovery across external dependencies |
| arch-review | Applicable specialist selection, cross-domain contradictions and urgency-based remediation |
| arch-security | User/workload/delegated identities, audience/purpose checks and negative authorization tests |
| arch-test | Risk-to-verification mapping, failure/concurrency/version-skew coverage and coherent assertions |
| arch-usability | Observed versus heuristic evidence, research sampling, complete states and localization |

## Link audit and provenance

The initial GET audit checked 340 unique external URLs: 19 reachable, 256 returning
404/410, and 65 unverified. Of the failures, 255 were legacy Awesome Architecture
routes and one was the ASVS page. All 297 legacy catalog routes were migrated,
including routes whose initial probes timed out. There were no missing local
Markdown targets or anchors in the original 211 documents; the local problem was
resource discoverability and missing regression coverage, not missing files.

Route mappings are grounded in upstream revision
`686546eb1bb1167229d409b9e9eb996a882aeadc`, specifically `docs/` and
`web/src/lib/content.ts`, rather than guessed URL substitutions. Renamed topics
were resolved explicitly. The updated catalog's ACP topic means Agent Client
Protocol; it must not be labelled Agent Communication Protocol.

Machine-readable [link evidence](2026-09-20-link-evidence.json) records before/after
responses, unverified URLs and every route replacement. The follow-up full probe
of 337 URLs found 304 reachable, 0 broken and 33 unverified. Additional primary
links added during remediation are included in the same after set. Final totals:
309 reachable, 36 unverified, 0 broken.
403/429, timeouts and other transport failures remain unverified. Do not equate
source-route validation with a successful live request, or a 200 response with
correct/current content. Topic-hub resources were not recursively audited.

## Validation

- Baseline: 33 skills structurally valid and 65 unit tests passing after installing
  the repository's declared dependencies in the execution environment.
- Expanded suite: 84 tests pass, including link/anchor/resource regressions, DAR
  malformed/incomplete/non-finite/tie/rounding/sensitivity cases and isolated
  bundled-helper execution.
- All 33 skills pass structure and resource-reachability checks; descriptions
  remain above the repository's advisory heuristic threshold.
- Both default (3 entry points) and expert (33 entry points) profiles are built
  in isolated fresh directories and checked before delivery.
- The formal template's synthetic matrix and the existing DAR fixture both pass
  the decision helper; neither provides product-evaluation or approval evidence.
- Patch whitespace and Python compilation are checked locally. Hosted CI is
  reported separately on the pull request; local checks do not imply a hosted pass.

The DAP record schema, rubric and process scoring rules are unchanged. Existing
contract, lifecycle and package regressions continue to pass. These checks do not
prove human identity authenticity, model behavior or architecture fitness.

## Primary references used for corrections

- [Agent Skills specification](https://agentskills.io/specification): portable paths and progressive disclosure.
- [arc42 overview](https://arc42.org/overview/): architecture views, decisions and quality requirements.
- [HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110.html): intended effects and method semantics.
- [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html): access-token and flow security.
- [WCAG contrast guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html): large text and contrast conditions.
- [HIPAA documentation rule](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.316): specific documentation retention scope.
- [AWS App Mesh lifecycle notice](https://docs.aws.amazon.com/app-mesh/latest/userguide/what-is-app-mesh.html): September 30, 2026 end of support.
- [dependency-cruiser rule reference](https://github.com/sverweij/dependency-cruiser/blob/main/doc/rules-reference.md): executable dependency-rule configuration.

## Remaining boundaries

Run behavioral scenarios on the actual consuming hosts before claiming interview,
routing or review quality. Confirm organization-specific policies and approvals
with their owners. Recheck unverified external URLs from an environment that can
reach them; do not remove useful references simply because a probe is blocked.
See [TODO](../../TODO.md) for these adoption tasks.
