# Architecture skills remediation and re-review

Date: 2026-09-20. Scope: all 33 canonical architecture skills, their contribution
assets, DAP runtime, packaging, documentation and deterministic validation.
This report follows the [original audit](2026-09-20-dap-skill-audit.md) of commit
1089b9f. The original evidence is retained as historical evidence, not rerun results
against this implementation. The original review assessed local working-tree
changes; the release preparation section records the subsequent cleanup.

## Outcome and public interface

Keep specialist responsibilities separate, but do not expose all 33 by default.
The implemented default distribution exposes three discoverable skills:

| User workflow | Public interface | Stopping boundary |
| --- | --- | --- |
| Interview | arch-orchestrator, interview mode | Confirmed requirements/constraints or explicit blocked handoff; no automatic design |
| Create | arch-orchestrator, create mode | Candidate architecture; human acceptance is separate |
| Update | arch-orchestrator, update mode | Changed candidate with dependency impacts, preserved history and renewed evidence |
| Evaluate | arch-evaluate for process; arch-review for design | Separate read-only results; no implicit repair or publication |

Default packages bundle other capabilities as selectively loaded instructions.md
resources, resolved by package-catalog.json. Recursive SKILL.md discovery sees
three entries, not nested specialist entries. The expert profile exposes all 33
or explicitly selected specialists. There is one canonical source per skill and
one authoring orchestration path; no additional host runtime or proprietary
hidden-skill flag was introduced.

Skill-creator guidance informed the progressive disclosure, removal of duplicate
inline templates, explicit resource routing and isolated package validation.
Architecture review boundaries keep design fitness separate from process evidence.

## Finding dispositions

Implemented means the identified mechanism was corrected and checked at the level
stated below. It does not mean an LLM's behavior or a real architecture is certified.

| Finding | Correction and re-review evidence |
| --- | --- |
| F01 Readiness | Separate configuration, integrity, convergence, traceability, decisions, artifacts, reviews, freshness and assessability gates. Positive fixture passes; all-fail, empty, unknown and high-score-blocked cases fail readiness. |
| F02 Human authority | Derive mandatory categories from design/decision implications, bind reviews to subject and baseline, check reviewer authority and dates, retain pending queue blockers. Tests cover disabled security flag, all mandatory categories, missing/stale/unauthorized approvals and non-waivable exceptions. |
| F03 Score populations | Expand versioned Q/D/A catalogues, validate exact check identities and evidence, keep missing decisions and unknown checks in denominators, authorize N/A, use exact rational weighted arithmetic. Tests reject anonymous, duplicate and mis-targeted inputs. |
| F04 Traceability | Typed source, requirement/constraint, accepted decision, design and verification relationships; confirmed source revision; shared evaluator/RTM semantics. Tests cover ADR-mediated links, CON justification, missing source/plan, circular-only links and explicit scope exclusions. |
| F05 Records and versions | JSON Schema plus semantic ID/reference checks; supported framework/schema/rubric tuple enforced. Quality scenarios and executed-verification evidence are required. Unsupported versions are unassessable, not silently rescored. |
| F06 Freshness | Explicit byte snapshot includes assessment, review, state/history, config, rubric, schema and declared evidence. Subject binding invalidates affected assessments; generated outputs are excluded. Tests cover changed inputs, external configuration and generated regions. |
| F07 Checkpoints | Unified revision/state/hash envelope, integrity checking, expected-revision locking and optional artifact-bound resume. Tests cover tampering, conflicting writers, changed subjects and preservation of interrupted locks. |
| F08 Publication | Timestamp/UUID JSON reports and adjacent Markdown summaries, guarded latest pointer, source-overwrite rejection and freshness check before promotion. Two publications retain two report versions. |
| F09 Packaging | Default/expert builder bundles runtime, contracts and resources. Isolated evaluator runs from an unrelated directory; recursive discovery, transitive resource paths, content hashes and no-overwrite behavior are tested. |
| F10 Orchestration | Explicit interview/create/update modes; evaluate stays read-only; binding constraints precede weighted preferences; human disposition is separate. Arc42 is the DAP default, while the older 22-section template remains optional standalone output. Mode and change-reentry helpers are tested; live agent compliance is not claimed. |
| F11 Specialist handoff | Shared conditional contribution contract and 28 specialist output sets carry baseline, typed relationships, evidence, uncertainty, authority and planned/executed verification. Narrow standalone requests do not require full DAP. |
| F12 Resource routing | Entry points explicitly route DAP requirement/checkpoint/ADR templates and the arc42 mapping. Structural/package checks resolve these resources without access to the repository root. |
| F13 Reference drift | Corrected demonstrated WCAG, OWASP, DORA, FinOps, ISO quality-model, abstractness/instability, decision-sensitivity and principle-checklist inconsistencies. Sources are cited in the affected references. This is not a claim that every external link or domain assertion was exhaustively certified. |
| F14 Validation claims | Replaced padding/link-presence checks with actual local resource checks, added negative/lifecycle/package regressions, corrected implementation-status claims and labelled schema-1 examples historical. Description lint is explicitly a heuristic; live-model tests remain separate. |

## Skill-by-skill coverage

All 33 entry points were reviewed. Core workflow changes are distinct from the
conditional contribution envelope applied to specialist outputs.

| Skill | Applied focus |
| --- | --- |
| arch-orchestrator | Three authoring modes, authority boundaries, package routing, convergence and update handoff |
| arch-evaluate | Read-only schema-2 evaluation, isolated runtime paths, evidence-bound results |
| arch-review | Design/process separation, proposal rather than approval, evidenced finding template |
| arch-doc | Explicit DAP arc42 routing and matching numbered section evidence |
| arch-decision | DAP ADR routing, decision-specific sensitivity and close-call criteria |
| arch-governance | Review authority, exception, expiry and delegation contribution |
| arch-test | VER plans with thresholds, targets, ownership and planned/executed distinction |
| arch-security | Threat/control evidence and versioned OWASP mapping |
| arch-compliance | Obligation applicability, control evidence, scope and qualified review |
| arch-ai | Model/context/evaluation versions, action boundaries and risk evidence |
| arch-data | Data ownership, classification, lineage, lifecycle and verification |
| arch-api | Contract/version/error/security implications and compatibility verification |
| arch-integration | Ownership, contracts, failure behavior and integration verification |
| arch-event | Event contracts, ordering/delivery assumptions and failure-path evidence |
| arch-microservices | Boundary/dependency justification and operational trade-offs |
| arch-ddd | Domain evidence, bounded contexts and consistency boundaries |
| arch-patterns | Drivers, alternatives, implications and pattern applicability |
| arch-principles | Contextual rationale instead of blanket abstraction/count rules |
| arch-antipatterns | Evidenced symptoms, causes, trade-offs and remediation checks |
| arch-refactoring | Protected behavior, incremental changes and verification evidence |
| arch-migration | Dependency impacts, sequencing, cutover and rollback evidence |
| arch-cloud | Workload assumptions, boundaries, options and verification plans |
| arch-cost | Unit economics, cost provenance and corrected FinOps framing |
| arch-devops | Delivery/rollback evidence and current DORA metric framing |
| arch-perf | Workload and quality scenarios, budgets and measured/planned distinction |
| arch-resilience | Failure assumptions, recovery objectives and validation plans |
| arch-observability | Signal ownership, objectives and diagnostic verification |
| arch-features | Exposure/experiment scope, rollback and lifecycle accountability |
| arch-fitness | Portable rules, target IDs, planned enforcement and executed evidence |
| arch-metrics | Defined populations and contextual thresholds; corrected metric zones |
| arch-frontend | Rendering/state/ownership boundaries and quality verification |
| arch-accessibility | WCAG edition/level, scoped barriers, manual evidence and internal interfaces |
| arch-usability | Research provenance, journeys, participant context and observed vs inferred findings |

Removed 27 duplicate inline output templates in favor of asset routing. The 28
specialist output sets now include the common contribution/evidence envelope and
domain-specific payload guidance. Instructions remain below the 500-line limit.

## Executed validation

| Check | Result | What it establishes |
| --- | --- | --- |
| python tests/test_skills.py | 33 skills, zero errors | Frontmatter, discovery, naming, line limit, forbidden files and actual local resource resolution |
| python -m unittest discover -s tests -p 'test_*.py' -q | 56 tests passed | Runtime, graph, gates, state/publication, generic adapter contracts and isolated package regressions |
| python tests/test_activation.py | 33 above heuristic threshold; advisory notes retained | Lexical description lint only, not measured activation |
| Available skill-creator quick validator, Python UTF-8 mode | 33 passed | Additional entry-point format validation |
| Default package build | Three public entries, built in .cache/reviewed-default-20260920 | Local isolated distribution; not global installation |
| python -m compileall -q scripts tests; git diff --check | Passed | Python syntax and patch whitespace |

The external quick validator initially hit Windows' default text decoding on two
UTF-8 files; rerunning with Python's UTF-8 mode passed all 33. The repository's own
validator reads UTF-8 explicitly. The description lint's console markers were made
ASCII-safe for Windows. Temporary-directory sandbox permission was needed for an
earlier full test run; approved execution completed successfully.

The final re-review additionally corrected wrong-section reuse in arc42 checks,
external-config comparison in the manifest CLI, pending-review queue handling and
historical-probe compatibility. Their regression cases are included in the count.

## Completion follow-up

A subsequent completion pass found that optional behavioral scenarios still
referenced historical schema-1 fixtures, and that their adapter envelope validator
accepted empty or contradictory assertion results. These were real remaining
repository gaps despite the earlier 56 passing tests.

- Replaced old fixture paths with generated schema-2 identifiers in scenario
  manifest 2.0; kept the external result protocol at 1.0.0.
- Added fresh-directory generation for seven synthetic workspaces: greenfield,
  create, brownfield, interrupted, blocking-review, interview and update.
- Added explicit interview stopping and update preservation scenarios; removed
  obsolete checkpoint paths and incidental prose assertions.
- Validate assertion parameters, safe relative paths, ordered timezone-aware
  timestamps, nonempty executed outcomes and consistent result status. Unavailable
  runs cannot claim executed assertions. This remains envelope validation, not
  proof of live execution or evidence authenticity.
- Corrected fixture documentation and supplied a packaged real-project migration
  guide without silently migrating examples or transferring approvals.

Completion-follow-up suite: **59 tests passed**. Structural validation still covers
all 33 skills. The seven-scenario manifest validates, and the unconfigured adapter
example remains explicitly unavailable. Generated fixtures are in
`.cache/completion-scenarios-20260920`; fresh default/expert distributions are in
`.cache/completion-default-20260920` and `.cache/completion-expert-20260920`.
These are isolated build/test artifacts, not global installations or committed
source. Actual consuming-host execution, real-project policy and approvals are
still external adoption work, not fabricated completion evidence.

## Completion verification

The resumed completion pass reran the full deterministic suite: **59 tests
passed**, all **33 skills** passed structural validation, all 33 descriptions
remained above the advisory heuristic threshold, and `git diff --check` passed.
Fresh default and expert packages were built at
`.cache/final-default-20260920` (three public entries) and
`.cache/final-expert-20260920` (33 entries). No additional implementation fixes
were required by these checks. This verification does not add live-model evidence.

## Release preparation

The release cleanup corrected both test wrappers to run structural validation,
the full contract/package suite and description lint, stop on failure and work
from any current directory. PowerShell and Bash smoke checks confirmed success
and failure propagation. GitHub Actions now defines the same checks and fresh
default/expert builds for Windows/Linux and Python 3.10/3.13, using pinned action
revisions and read-only repository permissions.

The DAP command-line helpers now use consistent formatting and report missing or
malformed inputs as CLI errors. Checkpoint saving rejects non-object state before
touching an existing checkpoint. Six additional regression tests cover these
failure paths, preservation and round-trip behavior. Line-ending policy and
generated-file exclusions keep portable scripts and local artifacts separate.

Local release validation: **65 tests passed**, **33 skills passed** structural
validation, all description heuristics passed their advisory threshold, Python
compilation and patch whitespace checks passed. Maintained documentation links
were checked with no missing local targets. Fresh distributions were built in
`.cache/release-default-20260920` and `.cache/release-expert-20260920`.
Earlier disposable package builds and Python bytecode caches were removed; the
historical audit evidence and generated scenario workspaces were retained.
Hosted CI results are recorded by GitHub Actions, separately from these local
checks. No live-model behavioral evidence is claimed.

## Compatibility and remaining boundaries

The normative framework remains 1.0.0 and rubric 1.0.0. Correcting the incompatible
record contract required schema 2.0.0 and evaluator 2.0.0. Schema-1 scoring is not
available in this runtime; no approval-preserving migration is claimed. Existing
examples remain historical. The current positive generator is clearly synthetic.

The evaluator verifies recorded structure, evidence resolution/binding and
arithmetic, not semantic truth, human identity authentication or production
behavior. Its synthetic positive assessment is an input to tests, not real review
evidence. A human must assess relevance, truth, risk classification and authority.
Instruction routing and deterministic helper tests do not establish live-model
interview, update or review performance on every consuming tool.

Optional consuming-host trials, real-project migration, organization-specific
policy adoption and authoritative license confirmation remain in [TODO](../../TODO.md).
No global skills were replaced and no host-specific installation setup was added.
