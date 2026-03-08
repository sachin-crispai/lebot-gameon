# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Multi-Agent Development

This repo supports parallel development by multiple LLM agents. Read `AGENTS.md` for the full onboarding guide, repo map, conventions, and conflict-avoidance rules. Always check `gh issue list` and `gh pr list` before starting work.

## Project Overview

**lebot-gameon** is a Tic-Tac-Toe game environment built on [OpenEnv](https://github.com/meta-pytorch/OpenEnv) for the Cerebral Valley Hackathon. A LEBOT robot arm plays as both an AI opponent and a physical robot player.

## Tech Stack

- **Framework:** OpenEnv (`openenv-core`) — Gymnasium-style `step()/reset()/state()` API
- **Server:** FastAPI + Uvicorn
- **Frontend:** Vanilla HTML/CSS/JS with WebSocket for real-time updates
- **Robot:** LeRobot integration for LEBOT physical arm control
- **Python:** 3.13+, managed with `uv`

## Commands

```bash
# Install dependencies
uv sync
uv sync --extra dev      # with test deps
uv sync --extra robot    # with LeRobot

# Run server
uv run uvicorn server.app:app --reload

# Run all tests
PYTHONPATH=. uv run pytest tests/ -v

# Run a single test
PYTHONPATH=. uv run pytest tests/test_tictactoe.py::test_win_detection -v
```

## OpenEnv Redbook Workflow

- Place source PDFs in `books/openenv-redbook/sources/` with numeric prefixes for order.
- Keep partner resources in `books/openenv-redbook/partners/` with one folder per partner.
- Build `books/openenv-redbook/openenv-redbook-a4.pdf` using:

```bash
uv pip install --python .venv/bin/python pypdf
./.venv/bin/python books/openenv-redbook/build_openenv_redbook.py
```

- Redbook page size standard: **A4 landscape** (`841.89 x 595.28 pt`) for every page.

## Local UX Convention

- Default doc/PDF reader is **Skim**.
- If the user says `skimread <file>` (or asks to open a file in skim), use:
  - `open -a Skim <file>`

## Architecture

- **`games/`** — Abstract `Game` base class + concrete implementations. `TicTacToe` is the first game; add new games by subclassing `Game`. No framework imports allowed here — pure Python only.
- **`players/`** — Abstract `Player` base class with `async def get_move(state) -> int`. Implementations: `HumanPlayer` (asyncio.Future awaiting API/WebSocket input), `AIPlayer` (minimax with alpha-beta pruning), `RandomPlayer`, `LeBotPlayer` (inherits `AIPlayer`, adds physical arm execution).
- **`server/tictactoe_env.py`** — `TicTacToeEnvironment` is a plain Python class (not a framework subclass) implementing the OpenEnv pattern: `reset() -> dict`, `step(action: dict) -> dict`, `state() -> dict`. Rewards: 1.0 win, 0.5 draw, -1.0 invalid move.
- **`server/app.py`** — FastAPI entry point. REST endpoints (`POST /reset`, `POST /step`, `GET /state`) + WebSocket (`/ws`). WebSocket messages: `{"type": "reset"}` or `{"type": "move", "position": N}`.
- **`models.py`** — `TicTacToeAction` and `TicTacToeObservation` dataclasses.
- **`client.py`** — `TicTacToeClient`: async context manager using `httpx` for programmatic environment access.
- **`web/static/`** — Browser game UI connecting via WebSocket.

## Key Patterns

- Game logic is decoupled from the server — `games/tictactoe.py` has no framework dependencies.
- Players are async and injected into the environment — swap human, AI, or LEBOT without changing game logic.
- The board is a flat list of 9 cells (indices 0-8): `None` = empty, `"X"` = player 1, `"O"` = player 2.
- `LeBotPlayer` inherits from `AIPlayer` — it uses minimax for decisions and adds physical robot execution on top. The LeRobot SDK integration is currently stubbed.

## Code Conventions

- Use Python 3.13+ features freely (e.g., `X | Y` union types)
- Type hints on all function signatures
- Imports ordered: stdlib → third-party → local
- Conventional commit messages: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`
- Branch names: `feat/<description>` or `fix/<description>`, always from `main`
- Keep PRs focused on one issue; don't modify files outside your issue scope
