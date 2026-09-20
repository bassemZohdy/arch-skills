# Skill-by-skill and end-to-end review

Date: 2026-09-20. Scope: all 34 canonical SKILL.md entry points, selected connected
references, public catalogs, packaging, behavioral transport, DAP snapshot/evaluation/
publication paths and maintained operating documentation. Automated resource/link
checks cover the complete repository; this is not a claim that every external
reference or every model behavior has been semantically verified.

The starting offline suite passed 100 tests. New regression probes reproduced
defects that it missed. This review adds targeted corrections and regression
coverage, not a guarantee that no undiscovered defect remains. Earlier dated
reviews retain their historical counts and findings.

## Implementation findings and fixes

| ID | Concern | Correction and evidence |
| --- | --- | --- |
| E2E-01 | The expanded manual smoke suite needed 16 calls but allowed 15; evaluator-only examples allowed 6 but needed 7 | Corrected workflow/docs, added no-call plan command and a regression reading the actual workflow selection |
| E2E-02 | Default interview instructions contradicted focused diagram/public review routing | Added precedence in entry point and workflow reference, kept three public packages, added typed routing candidates |
| E2E-03 | Custom RTM output could overwrite an archived evaluation summary | Existing custom destinations and symlink aliases are refused; regression verifies archive bytes remain unchanged |
| E2E-04 | Generated manifest paths could use aliases; evidence pointers accepted negative/noncanonical array indices | Enforced canonical paths, resolved generated-path exclusion and strict pointer tokens; evaluator patch version 2.0.1 |
| E2E-05 | Packages omitted the repository license and lacked source-nested-output preflight | Bundle/hash LICENSE; reject nested outputs, missing entries and canonical-source symlinks before building |
| E2E-06 | Malformed provider envelopes could escape structured error handling; null usage broke otherwise valid responses | Validate choices/text/usage, preserve unknown token usage, test malformed responses; adapter version 1.0.1 |
| E2E-07 | Current inventory/version documentation could drift from code | Add automated current-count/version checks; update current docs and keep TODO limited to unfinished work |

The description limit of 1024 characters was already enforced. This review adds
a boundary test rather than claiming it introduced that validation. Redundant DAP
boilerplate was removed from 27 skills; domain-specific contribution requirements
remain. Line-wrapped skill identifiers were repaired. Detailed resources remain
on-demand; no host-specific runtime or new global installation was added.

## One-by-one skill changes

| Skill | Improvement |
| --- | --- |
| [arch-accessibility](../../skills/arch-accessibility/SKILL.md) | Corrected article/landmark semantics, axe-core classification and brittle screen-reader shortcut guidance. |
| [arch-ai](../../skills/arch-ai/SKILL.md) | Separate token cost from total cost; reconcile unknown write outcomes; use verified completion rather than self-reported confidence. |
| [arch-antipatterns](../../skills/arch-antipatterns/SKILL.md) | Diagnosis does not authorize remediation; a smell needs context and demonstrated impact. |
| [arch-api](../../skills/arch-api/SKILL.md) | Require object/field authorization, bounded GraphQL work and RPC deadline/cancellation semantics. |
| [arch-cloud](../../skills/arch-cloud/SKILL.md) | Separate architecture/IaC proposals from authorized provisioning and cost exposure. |
| [arch-compliance](../../skills/arch-compliance/SKILL.md) | Separate legal, contractual, certification and attestation claims; preserve unknown evidence. |
| [arch-cost](../../skills/arch-cost/SKILL.md) | Use comparable total-cost horizons; avoid overlapping savings and budget-alert/spending-cap confusion. |
| [arch-data](../../skills/arch-data/SKILL.md) | Distinguish validity from accuracy; specify late data, replay, checkpoints and backfill completeness. |
| [arch-ddd](../../skills/arch-ddd/SKILL.md) | Protect aggregate invariants against concurrent writers; make repository stub bodies syntactically explicit. |
| [arch-decision](../../skills/arch-decision/SKILL.md) | Align zero-to-five score anchors; keep unknown evidence and excluded/provisional alternatives visible. |
| [arch-devops](../../skills/arch-devops/SKILL.md) | Correct reversed rollback arrow; remove automatic zero-downtime/stateful-rollback promises. |
| [arch-diagrams](../../skills/arch-diagrams/SKILL.md) | Preserve review-only inputs; distinguish authored source from executed renderer validation. |
| [arch-doc](../../skills/arch-doc/SKILL.md) | Do not invent accepted historical ADR rationale; bound fallback when diagram specialists are unavailable. |
| [arch-evaluate](../../skills/arch-evaluate/SKILL.md) | Retain actual result/exit evidence; a crashed evaluator is not a computed zero score. |
| [arch-event](../../skills/arch-event/SKILL.md) | Atomically couple deduplication and business updates; separate CQRS from eventual consistency; repair invalid JSON example. |
| [arch-features](../../skills/arch-features/SKILL.md) | Distinguish temporary release flags from continuing operational kill switches and entitlement policies. |
| [arch-fitness](../../skills/arch-fitness/SKILL.md) | Distinguish rule violations from checker errors, missing data and zero-check runs. |
| [arch-frontend](../../skills/arch-frontend/SKILL.md) | Separate deployment, composition and rendering axes rather than treating them as exclusive alternatives. |
| [arch-governance](../../skills/arch-governance/SKILL.md) | Use adopted authority, quorum and conflict rules; chair titles do not grant unilateral approval. |
| [arch-integration](../../skills/arch-integration/SKILL.md) | Bound stream ordering and saga guarantees; avoid arbitrary mediation thresholds. |
| [arch-metrics](../../skills/arch-metrics/SKILL.md) | Use behavioral contract assertions, not line coverage, as substitutability evidence. |
| [arch-microservices](../../skills/arch-microservices/SKILL.md) | Separate logical data ownership from physical servers and legitimate derived replicas. |
| [arch-migration](../../skills/arch-migration/SKILL.md) | Suppress duplicate shadow-run effects; replace unsafe restore/rollback shortcuts with data-safe recovery. |
| [arch-observability](../../skills/arch-observability/SKILL.md) | Remove unnecessary identifiers from the sample log; cover telemetry loss and bounded backpressure. |
| [arch-orchestrator](../../skills/arch-orchestrator/SKILL.md) | Give bounded artifact/review routing precedence over full interview preparation; shorten discovery metadata. |
| [arch-patterns](../../skills/arch-patterns/SKILL.md) | Make the selection matrix candidate guidance, not an automatic mesh/saga prescription. |
| [arch-perf](../../skills/arch-perf/SKILL.md) | Separate request/time error budgets and remove guaranteed linear-scaling claims. |
| [arch-principles](../../skills/arch-principles/SKILL.md) | Correct inverted yes/no checklist logic while preserving purposeful single-implementation seams. |
| [arch-refactoring](../../skills/arch-refactoring/SKILL.md) | An interface alone does not remove a package cycle; preserve observable contracts and inspect dependency direction. |
| [arch-resilience](../../skills/arch-resilience/SKILL.md) | Require authorized fault injection; treat write timeouts as unknown and preserve authorization in fallbacks. |
| [arch-review](../../skills/arch-review/SKILL.md) | Cover omitted cross-cutting specialist routes; avoid treating every simple CRUD model as defective. |
| [arch-security](../../skills/arch-security/SKILL.md) | Threat-model stores/flows/boundaries as well as entry points; include background/export authorization. |
| [arch-test](../../skills/arch-test/SKILL.md) | Isolate E2E data and accounts; suppress real external side effects without explicit execution authority. |
| [arch-usability](../../skills/arch-usability/SKILL.md) | Keep visible labels; specify optimistic recovery; distinguish SUS scores from satisfaction percentages. |

Every skill has a targeted typed regression candidate in
[the boundary manifest](../../tests/test-skill-boundaries.yaml). Five positive
controls complement the 34 initial cases. Scenario validity is tested offline;
their response quality is not established until actual model runs are recorded.
These are narrow decision checks, not comprehensive benchmarks.

Connected references were corrected for C4 scope/density, atomic event
deduplication, CQRS consistency, shadow-run side effects, migration recovery,
deployment assumptions and installed module paths. Other references were retained
where no evidenced correction was selected in this pass.

## Executed validation

| Check | Result | What it establishes |
| --- | --- | --- |
| Offline wrapper | 119 unit/integration tests passed locally | Deterministic implementation and regression behavior |
| Skill structure/resource reachability | 34 skills, zero errors | Metadata, local resources, catalogs and line limits |
| Scenario validation | 272 definitions across 38 manifests | Valid manifests, typed assertions and known skill coverage |
| Budget preflight | 8 smoke scenarios / 16 calls; 39 boundary scenarios / 39 calls | Selection fits stated limits; no model invoked |
| Default/expert builds | 3 / 34 discoverable entry points | Portable contents, hashes and selectively loaded modules |
| Packaged CLI lifecycle | Passed from an unrelated working directory | Checkpoint resume, read-only evaluation, RTM, two publications, preserved history, freshness and stale-baseline rejection |
| External recheck | Latest inventory: 351 URLs; 301 reachable, zero confirmed broken, 50 unverified | Reachability at the recorded probe time, not source truth |
| Diagram inventory | 33 Mermaid files/fences pass static header/hash checks; manual pinned renderer workflow added | Source validity is not rendered-output evidence |
| Patch whitespace | Clean | No whitespace errors |

The packaged CLI lifecycle executes real Python commands against synthetic
schema-2 evidence. Existing tests also exercise blocking review, incomplete
interview, concurrent/interrupted checkpoint, missing source/verification and
other failed gates. Synthetic approval identities are not authenticated humans.

[Latest external recheck evidence](2026-09-20-link-recheck-latest.json) retains
the unresolved URLs and timestamp. The previous 347-URL report remains historical;
the current inventory includes this review's supporting source links. None of the
50 unverified responses is classified as a confirmed broken link.

## Remaining boundaries

No model endpoint/model is configured in this workspace. No live model calls,
actual host activation or human-review integration was exercised. Content edits
and a shorter discovery description are not measured improvements in task success,
latency or token consumption. Live comparison/calibration remains required.

There is no configured diagram renderer in this review environment. The new
static inventory covers 33 Mermaid files/fences and the manual workflow provides
pinned Mermaid rendering when GitHub can download its headless browser; its
successful SVG/report artifact is still required before claiming rendered
evidence. PlantUML/Draw.io jobs remain optional if those formats become release
requirements. Host adapters, real-project adoption and unverified URL follow-up
remain in [TODO](../../TODO.md). No substantive runtime scoring formula or
record schema changed; the evaluator patch tightens integrity checks on
previously accepted invalid inputs.

## Primary-source checks

- [Agent Skills specification](https://agentskills.io/specification): discovery metadata and progressive loading informed the concise-entry-point approach.
- [W3C landmark guidance](https://www.w3.org/WAI/ARIA/apg/practices/landmark-regions/): HTML elements have context-dependent landmark semantics; article is not a landmark.
- [C4 review checklist](https://c4model.com/diagrams/checklist): preserve viewpoint, meaning and readable relationships rather than enforce an arbitrary five-to-seven-node cap.
- [Transactional outbox guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html): producer atomicity and consumer duplicate handling need explicit boundaries.
- [Parallel Change](https://martinfowler.com/bliki/ParallelChange.html): expand/migrate/contract informs compatible transitions; rollback still requires workload-specific recovery evidence.
