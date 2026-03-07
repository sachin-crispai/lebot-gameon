# lebot-gameon

LEBOT robot plays Tic-Tac-Toe using [OpenEnv](https://github.com/meta-pytorch/OpenEnv) — built at the [Cerebral Valley OpenEnv Hackathon](https://cerebralvalley.ai/e/openenv-hackathon-sf) (March 2026).

## What is this?

A game environment where a LEBOT robot arm plays Tic-Tac-Toe against humans. Built as an OpenEnv environment with Gymnasium-style `step()/reset()/state()` APIs, it supports:

- **Human vs AI** — play against a minimax-powered unbeatable opponent
- **Human vs LEBOT** — play against a physical robot arm that places pieces on a real board
- **AI vs LEBOT** — watch the robot play against itself
- **Web UI** — real-time game board visualization via WebSocket

## Setup

```bash
# Clone
git clone https://github.com/sachin-crispai/lebot-gameon.git
cd lebot-gameon

# Install dependencies
uv sync

# Install with robot support
uv sync --extra robot

# Install dev dependencies
uv sync --extra dev
```

## Usage

### Start the server
```bash
uv run uvicorn server.app:app --reload
```

Open http://localhost:8000 to play in the browser.

### Use as OpenEnv environment
```python
from client import TicTacToeClient

async with TicTacToeClient(base_url="http://localhost:8000") as client:
    obs = await client.reset()
    obs = await client.step({"position": 4})  # center square
```

### Run tests
```bash
PYTHONPATH=. uv run pytest tests/ -v
```

## Architecture

```
games/          — Game engine abstractions (extensible to other games)
players/        — Player implementations (human, AI, LEBOT)
server/         — OpenEnv environment + FastAPI server
web/static/     — Browser-based game UI
```

## License

MIT