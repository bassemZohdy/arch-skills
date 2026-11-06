# Test automation and coverage boundaries

Current counts and operating commands are in [project status](project-status.md); validation levels and authoring boundaries are in [skill testing](skill-testing.md); open host/model adoption work is tracked in [TODO.md](../TODO.md).

## What runs automatically

| Layer | Execution | What a pass establishes |
| --- | --- | --- |
| Structure, links, DAP contracts and package isolation | Every push/PR to main, Linux/Windows, Python 3.10/3.13 | Deterministic repository invariants |
| YAML scenario validation | Same offline CI | Valid assertions, repeat counts, known skills, coverage of all 34 skills and activation cases |
| Public external links | Weekly Monday 06:23 UTC and manual dispatch | Reachability at probe time; 404/410 fail; blocked, rate-limited, timed-out, non-200 and cross-host-redirected responses remain unverified |
| Cited-source freshness | Weekly Wednesday 05:41 UTC and manual dispatch | Broken/changed cited sources and, when a model is configured, grounded claim-versus-source findings filed as deduplicated issues |
| Model response smoke tests | Manual `Optional model response tests` workflow | Selected explicit-skill responses satisfy their assertions |
| Real host tools, automatic activation and DAP lifecycle | Requires a configured host adapter | Actual observed host behavior, only for executed scenarios |
| Diagram source inventory | Offline suite and manual command | Every Mermaid file/fence has a known header and stable source hash; rendering is available only through the manual pinned workflow |

The weekly workflow follows GitHub's scheduling semantics: default-branch
execution, possible delays and possible disabling after prolonged public-repo
inactivity. Keep the manual dispatch option. See the
[GitHub schedule reference](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).

## Source freshness audit

[`.github/workflows/source-audit.yml`](../.github/workflows/source-audit.yml) runs
[`scripts/source_audit.py`](../scripts/source_audit.py) against the external
sources cited by canonical skill content. The awesome-architecture topic hubs are
left out unless you pass `--include-catalog`.

1. **Inventory:** every cited link, with the paragraph or table row that makes the claim.
2. **Fetch and compare:** extract each source's text and hash it. The previous
   run's `state.json` comes from that run's artifact. Each source is classified as
   new, changed, unchanged, broken (404/410) or unverified.
3. **Optional model review:** set the repository variable `SOURCE_AUDIT_MODEL` to
   a GitHub Models model ID. The job then uses `models: read` and its own
   `GITHUB_TOKEN`, with no extra secret. Reviews cover changed sources first, then
   the least recently reviewed claims, up to `--max-reviews`. To use another
   OpenAI-compatible endpoint, set `SOURCE_AUDIT_API_BASE` and the secret
   `SOURCE_AUDIT_API_KEY`. The script never sends the GitHub token to any host
   other than `models.github.ai`.
4. **Issues:** scheduled runs, and manual runs with `create_issues`, open issues
   labelled `source-audit`. Model-derived findings also get `ai-suggested`.
   Issues are deduplicated by a fingerprint marker, including closed ones, and
   capped by `--max-issues`. A claim finding is re-raised only after its source
   content changes.

Fetched pages and model replies are untrusted. A model finding is filed only if
it matches a fixed JSON schema, its verdict is `outdated` or `contradicted` with
medium or high confidence, and its evidence quote appears verbatim in the
fetched source. Issue text is sanitized to neutralize mentions, issue
references, HTML, comments and images. The job runs only on `main`, never on
pull requests, and can write nothing except issues and labels. A filed issue is
a prompt for human review, not a verified correction.

~~~sh
python scripts/source_audit.py --output .cache/source-audit            # deterministic only
SOURCE_AUDIT_MODEL=<model-id> GITHUB_TOKEN=<token>   python scripts/source_audit.py --model-review --max-reviews 3 --output .cache/source-audit
~~~

## Run response tests locally

Build into a fresh directory:

~~~sh
python -m pip install -r requirements.txt
python scripts/build_packages.py --profile expert --output .cache/expert
python scripts/behavioral.py validate
~~~

Set `ARCH_TEST_API_BASE` to the compatible API base ending in `/v1` (not the full
`/chat/completions` endpoint), `ARCH_TEST_MODEL` to your chosen model ID, and
`ARCH_TEST_API_KEY` if authentication is needed. Use your shell/secret manager;
do not put credentials in scenario files. HTTPS is required except for loopback
HTTP servers. Nothing downloads or starts a local model automatically.

~~~sh
python scripts/behavioral.py run --manifest tests/test-arch-evaluate.yaml \
  --packages .cache/expert --output .cache/evaluate-results --limit 0 --max-calls 7
~~~

The same protocol is supported by services such as
[Hugging Face Chat Completion](https://huggingface.co/docs/inference-providers/tasks/chat-completion).
Providers differ: the bundled adapter requires text Chat Completions with
`max_tokens` support and a completed `stop` response. It is not a universal API
adapter. Configure a custom command for other APIs or hosts.

Defaults select at most 10 scenarios with a 30-call ceiling. `--limit 0` selects
all scenarios in the supplied manifests; omit `--manifest` to select from all
41 YAML manifests. The runner rejects a selection exceeding `--max-calls`
before making calls. These are call/output limits, not monetary spending caps.
`ARCH_TEST_MAX_TOKENS` defaults to 2048, with a hard adapter range of 1..16384.
Truncated answers are errors, not successful short responses. There are no hidden
retries. Scenario `runs` means independent observations, not retries until success.
Malformed provider envelopes return structured errors; omitted/null usage remains
unknown rather than being reported as zero tokens.

Reports and per-step request/observation records are written under the fresh
output directory, including package and manifest hashes, timestamps, adapter and
model IDs, observed token usage where supplied, assertion outcomes, repeat pass
rates and omitted-case counts. An incomplete run has `complete: false`.
A provider-reported model alias is not proof of an immutable model revision.
The HTTP adapter records generation settings but never its API key.

Exit 0 means all selected scenarios met their minimum counts. Exit 1 means an
assertion failure, execution error or invalid configuration. Exit 2 means one or
more tests were unavailable. Unavailable attempts never improve the pass rate.

### arch-evaluate calibration suite

`tests/test-arch-evaluate-calibration.yaml` holds 52 typed scenarios whose expected
values follow the packaged DAP scorer (exit-code classification, exact weighted S,
T = min(F, B), N/A authorization, weight validity, readiness and freshness). It is
not part of the 16-call smoke workflow. Run it with `--max-calls 52`. The latest
recorded results are in the [calibration audit](audits/2026-11-02-arch-evaluate-calibration.md).

## GitHub setup

Preview the exact selection and call budget without packages, credentials, writes
or model access:

~~~sh
python scripts/behavioral.py plan --manifest tests/test-regression.yaml \
  --manifest tests/test-arch-evaluate.yaml --limit 0 --max-calls 16
python scripts/behavioral.py plan --manifest tests/test-skill-boundaries.yaml \
  --limit 0 --max-calls 39
~~~

The 39 boundary scenarios include one targeted case per skill plus five positive
controls. They use typed JSON assertions and remain unexecuted live candidates
until run against a configured model. Passing them would not establish general
skill reliability. Offline CI also checks the manual smoke workflow's declared
budget against its actual manifest selection, so scenario growth cannot silently
break that command again.

Set repository variables `ARCH_TEST_API_BASE` and `ARCH_TEST_MODEL`; add repository
secret `ARCH_TEST_API_KEY` if required. Run **Optional model response tests** on
`main`. It executes eight scenarios with 16 total calls, a 2048-token output
limit per call and a 15-minute job timeout. It uploads reports for 14 days even
when tests fail. Missing configuration produces an unavailable report and a
non-success exit. No paid model calls run automatically on PRs or scheduled jobs.

**Audit external links** is separate from release CI so transient network
conditions do not block offline validation. It retains evidence for 30 days.
No issues or messages are posted automatically. A successful audit means no
confirmed broken links, not that all requests were verified.

## Diagram checks

The repository includes 33 Mermaid files or fenced blocks. Run the deterministic
inventory locally with `python scripts/check_diagrams.py --output
.cache/diagram-static`; it validates headers and records source hashes without
requiring a renderer. For release evidence, manually trigger the pinned Mermaid
workflow at [`.github/workflows/diagrams.yml`](../.github/workflows/diagrams.yml).
The workflow installs its browser and uploads SVGs plus the JSON report; a local
static pass must not be described as rendered output. The Mermaid CLI version is
pinned inline in that workflow (`@mermaid-js/mermaid-cli@11.17.0`); Dependabot
does not track it, so bump it manually when renewing renderer evidence.

## Custom host adapter protocol

Pass `--adapter-command` as a JSON argv array, for example
`["python", "/absolute/path/to/my_adapter.py"]`. It runs without a shell in a
fresh workspace per scenario repetition. All steps in one repetition share that
workspace and conversation history. Workspaces are isolation for test data, not
an OS security sandbox; configure host permissions and descendant-process cleanup
in the adapter. Use absolute script paths and only trusted adapters.

Read one JSON object from stdin containing `protocol_version: "1.0"`, `mode`,
`workspace`, `messages` and `timeout` in seconds. Explicit mode also provides
`skill_root` (the built package); activation mode provides `skills_root` (the
selected package profile root) and asks the host to report which skills it actually loaded.
Expected assertions are deliberately not sent to the model. Emit one JSON object
to stdout:

~~~json
{
  "status": "ok",
  "response": "Observed assistant answer",
  "execution_mode": "host",
  "adapter": {"id": "your-host-adapter", "version": "pinned-version"},
  "model": {"id": "model-id", "version": "observed-version"},
  "generation": {"max_output_tokens": 2048},
  "capabilities_used": ["file_write"],
  "skills_used": ["arch-api"],
  "resources_read": ["arch-api/references/rest-patterns.md"],
  "total_tokens": 1234
}
~~~

Use `execution_mode: "response-only"` with `capabilities_used: null` and
`skills_used: null` when no host tools or skill-loading events were observed.
Capability and skill observations must come from actual host traces,
not a model's claim or a synthetic tool name. The runner checks adapter structure,
not its honesty. Retain host traces in the workspace. Omit `total_tokens` if
unmeasured; zero must not stand in for unknown. For environment unavailability or
execution errors, emit `status: "unavailable"` or `"error"` with `reason`.
Do not emit secrets in responses, reasons or traces. Stderr is not retained.

Supported assertions: case-insensitive `contains`, `not_contains`, `contains_any`;
`json_equals` with JSON Pointer and typed expected `value` (numbers compare by value, so 50 equals 50.0; booleans and strings never equal numbers); normalized
`capability_used`, `skill_used` and `skill_not_used`; `resource_read` with a canonical
`<skill>/<relative-resource>` path; and `token_usage_under` (strictly less than total reported
input plus output tokens). Missing required capability/token observations are
unavailable, not passes. JSON answers must be raw JSON, not fenced Markdown.

The YAML suite supports explicit skill execution and activation mode. In activation
mode, the adapter receives `skills_root` and must return a host-observed
`skills_used` list. The runner does not treat a model's claim as a skill trace.
The suite also supports a scenario-level skill override, multiple steps, `runs`
and integer `min_passes`. Two successes out of three are `runs: 3, min_passes: 2`.
There is no ambiguous rounded `0.67` threshold. Unknown settings, duplicate YAML
keys and unsupported assertions fail validation. So does a `contains` or
`contains_any` value that already appears in its own prompt: an answer that
echoes the question must not satisfy a keyword check, so assert guidance the
prompt does not state.

This response/host transport is separate from the versioned
[DAP adapter contract](dap-adapter-contract.md). The seven JSON DAP scenarios
are not executed by this runner. They need fixture setup, artifact verification,
checkpoint/review integration and a host adapter, rather than text-only checks.

Run the stronger DAP completeness check after `validate-result`:

~~~sh
python scripts/dap_adapter.py validate-execution \
  result.json tests/dap-adapter-scenarios.json --workspace .cache/dap-run
~~~

It matches the result to its manifest scenario, requires one uniquely identified
outcome for every requested assertion, and verifies every evidence path exists
inside the execution workspace. An unavailable result remains explicitly
unavailable and does not need fixture evidence.

Completed reports can be compared before accepting a change:

~~~sh
python scripts/compare_behavioral.py baseline/report.json candidate/report.json \
  --output .cache/behavioral-diff.json
~~~

The comparator checks adapter, model, execution mode and recorded generation
settings on every step of every repetition, plus case selection, manifest and
repeat configuration. Legacy reports with unknown generation settings need a new
baseline. The runner reports within-case execution drift as an error.
Use `--allow-package-change` to compare changed skills while retaining the same
execution and scenario configuration. Use `--allow-configuration-change` only
for an intentional new baseline; neither option permits internally mixed execution
identities. Candidate errors fail, and unavailable observations never become passes.

## Portable resource and activation tests

Keep integrations for individual AI coding tools outside this repository. Supply
an external command implementing the protocol above through `--adapter-command`.
The canonical packages and scenarios do not require a specific executable,
installation directory, model family or vendor event format.

`tests/test-reference-loading.yaml` contains two explicit-skill scenarios that
require observed reads and typed decisions. Build the expert profile for those
cases. `tests/test-default-activation.yaml` covers the three public entrypoints;
build the default profile to test that discovery surface. The expert activation
manifest remains available for specialist routing.

Normalize observed resource identities to `<skill>/<relative-resource>` paths,
independent of installation location. Collect evidence from the host's actual
resource access mechanism. If that mechanism cannot establish a read, report
`resources_read: null`; do not infer access from a model's answer. Likewise,
report `skills_used: null` if the host cannot provide a complete activation trace:
an incomplete positive list cannot establish `skill_not_used`.

Record effective generation settings as adapter-defined JSON. The runner compares
them without imposing a vendor's parameter names or defaults. Missing settings
remain unknown and cannot establish a comparable baseline. `--max-calls` bounds
adapter invocations; internal host turns and spend need limits in the external
adapter. Configure its permissions and process cleanup there as well.

These scenarios are validated offline; no live reference-loading or activation
baseline was established in this review.

## Open coverage boundaries

Repository automation covers deterministic checks, fixture validation,
result-envelope checks and compatible report comparison; it is not exhaustive.
Live model quality,
host-observed activation, DAP lifecycle execution and assertion calibration require
an external adapter and remain tracked in [TODO.md](../TODO.md).
