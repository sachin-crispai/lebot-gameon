# Agent Patterns: Books and PDFs

A short, high-signal reading list for designing and shipping LLM agents.

## Core Books

- **Designing Autonomous AI Agents** (O'Reilly, Russ d’Sa et al., 2025)
  - Focus: practical agent architectures, orchestration loops, tool use.
- **AI Engineering** (Chip Huyen, 2025)
  - Focus: production LLM systems, evaluation, reliability, and deployment.
- **Multi-Agent Systems (2nd ed.)** (Gerhard Weiss, ed.)
  - Focus: classic foundations for coordination, communication, and distributed decision making.
- **Artificial Intelligence: A Modern Approach (4th ed.)** (Russell & Norvig)
  - Focus: planning, search, reasoning under uncertainty; useful for agent fundamentals.

## Key Papers (Direct PDFs)

- **ReAct: Synergizing Reasoning and Acting in Language Models**
  - PDF: https://arxiv.org/pdf/2210.03629.pdf
  - Why: foundational think-act-observe loop pattern.
- **Toolformer: Language Models Can Teach Themselves to Use Tools**
  - PDF: https://arxiv.org/pdf/2302.04761.pdf
  - Why: tool invocation as a learned behavior.
- **Generative Agents: Interactive Simulacra of Human Behavior**
  - PDF: https://arxiv.org/pdf/2304.03442.pdf
  - Why: memory/reflection/planning loops for long-horizon agents.
- **Reflexion: Language Agents with Verbal Reinforcement Learning**
  - PDF: https://arxiv.org/pdf/2303.11366.pdf
  - Why: self-critique and iterative improvement pattern.
- **Voyager: An Open-Ended Embodied Agent with LLMs**
  - PDF: https://arxiv.org/pdf/2305.16291.pdf
  - Why: curriculum + skill library + self-verification.
- **CAMEL: Communicative Agents for "Mind" Exploration of LLM Society**
  - PDF: https://arxiv.org/pdf/2303.17760.pdf
  - Why: role-based multi-agent collaboration pattern.
- **AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation**
  - PDF: https://arxiv.org/pdf/2308.08155.pdf
  - Why: practical multi-agent messaging and delegation model.

## Fast Application Patterns

- Start with a **single-agent ReAct loop** plus strict tool schemas.
- Add **retrieval + memory** only when repeated tasks need persistence.
- Add **multi-agent decomposition** only when specialization clearly improves quality/latency.
- Build an **eval harness first** (task success, tool error rate, cost, latency).
- Prefer **small deterministic tools** and explicit guardrails over free-form autonomy.

## Notes for This Repo

- Keep game logic pure in `games/` and isolate orchestration concerns in `server/` and `players/`.
- Treat each player as an agent with explicit state, action space, and constraints.
- Add tests for invalid actions, loop termination, and deterministic behavior under fixed seeds.
