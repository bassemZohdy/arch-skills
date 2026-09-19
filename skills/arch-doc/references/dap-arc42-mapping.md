# DAP to arc42 mapping

The deterministic process uses arc42 as the default architecture description. The
existing solution-architecture template remains useful for standalone requests;
the mapping below prevents the two structures from drifting when DAP is active.

| Existing concern | arc42 destination |
| --- | --- |
| Business context, summary and drivers | 1 Introduction and Goals |
| Requirements and constraints | 1 Introduction and Goals; 2 Constraints |
| System context | 3 Context and Scope |
| Architecture style, alternatives and strategy | 4 Solution Strategy |
| Components and data ownership | 5 Building Block View |
| Integration scenarios and failure flows | 6 Runtime View |
| Deployment topology | 7 Deployment View |
| Security, resilience, performance, operations and delivery | 8 Crosscutting Concepts |
| ADRs and technology decisions | 9 Architecture Decisions |
| Quality scenarios | 10 Quality Requirements |
| Risks and technical debt | 11 Risks and Technical Debt |
| Terms and IDs | 12 Glossary |

The RTM, checkpoint, reviews and exceptions remain durable supporting records and
are linked from appendices. Generated evaluation output is dated and excluded from
the input manifest used to assess the baseline.
