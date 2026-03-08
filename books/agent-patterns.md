# Agent Patterns: Sam Bhagwat (Mastra) Trilogy

Focused reading path for building AI agents, centered on Sam Bhagwat's Mastra book series.

## Trilogy (Mastra)

1. **Principles of Building AI Agents** (2025, 2nd ed.)
   - Link: https://mastra.ai/book
   - Focus: foundations and core building blocks (models, prompts, tools, memory, workflows, RAG, multi-agent basics).
2. **Patterns for Building AI Agents** (2025, Volume 2)
   - Link: https://mastra.ai/books/patterns-of-building-ai-agents
   - Focus: production patterns (agent architecture, context engineering, eval workflows, security).
3. **Volume 3 (forthcoming, title not announced publicly)**
   - Evidence: the Patterns announcement describes it as "Volume 2 of an eventual trilogy".
   - Link: https://mastra.ai/blog/patterns-book

## How to Use the Trilogy to Build Agents

1. **Start with Principles (what to build)**
   - Define task boundaries, tool interfaces, memory strategy, and workflow structure.
   - Build a minimal single-agent path before adding orchestration.
2. **Move to Patterns (how to ship it reliably)**
   - Apply context-engineering patterns to reduce failure modes.
   - Add eval loops and business metrics before scaling complexity.
   - Introduce security controls: guardrails, access boundaries, sandboxed execution where needed.
3. **Prepare for Volume 3**
   - Track updates from Mastra blog and books pages.
   - Treat your implementation docs as a living playbook so new trilogy guidance can be folded in quickly.

## Practical Pattern Checklist (for this repo)

- Keep game logic deterministic and framework-free in `games/`.
- Treat players as constrained agents with explicit action space.
- Add eval-style tests for invalid actions, loop termination, and predictable outcomes.
- Add safety checks around tool or actuator execution paths (especially robot control).

## References

- Principles book: https://mastra.ai/book
- Patterns book: https://mastra.ai/books/patterns-of-building-ai-agents
- Patterns announcement (trilogy reference): https://mastra.ai/blog/patterns-book
- Sam Bhagwat author page: https://mastra.ai/authors/sam-bhagwat
