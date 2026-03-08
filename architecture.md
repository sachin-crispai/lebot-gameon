# Architecture Notes: Agent Patterns Reading Path (Mastra Trilogy)

Date: 2026-03-08
Scope: Curate actionable resources for agent design patterns and map them to implementation guidance for this repository.

## Synopsis

This repo's agent-pattern guidance is now centered on Sam Bhagwat's Mastra trilogy:
1. Principles of Building AI Agents (foundation)
2. Patterns for Building AI Agents (production patterns)
3. Forthcoming Volume 3 (not publicly titled/released as of 2026-03-08)

This creates a practical progression from fundamentals to deployment rigor and keeps us aligned with a single coherent source.

## Findings (Verified)

### 1) Principles of Building AI Agents
- URL: https://mastra.ai/book
- Positioning: introductory-to-intermediate foundation for agent systems.
- Practical coverage: models, prompts, tools, memory, workflows, RAG, and multi-agent fundamentals.
- Suggested use in this repo: define core boundaries and interfaces first (state/action/constraints).

### 2) Patterns for Building AI Agents (Volume 2)
- URL: https://mastra.ai/books/patterns-of-building-ai-agents
- Positioning: production-focused continuation.
- Practical coverage: architecture patterns, context engineering, evaluation patterns, and security controls.
- Suggested use in this repo: prioritize eval + safety gates before adding complexity.

### 3) Trilogy status / Volume 3
- URL: https://mastra.ai/blog/patterns-book
- Verified statement: Patterns is described as "Volume 2 of an eventual trilogy."
- Current status: Volume 3 is forthcoming (no publicly announced title/release found on official pages as of 2026-03-08).
- Follow-up path: monitor Mastra books/blog pages for release updates.

### 4) Author reference
- URL: https://mastra.ai/authors/sam-bhagwat
- Purpose: canonical author index for updates across books and writing.

## Recommended Application to This Codebase

### Architecture direction
- Keep pure game logic in `games/` (no framework coupling).
- Keep orchestration/stateful environment behavior in `server/`.
- Treat each `players/*` implementation as an explicit agent policy with constrained action space.

### Pattern adoption order
1. Establish deterministic single-agent baseline and strict tool/state interfaces.
2. Add context/memory only where repeated tasks prove the need.
3. Add multi-agent decomposition only when specialization materially improves quality or latency.
4. Add evaluation harnesses and security boundaries before broadening autonomy.

### Concrete checks to enforce
- Invalid action handling is deterministic and test-covered.
- Episode/game loop termination is explicit and test-covered.
- Behavior is reproducible under fixed seeds where randomness exists.
- Any external-tool or physical-actuation path has validation/guardrails.

## Source List

- https://mastra.ai/book
- https://mastra.ai/books/patterns-of-building-ai-agents
- https://mastra.ai/blog/patterns-book
- https://mastra.ai/authors/sam-bhagwat
