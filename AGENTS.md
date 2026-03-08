# AGENTS.md — Multi-Agent LLM Collaboration Guide

This repository is designed for parallel development by multiple LLM agents (Claude, Codex, Gemini, GPT, etc.) and human developers. Read this file first to get up to speed.

## Quick Start for Any Agent

1. **Read these files in order:** `AGENTS.md` (this file) → `CLAUDE.md` → `README.md`
2. **Check open issues:** `gh issue list` — pick an unassigned issue
3. **Check open PRs:** `gh pr list` — avoid conflicting with in-progress work
4. **Check recent history:** `git log --oneline -20` — understand what just happened
5. **Run tests before changing anything:** `PYTHONPATH=. uv run pytest tests/ -v`

## Repository Map

```
lebot-gameon/
├── games/              # Game engine layer (pure logic, no framework deps)
│   ├── base.py         # Abstract Game class — extend for new games
│   └── tictactoe.py    # TicTacToe implementation (board is flat list[9])
├── players/            # Player abstractions (all async)
│   ├── base.py         # Abstract Player with get_move(state) -> int
│   ├── human.py        # Human player (receives moves via API/WebSocket)
│   ├── ai.py           # AIPlayer (minimax) + RandomPlayer
│   └── lebot.py        # LEBOT robot arm — AI brain + physical move stub
├── server/             # OpenEnv environment + FastAPI
│   ├── app.py          # FastAPI app: REST (/reset, /step, /state) + WebSocket (/ws)
│   └── tictactoe_env.py # OpenEnv Environment wrapping game engine
├── models.py           # TicTacToeAction, TicTacToeObservation dataclasses
├── client.py           # HTTP client for environment API
├── web/static/         # Browser UI (vanilla HTML/CSS/JS + WebSocket)
├── tests/              # pytest tests
├── openenv.yaml        # OpenEnv environment manifest
├── pyproject.toml      # Python 3.13+, uv package manager
├── CLAUDE.md           # Claude Code specific guidance
├── AGENTS.md           # This file — multi-agent onboarding
└── CONTRIBUTING.md     # Contribution rules for agents and humans
```

## Key Architecture Decisions

- **Game logic is pure Python** — no framework dependencies in `games/`. This is intentional. Don't add FastAPI, OpenEnv, or any imports there.
- **Board representation** — flat `list[9]`, values: `None` (empty), `"X"`, `"O"`. Positions 0-8, left-to-right top-to-bottom.
- **Players are async** — `get_move()` is `async` to support both instant AI and awaitable human/robot input.
- **OpenEnv pattern** — `reset() -> obs`, `step(action) -> obs`, `state() -> metadata`. Don't deviate.
- **LEBOT inherits from AIPlayer** — uses minimax for decisions, adds physical robot execution on top.

## Conventions

### Branching
- `main` — stable, deployable
- `feat/<description>` — feature branches
- `fix/<description>` — bug fixes
- Always branch from `main`, PR back to `main`

### Commits
- Use conventional-style messages: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`
- Include `Co-Authored-By: <Agent Name> <email>` trailer
- Reference issue numbers: `Fixes #N` or `Relates to #N`

### PRs
- Fill out the PR template completely
- Reference related issues
- Include test results
- Tag which agent/LLM created the PR in the description

### Code Style
- Python 3.13+ features are fine (type unions with `|`, etc.)
- No docstrings needed on obvious methods
- Use type hints on function signatures
- Keep imports at top of file, stdlib → third-party → local

## How to Avoid Conflicts Between Agents

1. **Claim an issue first** — comment on it or assign yourself before starting work
2. **Check `gh pr list`** — don't work on something that already has an open PR
3. **Keep PRs small and focused** — one issue per PR
4. **Don't modify files outside your issue scope** — resist the urge to "clean up" unrelated code
5. **Run tests before pushing** — `PYTHONPATH=. uv run pytest tests/ -v`

## Commands Reference

```bash
# Setup
uv sync                                    # Install deps
uv sync --extra dev                        # With test deps
uv sync --extra robot                      # With LeRobot

# Development
uv run uvicorn server.app:app --reload     # Start server (http://localhost:8000)
PYTHONPATH=. uv run pytest tests/ -v       # Run all tests
PYTHONPATH=. uv run pytest tests/test_tictactoe.py::test_win_detection -v  # Single test

# Git workflow
gh issue list                              # See available work
gh pr list                                 # Check in-progress work
gh pr create --title "..." --body "..."    # Open PR
```

## OpenEnv Redbook Workflow

- Redbook workspace: `books/openenv-redbook/`
- Source PDFs directory: `books/openenv-redbook/sources/`
- Partner resources directory: `books/openenv-redbook/partners/` (one folder per partner)
- Ordering rule: prefix files with `01-`, `02-`, `03-`, etc.
- Standard output: `books/openenv-redbook/openenv-redbook-a4.pdf`
- Page standard: **A4 landscape** (`841.89 x 595.28 pt`) for all pages.

Build command:

```bash
uv pip install --python .venv/bin/python pypdf
./.venv/bin/python books/openenv-redbook/build_openenv_redbook.py
```

## Local UX Convention

- The user uses **Skim** as the default document reader on macOS.
- If the user says `skimread <file>` (or asks to "open in skim"), agents should run:
  - `open -a Skim <file>`
- Use this for PDFs and other Skim-supported docs unless the user explicitly asks for a different app.
- If the user says `atlasread <url>`, agents should open the URL in Atlas:
  - `open -a "ChatGPT Atlas.app" "<url>"`
- If the user says `atlas left <website>`, agents should:
  - open Atlas with the website using full path:
    - `open -a "/Applications/ChatGPT Atlas.app" "<website>"`
  - position Atlas window to left half via AppleScript.
- If the user says `atlas right <website>`, agents should:
  - open Atlas with the website using full path:
    - `open -a "/Applications/ChatGPT Atlas.app" "<website>"`
  - position Atlas window to right half via AppleScript.
- After pushing changes, agents should always run an `atlas left` open on at least one file URL from the merged/pushed PR to visually verify remote availability.

## Current Status

This is a hackathon project (Cerebral Valley OpenEnv Hackathon, March 2026). Speed matters. Ship working code, iterate fast, don't over-engineer.
