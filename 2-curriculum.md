# Agentic AI Engineer: Project-Based Roadmap (100% free)

Each module = Concepts -> Code-along -> **You write it** -> Checkpoint -> Project in GitHub.
Suggested pace: 1 module per 3-7 days. Total about 14-18 weeks part-time.

## Free toolbox
- LLMs: Groq free tier (fast Llama), Google AI Studio (Gemini free tier), OpenRouter free models, Ollama (local, fully free)
- Frameworks: LangGraph, LangChain, (later) OpenAI Agents SDK / CrewAI for comparison
- Data: ChromaDB, Qdrant (local Docker), SQLite/PostgreSQL
- Serving: FastAPI, Docker, Render / Vercel / Hugging Face Spaces free tiers
- Observability/evals: Langfuse (self-host or free cloud), LangSmith free tier, pytest
- Free learning: DeepLearning.AI short courses, LangChain Academy (Intro to LangGraph), Hugging Face Agents Course, Anthropic "Building effective agents", Model Context Protocol docs, official library docs

---

## PHASE 1: BASICS

### M0. Setup & Python for AI work (skip if comfortable; take the checkpoint)
- Concepts: venv, .env and secrets, typing, dataclasses, **Pydantic**, async/await, HTTP/JSON, Git workflow
- Project: CLI script that calls a public API with async + Pydantic validation
- Checkpoint: explain sync vs async; validate a malformed JSON with Pydantic

### M1. How LLMs work for engineers
- Concepts: tokens, context window, temperature/top_p, system vs user vs assistant roles, stateless APIs, cost/latency, hallucination
- Code: raw API call (Groq/Ollama) with no SDK wrapper, then with the SDK; streaming
- Project: **CLI chatbot with conversation memory** (trim/summarize history)
- Checkpoint: why must you resend history? What happens when the context overflows?

### M2. Prompting & structured output
- Concepts: prompt patterns (role, few-shot, chain-of-thought), JSON mode, schema-constrained output, retries/validation
- Project: **Resume/email parser** returning validated Pydantic objects, with a retry-on-invalid loop
- Checkpoint: make output reliable on 20 messy inputs; measure the failure rate

---

## PHASE 2: AGENT CORE (from scratch)

### M3. Tool use / function calling
- Concepts: tool schemas, model decides vs code executes, argument validation, error returns, parallel calls
- Project: assistant with 4 tools (calculator, weather API, web search, file reader)
- Checkpoint: what if the model passes bad args? Who executes the tool?

### M4. Build an agent loop from scratch (ReAct)
- Concepts: observe -> think -> act loop, stop conditions, max steps, scratchpad, loop detection
- Project: **Mini-agent framework (~150 lines, no LangChain)**. This is the most important module.
- Checkpoint: add max-step guard, tool-error recovery, and logging of each step

### M5. RAG fundamentals
- Concepts: embeddings, similarity, chunking strategies, vector DB, top-k, reranking, citations
- Project: **Chat with your own docs** (ChromaDB + local embeddings, e.g. sentence-transformers)
- Checkpoint: build a small eval set of 15 Q&A pairs; compare chunk sizes by hit rate

---

## PHASE 3: INTERMEDIATE (frameworks & orchestration)

### M6. LangGraph foundations
- Concepts: State, nodes, edges, conditional routing, reducers, graph compile/invoke, streaming
- Free course: LangChain Academy "Introduction to LangGraph"
- Project: rebuild M4's agent in LangGraph and compare with your scratch version

### M7. Agentic RAG & routing
- Concepts: query rewriting, retrieval grading, self-correction loops, router agents, web fallback
- Project: **Corrective RAG agent** (retrieve -> grade -> rewrite/search -> answer with citations)

### M8. Memory, persistence & human-in-the-loop
- Concepts: short-term (checkpointers) vs long-term memory (stores), threads, interrupts, approval steps, time-travel debugging
- Project: **Research assistant** that pauses for human approval before sending/saving anything

### M9. Planning & reflection patterns
- Concepts: plan-and-execute, reflection/critic, evaluator-optimizer, prompt chaining, parallelization (Anthropic patterns)
- Project: **Report writer**: planner -> researchers -> writer -> critic loop

---

## PHASE 4: ADVANCED

### M10. Multi-agent systems
- Concepts: supervisor, handoffs/swarm, shared vs private state, when NOT to use multi-agent
- Project: **Multi-agent analyst team** (e.g. data analyst + SQL agent + chart agent + reviewer)

### M11. MCP & tool ecosystems
- Concepts: Model Context Protocol, servers/clients, resources vs tools, security of tools
- Project: **Build your own MCP server** (e.g. notes/GitHub/SQLite) and connect an agent to it

### M12. Evaluation, observability & safety
- Concepts: tracing (Langfuse), LLM-as-judge, regression evals with pytest, prompt injection, guardrails, permission scoping, cost/token budgets
- Project: add tracing + an eval suite + guardrails to your best agent

### M13. Production & deployment
- Concepts: FastAPI + streaming (SSE/WebSocket), background jobs, Redis/Postgres, Docker, CI, rate limits, retries, secrets
- Project: **Deploy** an agent API on a free tier with a simple React/HTML front-end

---

## CAPSTONE (M14)
Design and ship an original agentic application: problem statement, architecture diagram, multi-step agent with tools + RAG + memory, human approval, evals, tracing, deployed URL, README with a design-decision log.

## Module completion criteria
1. Project runs and is on GitHub with a README
2. I wrote the core code myself
3. Checkpoint passed
4. I can explain every design choice without notes
