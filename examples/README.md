# Example status

The checked-in greenfield, brownfield, interrupted and blocking-review directories
are historical schema-1 regression inputs retained for the original audit. They
are not ready architectures, current schema-2 demonstrations or transferable
stakeholder approvals. The current runtime reports unsupported versions rather
than silently migrating or rescoring them.

Generate the current, explicitly synthetic positive fixture in a fresh directory:

~~~sh
python tests/dap_fixture.py --output .cache/dap-example
python scripts/dap_validate.py .cache/dap-example
~~~

Its semantic assessments and human identities are test inputs, not real approvals.
Current executable negative, interruption, change and review cases are in
`tests/test_dap.py`; package isolation cases are in `tests/test_packages.py`.
Reconstruct actual evidence and obtain new authorized dispositions before adapting
any example to a real architecture. There is no automatic schema migration.

For the complete current synthetic suite, run
`python tests/dap_fixture.py --suite --output .cache/dap-scenarios` using a fresh
directory. See [the adapter contract](../docs/dap-adapter-contract.md) for selecting
these fixtures and complete built packages in optional behavioral runs.
