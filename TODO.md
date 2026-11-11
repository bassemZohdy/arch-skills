# Follow-up work

Only unfinished work is listed here. Current implementation status, available commands
and repository capabilities are documented in [docs/project-status.md](docs/project-status.md).

## Architecture evaluation platform reuse (proposed)

The reusable knowledge belongs in this repository; the future web application
owns tenants, users, uploaded architectures, profile administration, runtime
persistence and reports. The design is captured in
[ADR-0001](docs/adr/0001-reusable-architecture-knowledge.md) and
[architecture review model](docs/architecture-review-model.md).
These tasks are not implemented or approved governance policy.

- [ ] **Catalog schema and migration:** create a standalone versioned review
  reference/rule/decision-option schema. Keep existing DAP `criteria-catalog.json`
  and its rubric/version unchanged unless a separately tested migration is agreed.
- [ ] **Reusable architecture knowledge:** curate and validate reference artifact
  categories, evaluation dimensions, decision areas with exclusive options,
  pattern/anti-pattern relationships and source provenance. Avoid pretending
  this is a complete or normative industry enumeration.
- [ ] **Profile resolver:** organization defaults + scoped profile overrides,
  applicability, single-select expected options per decision area, enforcement
  levels, exceptions and immutable evaluation snapshots. Do not allow profiles
  to silently drop binding obligations.
- [ ] **Design-review executor:** implement and test rule evaluation, evidence
  locators, applicability/exclusion, pass/fail/unknown/not-applicable, finding
  traceability and pass/fail/needs-review gates separately from DAP readiness.
- [ ] **Create and update reuse:** demonstrate that authoring, change-impact
  analysis and design review use the same versioned catalog without duplicating
  rules or rewriting approved ADRs.
- [ ] **Fitness function mapping:** map automatable rules to document, static
  source and runtime verification, preserving planned-vs-executed distinction
  and human adjudication for non-automatable checks.
- [ ] **Consumer API contracts:** specify app-neutral request/result envelopes,
  frozen inputs, profile/catalog identity and version, structured findings,
  source/evidence references, gate results, unavailable status, and auth boundary.
- [ ] **Test fixtures:** add representative modular-monolith and microservices
  architectures with a variety of profile selections, conditional applicability,
  conflicts, exceptions, insufficient evidence, unapproved profile and update
  invalidation. Include property/invariant tests for gate precedence and unknowns.
- [ ] **Packaging and validation:** increment plugin version, rebuild generated
  Claude/Codex plugin with `scripts/build_plugin.py`, run the full offline
  suite, and record actual results. Do not hand-edit generated `plugins/` files.
- [ ] **Live verification:** test skills with independent real host sessions,
  record evidence and quality baselines, and separate results from synthetic tests.

## Live model and host integration

- Configure the endpoint/model and run the 16-call smoke workflow; record the first
  real baseline. Synthetic adapters and mocked HTTP are not live skill-quality evidence.
- Execute the seven DAP lifecycle scenarios through an external host adapter,
  including fixture setup, artifact verification, preserved history and baseline
  immutability.
- Run the two reference-loading cases and default/expert activation manifests
  through external adapters that supply actual resource and activation evidence.
  Keep host-specific trace collection and configuration outside the repository.

## Quality calibration and release evidence

- Calibrate keyword assertions on real outputs; move priority cases to typed
  decisions, artifact checks or reviewed semantic rubrics. Start with the
  prompt-echo cases the lint above will flag.
- Compare repeated baseline/candidate runs with identical pinned model and host
  settings before introducing a live-quality release threshold. Two or three samples
  are smoke tests, not a reliability estimate.

## Consuming-project adoption

- Run the host-neutral scenarios on each intended host and record actual model,
  adapter, routing and artifact versions.
- For real schema-1 projects, plan an explicit migration with owners; capture missing
  evidence and renew affected assessments instead of transferring approvals.
- Adopt project-specific review identities, thresholds, cadence and retention. The
  configuration example deliberately contains unapproved placeholders.

## External verification

- Enable the model step of the source freshness audit: set the repository variable
  `SOURCE_AUDIT_MODEL` to a GitHub Models model ID, run the workflow manually with
  `create_issues` off, review `report.json`, then let scheduled runs file issues.
  The model path is covered by offline tests only and has not run against a live endpoint.
- Recheck the 6 [currently unverified URLs](docs/audits/2026-11-06-link-recheck.json)
  (private Google Doc, EUR-Lex challenge page, eCFR block redirect, hhs.gov and two
  iso.org pages) with authorized access or another network; replace the eCFR link
  once a stable URL is confirmed. Do not treat blocked, rate-limited or timed-out
  probes as broken links.
- Re-verify the dated "no dedicated section" notes in each
  `references/awesome-architecture.md` by hand: the site's section list is rendered
  client-side and could not be checked automatically on 2026-11-06.
- Dependabot cannot see the inline Mermaid CLI pin in `.github/workflows/diagrams.yml`
  (documented in `docs/test-automation.md`); track it in a `package.json` if
  automated bumps are wanted.

## Diagram rendering coverage

- Run the manually triggered Mermaid renderer workflow and retain successful
  SVG/report evidence when GitHub can download its headless browser.
- Add equivalent pinned PlantUML and Draw.io renderer jobs only if those formats
  become required release evidence; the current static inventory covers all
  Mermaid sources.

## Publishing and distribution

Done 2026-11-07: manifests live in this repository (decision recorded in AGENTS.md); the
plugin is generated by `scripts/build_plugin.py` from the built default packages and checked
in `run-tests.sh`; Claude (`claude plugin validate`) and Codex (codex-cli 0.167.0) installs
verified; single-skill `npx skills add` verified from the built plugin folder.

- Set the GitHub repository description and topics (for example agent-skills,
  software-architecture, architecture-decision-records, claude-code). The session's GitHub
  proxy blocks repository settings writes, so this is an owner step. (#12)
- Owner submits the default profile to the Anthropic plugin directory (portal login and
  terms acceptance) and records the reference here. The directory validator also suggests
  a square PNG icon (512 to 2048 px) in the plugin. (#13)
- After the first push, confirm the GitHub-URL form of `npx skills add` from a clean
  machine: `npx skills add https://github.com/bassemZohdy/arch-skills/tree/main/plugins/arch-skills --skill arch-review`. (#11)
