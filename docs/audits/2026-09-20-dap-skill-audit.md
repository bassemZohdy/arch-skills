# Architecture skills: structure and DAP conformance audit

Date: 2026-09-20. Assessed commit: `1089b9f01034a76743330864d23a55a72f12ca74`.
Normative process: [Deterministic Architecture Process](../deterministic-architecture-process.md), especially its Implementation Contract.
Scope: all 33 `skills/arch-*` entry points, their output templates, core orchestration/evaluation references, shared contracts, Python evaluator/persistence/publishing, fixtures and validation coverage.

Historical baseline: findings and observations below describe the assessed commit,
not the current working tree. See [the remediation review](2026-09-20-remediation-review.md)
for subsequent changes and validation. The original probe is guarded against use
with schema 2; its captured JSON remains unchanged.

## Verdict

The repository is structurally organized, but its DAP implementation is **not conformant enough to establish architecture readiness**. The skills have useful specialties; the weakest part is the contract between instructions, templates, durable records and executable checks.

Most seriously, the evaluator can declare an incomplete or unassessable baseline ready. The published completion claims should be reopened. Passing the current test suite is not evidence that the normative process has been implemented.

Do not apply a fabricated Q/D/T/A/S score to this skill repository: those metrics assess a scoped solution-architecture baseline, not the quality of a skill library. This audit uses explicit findings and acceptance criteria instead.

### What was verified

| Check | Observed result | What it establishes |
| --- | --- | --- |
| `python tests/test_skills.py` | 371/371 checks pass | Current structural rules only |
| `python tests/test_activation.py` | 33 descriptions rated Good or better | Trigger-description heuristics, not live activation accuracy |
| `python -m unittest discover -s tests -p 'test_dap*.py' -v` | 12/12 tests pass | Seven DAP tests and five adapter-contract tests |
| All 33 entry points | 89–317 lines each | All satisfy the repository's 500-line ceiling |
| Inline local resource-path inventory | No missing paths among the scanned backtick-delimited resource paths | Does not cover prose commands or every transitive link |
| Existing Markdown resource-link checker | Zero matching resource links in all 33 entry points | Its passing link checks are vacuous for the paths these skills use |
| Isolated `arch-evaluate` copy | Documented validator command exits 2; script absent | Package is not independently executable as documented |
| [Diagnostic probes](dap_audit_probe.py) | 14 reproducible observations below | Demonstrated gaps beyond the existing tests |

All entry points and the principal output templates were read. Core process contracts were inspected in depth; specialist reference libraries were inspected selectively for consistency and version drift. This is not a claim that every external article, code example, live model, host adapter or provider capability was exhaustively tested. No global skill installation was modified. This audit does not implement the proposed fixes.

`arch-evaluate` was used to distinguish process evidence from design fitness; `arch-review` was used for instruction, ownership, trade-off and output-quality analysis. Specialists are assessed as DAP contributors, not required to become 33 separate orchestrators.

## Priority findings

### F01 — Critical: readiness is disconnected from required evidence

Evidence: `scripts/dap/scoring.py:94`, `tests/test_dap.py:27`, probes P01–P04. The readiness gate checks a claimed convergence status and limited blocking findings, while configuration and structural integrity are set to true after shallow validation.

Observed:

- The supplied arithmetic fixture has Q=80, D=75, F=90, B=60, A=100, S=76 and `ready=true`.
- Setting every supplied Q/D/A check to fail still gives `ready=true` and S=21.
- Emptying requirements, design elements, decisions and links gives `assessable=false`, S=null, but `ready=true`.

DAP explicitly requires all readiness conditions independently of the aggregate score; its 76% arithmetic example does not establish readiness. See the process's Gate outcomes and transitions and Reproducible scoring sections.

Required correction: derive readiness from validated, current, baseline-bound requirement/set/stability evidence; complete forward/backward traceability; decision dispositions; artifact checks; reviews; risks and exceptions. Missing or unknown mandatory evidence must block. Acceptance: P01–P03 become not ready, with criterion-specific findings; a genuinely complete positive fixture becomes ready.

### F02 — Critical: mandatory human review can be bypassed

Evidence: `scripts/dap/scoring.py:92`, `skills/arch-evaluate/references/evaluation-contract.md:21`, probe P05.

Security review is required only when both a configuration flag and a state flag are true. Turning off the configuration flag permits readiness with a declared security implication and a pending review. Privacy, compliance, irreversible/high-risk, cost and cross-team cases have no equivalent executable checks. A bare `status: approved` is accepted without reviewer authority, baseline, time or delegation evidence.

Required correction: derive mandatory review applicability from recorded implications and approved policy; validate authority, disposition, scope, baseline and reuse/expiry. Missing policy blocks affected acceptance. Human-approved delegation can authorize bounded low-risk decisions, but the agent cannot invent it. Acceptance: pending, stale, unauthorized and missing required reviews block independently of score and optional configuration flags.

### F03 — High: score populations and evidence are caller-controlled

Evidence: `scripts/dap/scoring.py:12`, `framework/criteria-catalog.json`, probes P01/P04.

`score_checks` accepts anonymous rows containing only `result`. It does not derive populations from the criterion catalogue, require check/target IDs, detect duplicate or omitted checks, or require evidence and rationale. One anonymous passing row per Q/D/A dimension produces 100 in each dimension.

The fixture has 10 requirements and four decisions, but only 10 Q rows, four D rows and five A rows. Before authorized exclusions, DAP requires 116 Q checks for ten active in-scope requirements, 40 D checks if these are the four significant decisions, and 60 A checks if all twelve arc42 sections and eight supporting groups apply. Decision inventory also needs reconciliation against significant choices in the design, not merely existing ADR files.

Required correction: generate criterion instances from versioned catalogues and validated inventories; attach assessments to those instances; validate evidence locators and authorized applicability decisions. Preserve exact arithmetic until presentation. Acceptance: omitted/duplicate/unknown checks cannot inflate a score; absent required populations make the affected result and S unassessable.

### F04 — High: traceability is reduced to direct edge presence

Evidence: `scripts/dap/scoring.py:37`, `framework/project-schema.json`, `scripts/dap_rtm.py:18`, probe P12.

Forward coverage ignores confirmed source, source revision, delivery scope and verification plans. Backward coverage recognizes only explicit `design_to_requirement` edges, not valid paths through ADRs or binding constraints. The evaluator does not validate semantic endpoints or superseded/circular/unrelated paths. Requiring separately authored reverse edges also risks divergence between two representations of the same relationship.

The RTM renderer looks for `requirement_to_verification`, while the schema defines `design_to_verification`. In P12, a schema-supported DES→VER edge is omitted from the RTM, which instead displays `PLANNED`. Missing evidence must be marked missing, not described as a plan that has not been recorded.

Required correction: use one typed, validated graph and derive both coverage directions and the RTM from it. Include CON, source provenance, verification plans and conditional ADR paths. Acceptance: source-less and verification-less chains fail forward coverage; justified ADR/CON paths count backward; dangling, superseded and circular-only paths do not establish coverage.

### F05 — High: runtime records and version compatibility are not enforced

Evidence: `scripts/dap/contracts.py:31`, `scripts/dap/contracts.py:72`, `framework/project-schema.json`, probes P06/P09.

Runtime validation is weaker than even the current JSON schema. It accepts a requirement containing only an ADR ID, duplicate IDs across record kinds, unknown edge types and nonexistent endpoints. Required ownership, provenance, revision, acceptance, verification and lifecycle fields are not validated. First-class schemas/inventories for constraints, questions, assumptions, exceptions, verification and reviews are incomplete or absent.

All framework/schema/rubric versions set to `999.0.0` are accepted: semantic-version syntax is checked, not supported compatibility. Configuration provenance/approval and complete review policy are also not enforced. Invalid configuration currently aborts evaluation rather than providing the scoped partial reporting described by DAP.

Required correction: one authoritative versioned schema/semantic-validation layer used by every consumer; explicit version compatibility and historical-rubric handling. Acceptance: malformed records and unsupported versions produce precise findings; unavailable score policy prevents S without suppressing independently assessable findings.

### F06 — High: report freshness omits inputs that change the result

Evidence: `scripts/dap/scoring.py:52`, `scripts/dap/scoring.py:63`, probes P07/P08.

The manifest scans the project directory rather than using an explicit assessed set. It excludes `process/assessment.json`, although that file directly determines the score. External configuration and the rubric are not bound to the manifest. Generated appendix regions are not specifically excluded.

Changing assessment results changes S from 76 to 21 while `report_is_stale` remains false. Changing an external configuration changes S from 76 to 67.5, again without staleness. Reading files before hashing also does not guarantee that the final manifest describes the same bytes that were evaluated under concurrent changes.

Required correction: freeze and evaluate one explicit snapshot, including evidence assessments, configuration and rubric identities/content; keep generated outputs outside the assessed set. Acceptance: every assessed input change invalidates the report, unrelated files do not, and publishing an appendix cannot invalidate its own baseline.

### F07 — High: checkpoint writer, reader and evaluator disagree

Evidence: `scripts/dap/persistence.py:30`, `scripts/dap/persistence.py:37`, `skills/arch-orchestrator/assets/dap-checkpoint-template.json`, probes P10/P11.

Persistence writes `{revision, state, state_hash}`. The evaluator reads `process/state.json` as a flat object. Giving it a saved envelope changes the convergence outcome without changing the underlying state. `load_checkpoint` accepts a tampered state without checking the stored hash.

Expected-revision validation is a check-then-replace sequence without a lock or compare-and-swap protecting the complete operation. Atomic file replacement prevents a partial file, but alone does not prevent two writers from reading the same revision and overwriting each other. This race is a code-inspection finding, not a concurrency stress-test result.

The checkpoint template also omits several normative fields, including assessed manifest and baseline revision. Required correction: one schema and reader across runtime and templates, integrity validation, concurrency control, and interrupted-operation recovery. Acceptance: saved checkpoints evaluate consistently, tampering fails, simultaneous stale writers cannot both commit, and resume validates the actual artifact baseline.

### F08 — High: publication does not preserve a versioned audit history

Evidence: `scripts/dap_publish.py:17`, probe P13, DAP Evaluation freshness and publishing.

Two publications leave only `evaluations/latest.json`; the prior report is overwritten. The publisher does not revalidate the frozen input revision at publication, record a separate baseline/publication revision contract, or generate the architecture appendix. Its unrestricted `--output` can target assessed source files rather than a report-only destination. No overwrite of product inputs was performed in this audit.

Required correction: immutable report runs plus an optional latest pointer, frozen-manifest publication checks, bounded output destinations, and idempotent generated-region handling. Acceptance: both reports survive, the correct prior report becomes stale, source documents remain unchanged outside authorized generated regions, and publication refuses a changed candidate.

### F09 — High: isolated skill packaging breaks core execution

Evidence: `skills/arch-evaluate/SKILL.md:14`, `skills/arch-orchestrator/SKILL.md:149`, probe P14; implementation-plan Integration boundaries.

The evaluator commands assume repository-root `scripts/`. The orchestrator assumes root `framework/` and `scripts/dap`. Those dependencies are not present in an isolated skill copy or declared through an implemented portable dependency-resolution contract.

Required correction: maintain one canonical shared implementation, then distribute versioned in-package dependencies or an explicit, resolvable portable dependency. Validate the release artifact, not only a repository checkout. Do not reintroduce a particular AI host, global installation path or host API into the skill contract. Acceptance: run the documented workflow from an unrelated working directory using only the declared installation artifacts.

### F10 — High: orchestration retains conflicting authority and output rules

Evidence: `skills/arch-orchestrator/SKILL.md:85`, `:120`, `:142`; `references/orchestration-playbook.md:34`; `assets/shared-context-template.md:78`.

The original workflow gives ratification to the orchestrator, orders user requirements ahead of legal/regulatory/security constraints, and requires the old 22-section output. Its later DAP section does not fully reconcile these instructions with configured human authority, binding constraints and the default twelve-section arc42 output. The root-dependent DAP paragraph also includes explicit process evaluation in the orchestrator route, despite the independent evaluator boundary.

Required correction: explicitly branch standalone versus DAP workflows; retain useful 22-section content through the existing arc42 mapping; treat mandatory constraints as eligibility gates; distinguish an agent recommendation from an authorized disposition. Route process-only audits to `arch-evaluate` and design-quality reviews to `arch-review`. Acceptance: conflicting user preference cannot waive a binding constraint; absent authority blocks acceptance; DAP outputs use the mapped arc42 baseline.

### F11 — High: specialist outputs lack a reliable DAP handoff contract

Evidence: specialist assets across the library, especially `arch-test/assets/strategy-template.md`, `arch-security/assets/review-template.md`, `arch-governance/assets/review-template.md`, `arch-review/assets/review-template.md` and `arch-fitness/assets/template.md`.

Most templates contain useful topic headings but do not require baseline revision, REQ/CON/DES/ADR/VER relationships, evidence locators, uncertainty, authority and planned-versus-executed status. Better instructions in the skill body are therefore not reliably preserved in generated artifacts. `arch-fitness` has code examples instead of a portable rule/evidence record; `arch-test` does not supply the VER plan DAP needs.

Required correction: a small, conditional specialist contribution envelope plus domain-specific payloads, not a copy of all six stages in every skill. Align entry point, references and assets together. Acceptance: each invoked specialist can return traceable proposals and verification plans without fabricating stakeholder approval or delivery evidence.

### F12 — High: DAP-specific resources are not routed by their entry points

The inventory found these resources are not named in their owning entry point:

- `arch-orchestrator/assets/dap-checkpoint-template.json`
- `arch-orchestrator/assets/dap-requirement-template.json`
- `arch-decision/assets/dap-adr-template.md`
- `arch-doc/references/dap-arc42-mapping.md`

They exist, but the ordinary workflows instead direct agents to generic templates. This is a routing gap, not proof the resource can never be discovered indirectly. Required correction: explicitly select the DAP resource in DAP mode and exercise that route in tests. In particular, the stronger DAP ADR template should not be bypassed by the generic ADR path.

### F13 — Medium: content and reference versions drift within packages

These are verified examples, not an exhaustive currentness certification:

| Skill | Local inconsistency | Required correction |
| --- | --- | --- |
| `arch-security` | Entry point names Top 10:2025; its review asset still has the older category mapping, e.g. A02 Cryptographic Failures and A10 SSRF | Pin the chosen edition across body/reference/template; do not label a Top 10 awareness checklist as complete security compliance. The current list changes those categories. [OWASP](https://top10.owasp.org/2025/) |
| `arch-devops` | `SKILL.md:229` describes four DORA metrics, including broad time-to-restore-service terminology | Distinguish historical measurement from the current five-metric model and deployment-specific recovery definition; add rework measurement. [DORA](https://dora.dev/guides/dora-metrics/) |
| `arch-cost` | Entry point labels the four domains as phases; its FinOps reference correctly separates the two | Use Inform/Optimize/Operate for phases; retain the domains as a different dimension. [FinOps Foundation](https://www.finops.org/framework/) |
| `arch-accessibility` | Entry point targets WCAG 2.2 but routes to a short WCAG 2.1 reference | Version scope and criterion IDs explicitly; update supporting coverage for the claimed edition. Avoid a blanket conformance statement based on a few checks. [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) |
| `arch-review` | `references/quality-attributes.md:5` attributes eight characteristics to an unversioned ISO/IEC 25010 | Identify the historical edition or update the model; the 2023 product-quality model has nine characteristics. [ISO](https://www.iso.org/standard/78176.html) |
| `arch-metrics` | Prose assigns the pain/uselessness zones to the wrong instability sides and conflicts with its own quadrant chart | Pain is low instability/low abstractness; uselessness is high instability/high abstractness. Define edge cases and avoid presenting either instability extreme as universally good/bad. [NDepend metric definitions](https://www.ndepend.com/docs/code-metrics) |

Also qualify example thresholds and scoring bands in assets, not just entry-point disclaimers: principle-check counts, coverage targets, default retry values and usability targets are not automatically approved project gates. Provider/tool examples can remain optional examples; they should not become a required host setup or universal technology choice.

### F14 — High: tests and implementation-status claims overstate completion

Evidence: `tests/test_skills.py:259`, `tests/test_dap.py`, `docs/framework-implementation-plan.md:3`, `docs/dap-implementation-status.md`, `TODO.md`.

The link checker ignores the backtick paths actually used, transitive references and prose CLI dependencies. Structural rules enforce a >500-word minimum and supporting directories, while missing exact name/directory validation and complete nonempty frontmatter validation. Those rules reward bulk rather than a minimal sufficient skill. The portable format allows optional resource directories. [Agent Skills specification](https://agentskills.io/specification)

Existing DAP tests check arithmetic, a single security path, sequential revisions and limited freshness. They do not establish catalogue completeness, graph semantics, non-vacuous readiness, packaging or concurrent recovery. The implementation plan says remaining work is limited to host integration and live models, and TODO says there are no open implementation tasks. The probes contradict those claims.

Required correction: reopen core DAP tasks, distinguish instruction-level guidance from executable enforcement, replace arithmetic-only success fixtures with complete baselines, and introduce negative/positive contract tests. Retain host-neutral tests; a live model is not needed to catch the demonstrated bugs.

## DAP-stage validation

| Process obligation | Primary owner | Present | Gap / validation outcome |
| --- | --- | --- | --- |
| 1. Seed and requirements lifecycle | Orchestrator | Scope and stable-ID guidance | Full record semantics and CON lifecycle not enforced |
| 2. Preparation and brownfield evidence | Orchestrator + evaluator | Mode classification and evidence-gap instructions | Baseline evaluator can pass incomplete evidence; source/approval provenance insufficient |
| 3. Interviews and convergence | Orchestrator | Budgets, rounds and human confirmation described | Runtime trusts `convergence_status`; no reconciliation against 11-per-REQ, five-set and stability checks |
| 4. Views and ADRs together | Specialists + decision + doc | Strong domain guidance; DAP ADR/mapping resources exist | DAP resources not selected; design/decision inventory and significant-choice coverage unvalidated |
| 5. Human review | Governance + human authority | Escalation policy described | Fail-closed applicability/authority not implemented; agent-ratification wording conflicts |
| 6. arc42, ADR log, RTM and supporting records | Doc + orchestrator | Generic templates and RTM script | 22-section conflict, VER mismatch, weak artifact checks and publication history |
| Re-entry/change impact | Orchestrator | Stage 3/4/5 routing in prose | Executable dependency invalidation and baseline-bound approval checking not established |
| Persistence and interrupted resume | Shared runtime | Atomic replacement and revision field | Envelope mismatch, no hash check, concurrency gap |
| Read-only reproducible evaluation | Evaluate | Read-only calculation exists | Inputs not fully frozen; incomplete rubric and graph semantics |
| Handoff and continuing ownership | Governance + orchestrator | Prose ownership/cadence guidance | Maintainer, reviewer, review triggers and handoff acceptance need durable records and checks |

## Proper structure for the skill library

Keep the current separation of specialties. Do not create a second general-purpose orchestrator or make all skills execute DAP end to end.

### Responsibilities and boundaries

| Layer | Owner | Must not do |
| --- | --- | --- |
| Execution and baseline assembly | `arch-orchestrator` | Invent authority, silently accept decisions, bypass prerequisite gates |
| Independent process assessment | `arch-evaluate` | Repair assessed inputs during an audit or equate completeness with good design |
| Independent design-quality review | `arch-review` | Present its recommendation as a human approval or a DAP readiness score |
| Decision reasoning and lifecycle | `arch-decision` | Confuse DAR option ranking with DAP completeness scoring |
| Views and artifact production | `arch-doc` | Treat planned verification as delivered proof or overwrite historical ADRs |
| Policy, delegation and review records | `arch-governance` | Treat silence, confidence or a score as approval |
| Domain reasoning and verification proposals | Other 27 specialists | Mutate accepted baselines or impose full DAP on a standalone request |
| Schemas, graph, state and arithmetic | Shared portable library | Depend on a particular agent host or undocumented repository-relative paths |

### Recommended package layout

This is a proposed target, not a structure claimed to exist today. Only include resources that the skill actually needs.

```text
skills/arch-<concern>/
  SKILL.md                         # trigger, boundary, inputs, workflow, outputs, validation
  references/
    <domain-guidance>.md           # detail loaded for the selected task
    dap-contribution-contract.md   # conditional DAP integration; versioned packaged contract
  assets/
    <domain-output-template>.md    # one authoritative template rather than duplicate body text
  scripts/                        # optional; portable, declared dependencies only

framework/                        # canonical schemas, catalogues, policy and state contracts
scripts/                          # canonical build/validation helpers, no required AI host
tests/                            # structure, contract, isolated-package and scenario checks
```

Avoid independently hand-maintained copies of the shared contract. Generate and verify packaged copies from a canonical version, or provide a tested explicit dependency mechanism. The installation result must work without the repository root. Optional example technologies are not host adapters and need not all be removed.

### Consistent entry-point sections

1. YAML name and a precise trigger description, with name matching the directory.
2. Purpose and responsibility boundary, including what adjacent skills own.
3. Inputs and missing-evidence handling: ask, record unknown, or return a scoped blocker.
4. A short ordered workflow with explicit reference/template routing.
5. Output contract and validation criteria.
6. Conditional DAP contribution rules; standalone requests stay lightweight.
7. Relevant pitfalls and related-skill handoffs.

Keep the entry point below 500 lines, but do not impose a minimum word count. Move catalogues, provider matrices and long examples to references. Keep outputs in assets; avoid maintaining near-identical inline and asset templates. These recommendations follow progressive disclosure and optional resource packaging in the [Agent Skills specification](https://agentskills.io/specification).

### Conditional DAP contribution contract

When invoked within DAP, every specialist should consume and return the following. This is a proposed envelope, not an additional scoring dimension.

| Part | Minimum information |
| --- | --- |
| Invocation | Run ID, task scope, mode, stage, candidate baseline revision/hash, relevant contract versions |
| Inputs | Relevant REQ/CON IDs, source revisions, quality scenarios, current DES/ADRs, protected decisions, available evidence and configured authority |
| Findings | Stable finding ID, target IDs, observed/proposed/unknown status, severity, evidence locator, rationale and uncertainty |
| Design contribution | Proposed DES records and relationships, alternatives, trade-offs, rejected options, proposed ADR needs |
| Verification | VER ID, protected REQ/CON/DES/ADR, method, measurable acceptance condition, owner, environment and planned/executed status; evidence only if actually obtained |
| Governance | Required review type, proposed owner, decision status, exception request or risk; explicit statement that approval remains pending unless evidenced |
| Change impact | Affected upstream/downstream IDs, approvals/evaluations made stale, required re-entry stage |
| Return status | Complete for assigned scope, provisional, or blocked; unresolved Q/ASM records and next action |

Not every small specialist answer needs to create every record type. Apply fields to the actual contribution, with explicit applicability. A missing stakeholder answer stays unknown; a suggested default is an assumption. Significant design assertions must be inventoried even when no ADR has yet been written.

## Skill-by-skill assessment and target contract

Every row inherits the shared DAP contribution gap above unless stated otherwise. “Partial” means useful domain structure but an incomplete DAP handoff; it does not mean the skill is unusable standalone. Stage numbers refer to DAP. The six process-facing skills need priority repair because other skills depend on their contracts.

### Process-facing skills

| Skill | Status / role | Preserve | Required structural change and acceptance example |
| --- | --- | --- | --- |
| [arch-orchestrator](../../skills/arch-orchestrator/SKILL.md) | Blocking gaps; stages 1–6 | Selection, shared context, reconciliation, preparation and change-routing guidance | Unify the legacy workflow with DAP gates; package contracts; route DAP templates; separate proposals from approvals. Test interrupted and brownfield runs with baseline-bound human confirmation. |
| [arch-evaluate](../../skills/arch-evaluate/SKILL.md) | Blocking gaps; independent assessment | Clear separation from design review, unknown-evidence and read-only intent | Align its reference contract with the normative rubric; repair runtime findings F01–F09; add evaluator/config identity and complete evidence findings. Test isolated installation and complete/invalid baselines. |
| [arch-doc](../../skills/arch-doc/SKILL.md) | Partial; stages 4/6 | Multiple documentation formats, diagrams and ADR preservation | Add explicit DAP-mode routing to the arc42 mapping, linked DES/ADR/scenario records and generated appendix regions. Keep requested formats for standalone tasks. Test all twelve applicable arc42 sections for substantive evidence. |
| [arch-decision](../../skills/arch-decision/SKILL.md) | Partial; stages 4/5 | Knockout gates, alternatives, weighted evaluation and sensitivity analysis | Select DAP ADR asset in DAP mode; normalize weight conventions; make close-call thresholds decision-specific; require authority, evidence, baseline and supersession. Test a top-scoring option rejected for a failed mandatory gate. |
| [arch-governance](../../skills/arch-governance/SKILL.md) | Partial; preparation/review/handoff | Review policy, exceptions, ownership and expiry guidance | Add machine-readable policy/review/delegation/exception records with scope, provenance, approver, baseline and expiry. Test missing cost/risk policy and stale delegation fail affected acceptance. |
| [arch-review](../../skills/arch-review/SKILL.md) | Partial; design fitness at stages 4/5 | Evidence-driven findings and process/design distinction | Make findings template carry target IDs, evidence, uncertainty, owner and validation action; label approval text a recommendation. Pin quality-model edition. Test that good process completeness cannot hide a poor design. |

### Domain and structural design

| Skill | DAP role / status | Preserve | Required output and validation improvement |
| --- | --- | --- | --- |
| [arch-ddd](../../skills/arch-ddd/SKILL.md) | Stages 3/4; partial | Domain language, contexts, aggregates and invariants | Capture domain-expert source/confirmation, context and invariant IDs, owning teams, cross-context dependencies and invariant VER plans. Test a boundary change routes cross-team review. |
| [arch-patterns](../../skills/arch-patterns/SKILL.md) | Stage 4; partial | Pattern trade-offs and composition guidance | Record quality scenarios, eligible alternatives, disqualifying constraints, DES/ADR mapping and fitness criteria. Test selection from measured drivers rather than a universal pattern lookup. |
| [arch-principles](../../skills/arch-principles/SKILL.md) | Stages 4/5; partial | Simplicity, coupling/cohesion and context-aware guidance | Replace unconditional principle-count approval with applicability, evidence and cost-of-change reasoning. Preserve justified seams with one implementation. Test justified exceptions do not become automatic design failures. |
| [arch-antipatterns](../../skills/arch-antipatterns/SKILL.md) | Brownfield preparation/review; partial | Concrete evidence, impact ranking and refactor/contain/accept choices | Add baseline/target IDs, accepted-debt authority, expiry and measurable remediation verification. Distinguish suspected smell from established costly behavior. |
| [arch-microservices](../../skills/arch-microservices/SKILL.md) | Stage 4; partial | Ownership, lifecycle, bounded contexts and operational-cost caveats | Produce service-boundary DES IDs, data authority, independent-deployment evidence, consistency/failure scenarios, alternatives and VER plans. Test that a modular-monolith alternative remains eligible. |
| [arch-api](../../skills/arch-api/SKILL.md) | Stages 3/4/6; partial | Contract evolution, idempotency, concurrency and errors | Add contract version, consumer/producer owners, REQ/CON mappings, auth decisions and compatibility/negative-test VER records. Test API changes identify affected consumers and approvals. |
| [arch-integration](../../skills/arch-integration/SKILL.md) | Stage 4; partial | Boundary contracts and delivery-semantics reasoning | Capture system/contract IDs, data authority, failure/ordering semantics, owners and cross-team review; link integration tests. Test failure and contract-change paths, not only a happy-path topology. |
| [arch-event](../../skills/arch-event/SKILL.md) | Stage 4; partial | Delivery scope, idempotency, replay and compensation | Add schema/revision ownership, event versus command intent, causation, consistency and replay verification linked to requirements. Test duplicate delivery and partial saga failure with explicit acceptance conditions. |
| [arch-data](../../skills/arch-data/SKILL.md) | Stages 3/4; partial | Ownership, data contracts, freshness, retention and recovery | Add lineage/source IDs, classification constraints, schema/lifecycle decisions, data-quality and restore VER plans. Test a retention change propagates to stores, pipelines, controls and approvals. |

### Platform, delivery and operation

| Skill | DAP role / status | Preserve | Required output and validation improvement |
| --- | --- | --- | --- |
| [arch-cloud](../../skills/arch-cloud/SKILL.md) | Stage 4; partial | Workload fit, identity, region/quota, egress and exit considerations | Organize around workload constraints before provider choices; record region/rate evidence dates, landing-zone controls, recovery plans, DES/ADRs and cost/security review. Test an unavailable region/service assumption remains provisional. |
| [arch-devops](../../skills/arch-devops/SKILL.md) | Stages 4/6/handoff; partial | Artifact immutability, provenance and rollback caveats | Model release/promotion gates, environment ownership, approval evidence, supply-chain and rollback VER plans; make Kubernetes conditional; update DORA definitions. Test deployed artifact identity matches reviewed provenance. |
| [arch-features](../../skills/arch-features/SKILL.md) | Stages 4/6; partial | Flag ownership/expiry and separation from authorization | Record flag/experiment IDs, exposure policy, guardrail thresholds, approval, kill-switch tests and removal criteria. Test rollout stops on recorded guardrail failure and expired flags are visible. |
| [arch-migration](../../skills/arch-migration/SKILL.md) | Brownfield preparation/stages 4–6; partial | Incremental cutover, reconciliation, compatibility and rollback rehearsal | Add old/new baseline IDs, phase dependencies, checkpoint ownership, quantitative cutover/rollback conditions and irreversible-step approval. Test changed requirements return to stage 3, not directly to cutover. |
| [arch-refactoring](../../skills/arch-refactoring/SKILL.md) | Change design/verification; partial | Characterization tests, incremental delivery and behavior preservation | Link before/after DES and ADR records, scope impacts, preserved-behavior evidence, revert boundary and validation owner. Test a structural change identifies affected verification and approvals. |
| [arch-perf](../../skills/arch-perf/SKILL.md) | Stages 3/4/6; partial | Workload-based budgets and tail-latency measurements | Produce quality scenarios with stimulus, environment, response and measurable threshold; record dataset/build/load assumptions and VER owner. Test planned benchmark does not become claimed measured compliance. |
| [arch-resilience](../../skills/arch-resilience/SKILL.md) | Stages 3/4/6; partial | Bounded retry, cancellation, degradation and blast-radius controls | Record failure-model IDs, SLO/RTO/RPO constraints, policy rationale, recovery owner, experiment abort authority and VER evidence. Test a destructive experiment remains a plan without execution authorization. |
| [arch-observability](../../skills/arch-observability/SKILL.md) | Stages 4/6/handoff; partial | Semantic-convention pinning, budgets, SLOs and runbooks | Replace tool-stack-only output with signal definitions/versions, REQ/SLO mapping, privacy/retention controls, owner and alert verification. Test missing telemetry evidence is unknown, not a passing operational control. |
| [arch-cost](../../skills/arch-cost/SKILL.md) | Stages 3/4/5; partial | Unit economics, uncertainty, commitments and service trade-offs | Separate FinOps domains/phases; record rate date, currency, horizon, workload assumptions, forecast range, budget constraint and approval threshold. Test a cheap option failing a mandatory constraint is ineligible. |
| [arch-fitness](../../skills/arch-fitness/SKILL.md) | Verification planning/handoff; partial | Decision-linked rules, ownership, noise and expiry guidance | Provide a portable VER/rule template before implementation examples: protected IDs, measurement, threshold, evidence, failure action, owner and exception expiry. Test actual execution separately from rule generation. |
| [arch-metrics](../../skills/arch-metrics/SKILL.md) | Preparation/review/handoff; partial | Baselines, trends and anti-gaming caveats | Correct metric definitions/diagram alignment; record units, sampling, source revision, uncertainty and approved thresholds. Test zero denominators and avoid substituting a debt score for DAP readiness. |

### Risk, verification and user-facing design

| Skill | DAP role / status | Preserve | Required output and validation improvement |
| --- | --- | --- | --- |
| [arch-security](../../skills/arch-security/SKILL.md) | Stages 2–5; partial, high-risk handoff | Threat modeling, identity, trust boundaries and verification intent | Version threat/control criteria consistently; link threats to REQ/CON/DES/VER, evidence, residual risk and authorized human disposition. Test a Top 10 checklist cannot establish implementation or approval by itself. |
| [arch-compliance](../../skills/arch-compliance/SKILL.md) | Stages 2/3/5; partial, high-risk handoff | Jurisdiction/version applicability and control evidence | Record obligation source/version, applicability authority, data scope, control mapping, retention basis, exceptions and review expiry. Test unsupported legal applicability is flagged for qualified confirmation. |
| [arch-test](../../skills/arch-test/SKILL.md) | Stages 3/4/6; partial, critical trace dependency | Risk-based layers, contract tests and flaky-test ownership | Make a VER-plan register central: requirement, method, environment, threshold, owner and evidence state. Test every active in-scope requirement has a plan while unexecuted tests remain planned. |
| [arch-ai](../../skills/arch-ai/SKILL.md) | Stages 3–5; partial | Versioning, evaluation, tool permissions, fallback and approval gates | Record model/prompt/corpus/eval-set versions, risk-specific acceptance thresholds, grounding evidence, permitted actions, human review and runtime budgets. Test tool-use proposals cannot authorize new actions implicitly. |
| [arch-frontend](../../skills/arch-frontend/SKILL.md) | Stages 3/4; partial | Rendering/state boundaries, composition and user budgets | Add journey/REQ IDs, trust and ownership boundaries, quality scenarios, alternatives and linked accessibility/performance/security verification. Keep framework menus illustrative rather than mandatory. |
| [arch-accessibility](../../skills/arch-accessibility/SKILL.md) | Stages 3–5/verification; partial | Semantics, keyboard, assistive technology and manual testing | Pin WCAG edition/level and scoped flows; record criterion evidence, technology/browser context, unresolved barriers and review authority. Apply to internal as well as customer-facing interfaces. |
| [arch-usability](../../skills/arch-usability/SKILL.md) | Stages 2/3/4; partial | Research, journeys, heuristics and outcome measures | Record study/source IDs, participant context, consent/privacy boundaries, task success criteria and research uncertainty; separate heuristic opinion from observed usability. Do not use universal sample/score targets as approved gates. |

## Remediation sequence and release acceptance

This is a proposed backlog; no item below is marked implemented by this audit.

| Order | Work package | Exit evidence |
| --- | --- | --- |
| 1 | Correct readiness and mandatory-review semantics; reopen overstated completion claims | Negative fixtures for F01/F02 block, complete positive fixture passes, status documents distinguish delivered from pending |
| 2 | Freeze complete schemas, criterion catalogues, source/constraint/verification graph and versions | Catalogue expansion, semantic graph, authority and scope tests; RTM round-trip agrees with evaluator |
| 3 | Repair snapshot/freshness, checkpoint integrity/concurrency and immutable publication | Assessed-input mutation tests, concurrent writer test, interrupted recovery, generated-region/idempotence tests |
| 4 | Package core dependencies and reconcile orchestrator/evaluate/doc/decision/governance/review | Each isolated package resolves declared dependencies; DAP mode chooses correct templates and authority path |
| 5 | Upgrade `arch-test`, security/compliance and other domain contribution templates | Each specialist output maps into the common records without losing IDs, provenance or planned/executed distinction |
| 6 | Reconcile domain references, assets, versions and illustrative defaults | Cross-resource consistency checks plus domain-specific cases for the six demonstrated drift examples |
| 7 | Expand lifecycle validation and publish a verified implementation status | Greenfield, brownfield, interrupted, changed-approval, invalid-version and high-score-blocked scenarios; clearly separate live-model evidence |

Tests needed across the library:

- Structural: discover malformed skill directories too; nonempty frontmatter; name equals directory; line budget; host neutrality; resolve Markdown/backtick/script paths and transitive dependencies.
- Semantic records: full required fields, typed/global IDs, source confirmation, status/revision consistency, approved configuration and version compatibility.
- Scoring: exact catalogue populations, unknown/fail treatment, authorized N/A, omitted significant decisions, zero denominators and no early rounding.
- Traceability: source→REQ/CON→DES/ADR→VER, valid reverse justification, scope, supersession, dangling endpoints and cycles.
- Gates: explicit stakeholder confirmation, stability reset, interview exhaustion, unauthorized/stale reviews, blocking risks and exceptions, high score without readiness.
- Persistence: identical envelope interpretation, integrity checks, stale/concurrent writers, partial operation recovery and dependency-based invalidation.
- Publishing: immutable history, explicit snapshots, freshness for all assessed inputs, no source overwrite, no self-invalidating appendix.
- Packaging: isolated package in a fresh directory, no global installs and no undeclared access to repository-root resources.
- Behavioral: standalone request does not invoke full DAP; missing answers stay unknown; specialists propose rather than approve; brownfield gaps are not invented; live-model result includes actual execution identity and evidence.

## Reproduction observations

Run `python docs/audits/dap_audit_probe.py`. It uses disposable copies under the repository, prints JSON and removes its own temporary copies. It is a diagnostic script, not a test suite whose successful exit means DAP conformance.

The captured [machine-readable evidence and 33-skill inventory](2026-09-20-dap-evidence.json) records the observed results for this audit baseline.

| Probe | Observation on the assessed implementation |
| --- | --- |
| P01 | Arithmetic fixture: ready=true despite Q80/D75/F90/B60; supplied Q/D/A populations 10/4/5 |
| P02 | All supplied Q/D/A checks fail: ready=true, S21 |
| P03 | Required record inventories empty: ready=true, assessable=false, S=null |
| P04 | One anonymous passing check per Q/D/A dimension: Q=D=A=100, ready=true |
| P05 | Declared security implication, pending review, disabled flag: ready=true |
| P06 | Framework/schema/rubric `999.0.0`: accepted, ready=true |
| P07 | Assessment changed: S76→21; old report stale=false |
| P08 | External weights changed: S76→67.5; old report stale=false |
| P09 | Wrong-kind IDs, cross-kind duplicate IDs, missing fields and dangling/unknown edges: accepted |
| P10 | Same flat state wrapped by persistence envelope: convergence/readiness changes |
| P11 | Checkpoint state modified without updating hash: tampered state loads |
| P12 | Schema-supported DES→VER link: VER ID absent from RTM; row says PLANNED |
| P13 | Two publications: only latest.json survives; assessment change not recognized as prior-report staleness |
| P14 | Isolated evaluator's documented script command: exit 2, script missing |

The existing greenfield example should remain an arithmetic fixture only until its records and evidence satisfy the process. A coherent, fully evidenced positive baseline is necessary before advertising DAP readiness validation as complete.
