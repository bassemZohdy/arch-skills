# Implementation backlog

Framework target: 1.0.0. The specification and implementation plan are documented; all tasks below are **not implemented**. Start with DAP-001 and satisfy dependencies before dependent work.

References: [framework](docs/deterministic-architecture-process.md), [review](docs/framework-review.md), [integration plan](docs/framework-implementation-plan.md). Earlier completed work is retained in [the historical log](docs/completed-work.md).

## P0 Contracts and persistence

- [ ] **DAP-001 — Define shared contracts and configuration**

  Dependencies: none. Paths: new versioned contracts/schemas under `framework/`, shared skill references, validation helpers under `scripts/`.

  Define stable IDs, records, criterion catalogue, framework/schema/rubric compatibility, organisational review authority, cost currency/horizon, review cadence and interview budgets. Define one canonical source for shared assets and how isolated skill installations obtain them.

  Acceptance: valid configuration parses; invalid weights, incompatible versions and missing authority have explicit scoped outcomes. The complete Q/D/F/B/A criterion expansion matches the framework. No silent defaults, confidence-based approval or unsupported ISO conformity claim. Example weights remain examples.

- [ ] **DAP-002 — Add requirements, trace graph and architecture templates**

  Dependencies: DAP-001. Paths: `skills/arch-orchestrator/assets/`, `skills/arch-doc/references/arc42-template.md`, `skills/arch-decision/assets/adr-template.md`, shared schema assets.

  Deliver templates for requirements/constraints, sources, quality scenarios, design elements, questions/assumptions, verification plans, reviews, exceptions and typed links. Map the 22-section architecture template into arc42; generate the RTM from the trace graph.

  Acceptance: a complete small example validates; IDs survive edits; design, implementation and executed verification stay distinct. Applicable sections have substantive content, and inapplicability has authority and rationale. Missing ADRs remain visible in the significant-decision inventory.

- [ ] **DAP-003 — Persist and recover process state**

  Dependencies: DAP-001, DAP-002. Paths: persistence helpers under `scripts/`, orchestrator references, fixtures under `tests/`.

  Checkpoint after each round and substantive change: answers, pending questions, baseline, counters, stage, gates, reviews and next action. Separate mutable checkpoints, frozen candidate manifests and publication receipts; use atomic writes and revision checks.

  Acceptance: interruption recovery preserves answers and counters; partial writes recover to the last valid manifest; concurrent changes are detected; repeated saves are idempotent. No unnecessary sensitive content or credentials are stored. Missing persistence produces an explicit draft limitation.

## P0 Execution integration

- [ ] **DAP-004 — Integrate preparation and scope assessment**

  Dependencies: DAP-001, DAP-002, DAP-003. Paths: `skills/arch-orchestrator/SKILL.md`, `references/orchestration-playbook.md`, `assets/shared-context-template.md`.

  Classify greenfield, brownfield and mixed scope from evidence; ingest configuration and existing artifacts; calibrate language and create targeted questions. Define the evaluator contract now, then wire actual assessment after DAP-010.

  Acceptance: missing documents, conflicting seeds and unavailable evaluation are explicit. Brownfield scope includes dependency impact. Standalone specialists remain usable without the full process. Preparation may gather information without claiming blocked gates passed.

- [ ] **DAP-005 — Implement the interview and convergence gates**

  Dependencies: DAP-003, DAP-004. Paths: orchestrator interview references/question banks, `tests/test-arch-orchestrator.yaml`, state fixtures.

  Elicit functional needs and quality drivers together; record provenance and scenarios; separate assumptions and mandates. Implement individual, set-level and stability checks, explicit baseline confirmation and round/time budgets. Apply MoSCoW within a named timeframe separately from exceptions.

  Acceptance: silence, unanswered questions, exhausted budgets and LLM-only confirmation cannot converge. Material changes reset stability. Confirmation records participants and baseline hashes. Conflicts remain blocked with an owner and next action. Plain-language suggestions never become unconfirmed mandates.

- [ ] **DAP-006 — Integrate design views and ADR decision analysis**

  Dependencies: DAP-002, DAP-005. Paths: `skills/arch-orchestrator/`, `skills/arch-decision/`, `skills/arch-doc/`, their templates and tests.

  Develop views and ADRs together with requirements, alternatives, evidence and verification links. Correct the ambiguous ADR immutability instruction. Remove the arbitrary four-gate cap and blanket do-nothing exemption; make baseline alternatives context-dependent. Bound and renormalise DAR sensitivity changes so weights cannot become negative.

  Acceptance: a mandatory-constraint failure cannot win through weighting; status quo is evaluated fairly where relevant; DAR scores remain separate from completeness scores. Reviewers see interacting views and decisions. Accepted reasoning is preserved and substantive changes use supersession.

- [ ] **DAP-007 — Implement review authority and exceptions**

  Dependencies: DAP-001, DAP-003, DAP-006. Paths: `skills/arch-governance/`, orchestrator review references, review/exception schemas and tests.

  Implement risk, reversibility, mandatory security/privacy/compliance review, scoped fail-closed outcomes, asynchronous queues, due dates and human-approved delegation. Replace implicit orchestrator ratification with recorded authority; resolve binding-constraint conflicts explicitly.

  Acceptance: scores and LLM confidence never approve decisions; missing relevant policy blocks dependent acceptance; independent drafting may continue. Silence/timeouts never approve. Invalid or expired exceptions block affected decisions. No messages are sent without user authorisation.

- [ ] **DAP-008 — Implement impact analysis and change re-entry**

  Dependencies: DAP-003, DAP-006, DAP-007. Paths: orchestrator references, trace/state helpers, change fixtures.

  Distinguish requirement changes, design defects and review changes. Traverse dependencies to identify affected decisions, views and verification plans; invalidate affected approvals/evaluations and preserve history.

  Acceptance: a design violating a Must have returns to design without changing the requirement; authorised scope changes reopen elicitation. Supersession and baseline reconciliation catch stale dependencies. Editorial changes do not reopen unrelated decisions.

## P0 Assessment and reporting

- [ ] **DAP-009 — Implement structural validation and score calculation**

  Dependencies: DAP-001, DAP-002. Paths: validator/scoring modules under `scripts/`, deterministic fixtures and tests.

  Validate schemas, IDs, statuses, typed links, applicability, evidence and manifests. Expand the fixed catalogue and calculate Q, D, F, B, T=min(F,B), A and configured S. Keep semantic judgments explicit and evidence-backed.

  Acceptance: the worked example yields 76.0%; F/B retain separate counts and uncovered IDs. Unknown checks receive zero credit; approved N/A is listed; empty required populations are not assessable; invalid weights fail. Missing ADRs/orphan elements remain in denominators. Round only displayed results. Gate status is independent of S.

- [ ] **DAP-010 — Add the process evaluator skill**

  Dependencies: DAP-007, DAP-008, DAP-009. Paths: new `skills/arch-evaluate/SKILL.md`, `agents/openai.yaml`, references/assets, orchestrator integration and skill catalog.

  Assess frozen inputs, invoke structural checks and record semantic findings with evidence. Keep `arch-review` responsible for design fitness. Support brownfield artifacts with missing historical records and version-aware assessment.

  Acceptance: audit-only runs do not change assessed inputs or recursively invoke the executor. Missing history stays unproven. Unavailable historical rubrics produce a limitation and separately labelled current-gap assessment, never fabricated scores. Preparation consumes actual evaluation results.

- [ ] **DAP-011 — Publish reports and detect stale evaluation**

  Dependencies: DAP-003, DAP-009, DAP-010. Paths: report/manifest helpers, `skills/arch-doc/` appendix support, publication fixtures.

  Store input hashes, UTC timestamp, evaluator identity, exact framework/schema/rubric/configuration versions and findings. Use an explicit publisher for generated reports and appendices; exclude generated output and publication receipts from assessed hashes.

  Acceptance: publishing is idempotent and does not invalidate its input hash. Changes to requirements, design, ADRs, reviews or configuration mark reports stale. Preserve user content outside the generated region; reject concurrent-revision conflicts. Accepting a baseline does not create a self-invalidating report.

## P1 Adoption and release evidence

- [ ] **DAP-012 — Add brownfield migration and lifecycle examples**

  Dependencies: DAP-008, DAP-010, DAP-011. Paths: `examples/`, fixtures under `tests/`, adoption guide under `docs/`.

  Demonstrate 22-section migration, mixed-scope changes, interrupted interviews, missing history and superseded decisions. Preserve existing IDs and sources; do not imply old approvals occurred under the new process.

  Acceptance: retained content is accounted for; missing facts stay explicit; questions target impacted gaps. Historical scores are not silently recalculated under another rubric. Include blocked cases and supported recovery, not only success.

- [ ] **DAP-013 — Package contracts and skills for supported hosts**

  Dependencies: DAP-001, DAP-010, DAP-011. Paths: setup/sync scripts, checked-in `.github/` mirrors, UI metadata, orchestrator catalog, `docs/harness-compatibility.md`.

  Make versioned shared assets available outside the repository, sync mirrors from canonical sources and document host capability fallbacks. Update metadata for the new evaluator.

  Acceptance: isolated installations resolve every contract reference; version and source/mirror drift are detected; existing skills load. Use isolated destinations without changing global skill installations. Claim verified compatibility only for hosts actually tested.

- [ ] **DAP-014 — Validate end-to-end behavior and publish usage guidance**

  Dependencies: DAP-005, DAP-006, DAP-007, DAP-008, DAP-009, DAP-010, DAP-011, DAP-012, DAP-013. Paths: `tests/`, applicable `tests-pi/` scenarios, test runners, optional CI, `README.md`, `AGENTS.md`, `docs/`.

  Run existing structural checks after skill edits and add meaningful framework tests: greenfield/brownfield, no response, absent evidence, invalid configuration, mandatory conflicts, unsupported versions, unavailable evaluator, concurrent writes, interruption and stale reports. Keep paid live-model runs opt-in.

  Acceptance: deterministic tests pass; behavioural results record actual harness/model versions and evidence. A high-score fixture with pending security review remains blocked. Document real commands, setup, configuration and limits. Mark planned capabilities available only after demonstration; move completed backlog items to the historical log with evidence.
