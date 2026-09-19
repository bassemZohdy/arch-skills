# Evaluation contract

The evaluator reads a project root containing requirements.json, design-elements.json,
decisions.json, traceability.json and process/{config,assessment,state,reviews}.json.

Each check has result pass, fail, unknown or not_applicable. Unknown is included in
the denominator and receives zero credit. Not applicable is excluded only when the
record includes reason and authorized_by.

Q, D and A are the passed applicable checks divided by all applicable checks. Forward
coverage is active requirements with a requirement_to_design link divided by active
requirements. Backward coverage is significant active design elements with a
design_to_requirement link divided by significant active design elements.
T = min(forward, backward). Empty required populations are not assessable.

S = wQ*Q + wD*D + wT*T + wA*A. Configuration weights must be non-negative, sum
to one and make traceability the largest weight. Scores are rounded only for display.

The readiness gate is independent of S. Convergence, required review dispositions,
valid configuration and structural integrity must pass. Security implications require
an approved security review when configured. Reports include the frozen input manifest
and are stale when any assessed input changes. Generated reports and publication
receipts are excluded from the assessed hash.

