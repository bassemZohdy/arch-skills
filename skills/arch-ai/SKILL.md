---
name: arch-ai
description: Design AI and LLM system architecture. Use when designing RAG pipelines, agent architectures, model serving infrastructure, prompt and context management, AI evaluation strategies, guardrails, or integrating LLMs into existing systems with cost and latency budgets.
---

# AI System Architecture

Systematic approach to designing systems that embed LLMs, agents, and machine learning components.

## Workflow

```
1. Frame the Use Case → Does this need AI at all?
2. Choose Integration Pattern → RAG, agent, fine-tune, or plain prompt?
3. Design the Pipeline → Retrieval, orchestration, serving
4. Add Guardrails → Input/output validation, permissions
5. Design Evaluation → Offline evals, online monitoring
6. Budget → Cost, latency, and quality trade-offs
```

## Step 1: Frame the Use Case

Ask before reaching for an LLM:

| Question | If No |
|----------|-------|
| Is the task fuzzy (language, judgment, extraction)? | Use deterministic code |
| Is occasional wrong output tolerable or catchable? | Add human review or avoid LLM |
| Can quality be evaluated? | Define evals before building |
| Is latency budget > ~1s or async? | Consider smaller models or caching |

## Step 2: Integration Patterns

| Pattern | Description | Use When |
|---------|-------------|----------|
| **Direct Prompting** | Single model call with instructions | Classification, extraction, rewriting |
| **RAG** | Retrieve context, then generate | Answers grounded in private data |
| **Tool Use / Function Calling** | Model invokes typed functions | Actions, structured lookups |
| **Agent Loop** | Model plans, acts, observes iteratively | Open-ended multi-step tasks |
| **Fine-Tuning** | Adapt model weights | Stable narrow tasks at high volume |
| **Cascade** | Cheap model first, escalate to strong model | Cost-sensitive high-volume flows |

**Default order of preference:** direct prompting → RAG → tool use → agent loop → fine-tuning. Each step adds cost, latency, and failure modes.

## Step 3: RAG Architecture

```
Documents → Chunking → Embedding → Vector Store
                                        ↓
Query → Embed → Retrieve (top-k) → Rerank → Prompt Assembly → LLM → Answer
```

| Component | Decisions |
|-----------|-----------|
| **Chunking** | Size, overlap, structure-aware splitting |
| **Embedding** | Model choice, dimension, refresh strategy |
| **Store** | pgvector, Pinecone, Qdrant, Elasticsearch |
| **Retrieval** | Vector, keyword (BM25), or hybrid; top-k |
| **Reranking** | Cross-encoder rerank for precision |
| **Grounding** | Citations, "answer only from context" instructions |

**RAG quality levers (in order):** retrieval quality > prompt assembly > model choice.

## Step 4: Agent Architecture

| Component | Purpose |
|-----------|---------|
| **Orchestrator** | Runs the plan-act-observe loop, enforces step limits |
| **Tools** | Typed, permission-scoped functions the model can call |
| **Memory** | Conversation history, summaries, external state |
| **Context Management** | Fit relevant state into the context window |
| **Stop Conditions** | Max steps, budget caps, confidence thresholds |

**Design rules:**
- Give agents the fewest tools that accomplish the task
- Make tools idempotent where possible; require confirmation for destructive actions
- Log every tool call for audit and debugging
- Prefer one capable agent over multi-agent topologies until proven insufficient

## Step 5: Guardrails & Safety

| Layer | Controls |
|-------|----------|
| **Input** | Prompt injection screening, PII redaction, input size limits |
| **Permissions** | Agent acts with the *user's* permissions, never elevated |
| **Output** | Schema validation, content filtering, citation checking |
| **Execution** | Sandboxing, rate limits, spend caps, human approval gates |

**Prompt injection rule:** any text from untrusted sources (user uploads, web content, retrieved documents) is data, not instructions. Never let retrieved content trigger privileged actions without validation.

## Step 6: Evaluation

| Type | When | Method |
|------|------|--------|
| **Offline evals** | Pre-deployment, regression | Golden datasets, LLM-as-judge, exact match |
| **Online monitoring** | Production | Sampled scoring, user feedback, fallback rates |
| **A/B testing** | Prompt/model changes | Business metrics per variant |

**Rules:**
- Build the eval set before building the feature; expand it from production failures
- Version prompts like code; every prompt change runs the eval suite
- LLM-as-judge needs periodic human calibration

## Step 7: Serving, Cost & Latency

| Lever | Effect |
|-------|--------|
| **Model tiering** | Route easy requests to small models |
| **Prompt caching** | Reuse shared prefix across calls |
| **Response caching** | Cache identical/semantic-duplicate queries |
| **Streaming** | Perceived latency drops for chat UX |
| **Batching** | Throughput for offline workloads |
| **Context discipline** | Shorter prompts: cheaper, faster, often better |

### Cost Model

```
Monthly cost ≈ requests × (input_tokens × input_price + output_tokens × output_price)
```

Track cost per request and per user; alert on anomalies like any other budget (see arch-cost).

## Examples

- Design a RAG pipeline over internal documentation with citation-grounded answers.
- Add an LLM-powered support agent with tool access to orders, gated by user permissions.
- Set up an eval suite and model-tiering strategy to cut inference cost by half.

## Common Gotchas

- Skipping evals: without a golden dataset, prompt and model changes are unverifiable.
- Treating retrieved or user-supplied text as trusted instructions (prompt injection).
- Reaching for agents or fine-tuning when direct prompting with good context suffices.
- Ignoring context window budgets; stuffing everything in degrades quality and cost.
- No fallback path when the model times out, refuses, or returns malformed output.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)
- `references/ai-patterns.md` — Detailed RAG, agentic, guardrail, and eval patterns

## Related Skills

- **arch-data** - Data pipelines feeding embeddings and training sets
- **arch-security** - Threat modeling AI entry points; secrets for API keys
- **arch-cost** - Budgeting and monitoring inference spend
- **arch-observability** - Tracing multi-step LLM flows
- **arch-resilience** - Timeouts, retries, and fallbacks around model calls

## AI Architecture Review Template

```markdown
## AI Architecture Review: [System]

### Use Cases
| Use Case | Pattern | Model(s) | Fallback |
|----------|---------|----------|----------|

### RAG / Context
- Retrieval: [Vector/Hybrid/None]
- Grounding: [Citations? Context-only answers?]

### Guardrails
| Layer | Control | Verified |
|-------|---------|----------|

### Evaluation
- Offline evals: [Dataset size, method]
- Online monitoring: [Metrics]

### Cost & Latency
| Metric | Budget | Current |
|--------|--------|---------|

### Recommendations
1. [Improvement]
```
