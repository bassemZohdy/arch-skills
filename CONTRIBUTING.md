# Contributing

Thank you for helping improve the architecture skills. Keep changes portable,
host-neutral and useful to a reader who has not seen this repository before.

## Before opening a pull request

1. Read [AGENTS.md](AGENTS.md) and the relevant skill entry point.
2. Keep each `SKILL.md` under 500 lines and put detailed material in
   `references/` or reusable output files in `assets/`.
3. Keep host-specific commands, model names and adapter behavior outside the
   canonical skill instructions.
4. Update tests and documentation when a contract, package profile or public
   workflow changes.

Install the Python dependencies and run the complete offline checks from the
repository root:

```powershell
python -m pip install -r requirements.txt
./run-tests.ps1
```

On Linux or macOS, run `bash run-tests.sh`. The checks validate all skills,
exercise the DAP contracts and isolated package runtime, run activation lint,
and stop on failure. Build packages into a fresh destination:

```text
python scripts/build_packages.py --profile default --output .cache/packages-default
python scripts/build_packages.py --profile expert --output .cache/packages-expert
```

Do not install source skills globally as part of tests. The builder copies the
shared framework and runtime into a portable package; use that package for
installation or isolated host testing.

## Pull requests

Describe the user-visible behavior and the evidence supporting it. Include the
scope of the change, validation commands and any limitation that remains. Keep
unrelated formatting or generated cache files out of the patch. A maintainer
may request changes to preserve skill boundaries, portability or evidence
semantics.

## Links and skill connections

Run `python scripts/check_links.py` for document-relative Markdown targets and
anchors. `python tests/test_skills.py` also walks resource pointers from every
entry point and rejects unknown skill names. Link supporting resources from a
reachable instruction, and resolve local helper scripts from the specialist root.

External probes are explicit and separate from offline CI:

```sh
python scripts/check_links.py --external --output .cache/link-audit.json
```

Keep access-denied, throttled and timed-out URLs unverified. Repair a moved link
from the publisher's current page/source tree, not a guessed slug. Templates and
synthetic fixtures must not claim approval or product evaluation evidence.
