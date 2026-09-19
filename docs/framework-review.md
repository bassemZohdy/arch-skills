# Framework review and corrections

Reviewed on 2026-09-19 against repository baseline `8fe7e13a04af19d9c0ffc187272ecb8f3b8dba5a`.

The framework is suitable as a specification for implementation after the corrections below. This is a document review, not evidence that the process is implemented or that an architecture has passed it.

The [original Google document](https://docs.google.com/document/d/1CiBfGY_tBrFVOTAIAnqjK4VNCDwZza0BV14i-dgWUpQ) has been corrected in place. The [repository specification](deterministic-architecture-process.md) is its versioned implementation reference. Future semantic changes must reconcile both representations explicitly; automatic synchronisation is not currently implemented.

## Findings resolved in the specification

| Finding | Impact | Correction |
| --- | --- | --- |
| Determinism implied a unique or repeatable LLM design | An implementation could promise results it cannot guarantee | Define deterministic gates and arithmetic over frozen evidence; preserve uncertainty in semantic judgments |
| Claimed architecture lacks a repeatable design process | Overstated novelty and omitted established design methods | Position the framework as an integration and acknowledge Attribute-Driven Design |
| C4 described as static only; arc42 treated as a final export | Incomplete view of both approaches | Include C4 dynamic/deployment views and maintain arc42 throughout design |
| Eleven project checks attributed directly to ISO 29148 | Unsupported standards-conformity implication | Label a project checklist, restore individual completeness, correctness and conformity, and require a separate assessment for formal conformity claims |
| A quiet round counted as convergence | Silence, missing stakeholders or exhaustion could produce false readiness | Define a round, explicit baseline confirmation, blocking questions, reset conditions and a bounded blocked outcome |
| Functional questions necessarily preceded quality constraints | Security, scale or recovery drivers could arrive too late | Elicit functional and quality concerns together as dependencies appear |
| MoSCoW exclusions equated to waivers | Mandatory obligations could be silently dropped | Separate timeframe priority, applicability and authorised exceptions; remove universal numeric bucket weights |
| Human review primarily saw ADRs | A set of locally plausible decisions might form an incoherent design | Review draft views, requirements and verification plans alongside ADRs |
| Confidence thresholds had no calibration | LLM confidence could become false approval evidence | Use observable risk, reversibility, impact and explicit authority |
| Accepted ADRs could be revised in place | Decision history and approval evidence could be lost | Preserve accepted reasoning and use reviewed superseding records |
| A conflict with a Must have meant the requirement was wrong | The process could rewrite valid needs to fit a flawed design | Diagnose design defect versus authorised requirements change and re-enter the appropriate stage |
| Interview state existed only in session memory | Interruptions would lose answers and gate evidence | Persist records and atomic checkpoints after each round |
| A separate skill was described as independent enforcement | Role separation could be mistaken for a technical guarantee | Separate authoring and assessment, use frozen inputs and structural validators, preserve human adjudication |
| Completeness percentage had no formula or denominator rules | Different runs could report incomparable or inflated scores | Define criteria populations, pass/fail/unknown treatment, F/B coverage, conservative aggregation, zero-denominator handling and a worked example |
| Forward design traceability implied software was built | Documentation could be mistaken for execution evidence | Separate design coverage, implementation coverage and executed verification |
| The evaluator changed the document revision it assessed | Publishing could immediately invalidate its own report | Hash assessed inputs while excluding generated evaluation output; separate publication metadata |
| Shared version labels were said to prevent drift | A label alone cannot enforce compatibility | Add schema/rubric/configuration versions, runtime checks and unsupported historical-version handling |
| Configuration mixed silent defaults and fail-closed rules | Missing values had ambiguous effects | Define scoped consequences and no automatic scoring defaults |

The original draft's broader research examples are no longer treated as verified evidence. The retained LLMREI example is explicitly limited to its study setting. No quantitative result from that study is used as a production gate.

## Repository gaps requiring implementation

The repository now contains the evaluator, persistent process contracts and deterministic completeness calculator. The implementation is a reference baseline; deeper host-specific orchestration and live-model scenarios remain bounded by each host's capabilities.

| Existing path | Observed gap | Planned resolution |
| --- | --- | --- |
| `skills/arch-orchestrator/SKILL.md` | Generic ten-step workflow; no auditable convergence or recovery contract | Integrate the six-stage framework and durable state while retaining specialist selection |
| `skills/arch-orchestrator/assets/shared-context-template.md` | Broad free-text fields; orchestrator can ratify decisions without defined human authority | Add stable IDs, provenance, baseline state and explicit acceptance authority |
| `skills/arch-orchestrator/assets/solution-architecture-template.md` | A separate 22-section structure | Map its useful content into arc42 without losing concerns |
| `skills/arch-doc/SKILL.md` | ADR immutability sentence is ambiguous; lightweight ADR examples omit framework fields | Align lifecycle and templates with the shared contract |
| `skills/arch-decision/SKILL.md` | Hard cap of four gates, universal do-nothing prompting, and technology-gate exemption | Make mandatory constraints exhaustive; evaluate the status quo fairly; allow only evidenced non-applicability |
| `skills/arch-decision/SKILL.md` | Fixed ±10 sensitivity perturbations may make weights negative | Bound and renormalise decision-specific perturbations; keep DAR scores separate from completeness scores |
| `skills/arch-orchestrator/SKILL.md` | Conflict precedence could let a preference appear to override a binding obligation | Make binding constraints eligibility rules and escalate conflicts rather than silently rank them away |
| `skills/arch-governance/` | General guidance without this framework's executable configuration contract | Define scoped fail-closed review policy and recorded exceptions |
| `tests/` | Structural and behavioural scenarios do not establish the new framework's behavior | Add targeted deterministic and behavioural fixtures tied to backlog acceptance criteria |
| `README.md` and `TODO.md` | Status needed to reflect the implemented reference baseline | Document available commands, evidence and remaining host-specific limits |

## Evidence and limits

Primary references used for factual corrections:

- [C4 diagrams](https://c4model.com/diagrams): supporting dynamic and deployment views.
- [arc42 overview](https://arc42.org/overview/): twelve-section documentation structure and tailoring.
- [SEI Attribute-Driven Design](https://www.sei.cmu.edu/library/attribute-driven-design-add-version-20/): established architecture design method.
- [ISO 29148 catalogue](https://www.iso.org/standard/72089.html): requirements-engineering scope; not a substitute for a licensed clause-level conformity review.
- [Agile Business Consortium MoSCoW](https://www.agilebusiness.org/resource/what-is-moscow-prioritization/): delivery priorities within a timeframe.
- [AWS ADR process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html): decision lifecycle and supersession.
- [SEI ATAM](https://www.sei.cmu.edu/library/atam-method-for-architecture-evaluation/) and [ISO 42030](https://www.iso.org/standard/73436.html): architecture evaluation context.
- [LLMREI paper](https://arxiv.org/html/2507.02564v1): bounded research evidence for AI interviewing.
- [Agent Skills specification](https://agentskills.io/specification): portable skill packaging, not workflow enforcement.

The scoring formula, criterion catalogue, checkpoint contract and approval policy are project-defined. Organisational thresholds, reviewer identities and weights remain adoption-time configuration. The example weights in the framework are not an approved configuration.

The reference implementation is complete for the contract and fixture scope. [TODO.md](../TODO.md) records completion evidence; [the implementation plan](framework-implementation-plan.md) describes the implemented boundaries and future host-specific extensions.
