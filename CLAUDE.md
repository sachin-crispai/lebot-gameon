# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

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

## Architecture

- **`games/`** — Abstract `Game` base class + concrete implementations. `TicTacToe` is the first game; add new games by subclassing `Game`.
- **`players/`** — Abstract `Player` base class. Implementations: `HumanPlayer` (API input), `AIPlayer` (minimax), `LeBotPlayer` (robot arm). All share `get_move(game_state) -> move` interface.
- **`server/`** — OpenEnv `Environment` subclass wrapping the game engine. `app.py` is the FastAPI entry point. The environment exposes `reset()`, `step(action)`, `state()`.
- **`models.py`** — OpenEnv dataclasses: `TicTacToeAction`, `TicTacToeObservation`.
- **`client.py`** — OpenEnv `EnvClient` subclass for programmatic interaction.
- **`web/static/`** — Browser game UI connecting via WebSocket.

## Key Patterns

- Game logic is decoupled from the OpenEnv environment — `games/tictactoe.py` is a pure game engine with no framework dependencies.
- Players are injected into the environment — swap between human, AI, or LEBOT without changing game logic.
- The board is a flat list of 9 cells (indices 0-8), where `None` = empty, `"X"` = player 1, `"O"` = player 2.