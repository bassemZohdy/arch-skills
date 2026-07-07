# AI Architecture Patterns — Reference

Detailed guidance for the patterns summarized in SKILL.md.

## RAG Pipeline Design

### Chunking Strategies

| Strategy | Description | Best For |
|----------|-------------|----------|
| **Fixed-size** | N tokens with overlap | Uniform prose |
| **Structure-aware** | Split on headings, paragraphs, code blocks | Docs, wikis, codebases |
| **Semantic** | Split at topic boundaries via embeddings | Long unstructured text |
| **Parent-child** | Retrieve small chunks, return larger parent | Precision + context |

Typical starting point: 300-800 token chunks with 10-20% overlap, structure-aware where the corpus has structure.

### Retrieval Quality Checklist

- [ ] Hybrid search (vector + BM25) evaluated against pure vector
- [ ] Reranker applied when top-k precision matters
- [ ] Metadata filters (date, source, tenant) applied before ranking
- [ ] Embeddings refreshed when documents change
- [ ] Retrieval evaluated separately from generation (recall@k, MRR)

### Prompt Assembly

Order context by relevance, put instructions before context, and state grounding rules explicitly:

```
You answer only from the provided context. If the context does not
contain the answer, say so. Cite the source id for every claim.

<context>
[ranked chunks with source ids]
</context>

Question: [user question]
```

## Agent Design

### Loop Skeleton

```
while not done and steps < max_steps and cost < budget:
    action = model.plan(state, tools)
    result = execute(action)          # permission-checked, logged
    state = update(state, result)
```

### Tool Design Rules

1. Typed input/output schemas; validate before execution
2. Names and descriptions written for the model, not the developer
3. One clear purpose per tool; avoid mega-tools with mode flags
4. Return errors as structured data the model can recover from
5. Destructive operations require confirmation or elevated approval

### Multi-Agent Caution

Multi-agent systems multiply token cost and failure modes. Justify them only when:
- Subtasks are parallelizable and independent, or
- Context isolation is required (one agent's context would pollute another's)

## Model Selection

| Factor | Guidance |
|--------|----------|
| **Quality ceiling** | Prototype with the strongest model; optimize down later |
| **Latency** | Smaller models or streaming for interactive paths |
| **Cost** | Tier: route simple requests to small models |
| **Privacy** | Self-hosted/open-weight when data cannot leave boundary |
| **Structured output** | Prefer models/APIs with native JSON schema support |

## Evaluation Methods

| Method | Cost | Reliability | Use For |
|--------|------|-------------|---------|
| **Exact / regex match** | Low | High | Extraction, classification |
| **Semantic similarity** | Low | Medium | Paraphrase-tolerant answers |
| **LLM-as-judge** | Medium | Medium (calibrate) | Open-ended quality |
| **Human review** | High | High | Calibration, high-stakes |

### Eval Set Construction

1. Start with 20-50 real examples covering the distribution of inputs
2. Include known-hard cases and past failures
3. Label expected outputs or scoring rubrics
4. Re-run on every prompt, model, or retrieval change
5. Grow the set from production incidents

## Failure Handling

| Failure | Mitigation |
|---------|------------|
| Timeout | Timeout + retry with backoff; degrade to cached/simpler answer |
| Malformed output | Schema validation + one repair retry |
| Refusal | Detect and route to fallback flow |
| Hallucination | Grounding, citations, confidence signals |
| Provider outage | Multi-provider abstraction or graceful degradation |

## Security Threat Model for AI Features

| Threat | Vector | Control |
|--------|--------|---------|
| **Prompt injection** | Retrieved docs, user input, web content | Treat as data; strip/flag instructions; least-privilege tools |
| **Data exfiltration** | Model output channels, tool calls | Output filtering, egress controls |
| **Excessive agency** | Over-permissioned tools | User-scoped permissions, approval gates |
| **Denial of wallet** | Unbounded loops, long inputs | Spend caps, step limits, input limits |
| **Training data leakage** | PII in prompts sent to third parties | Redaction, data processing agreements |
