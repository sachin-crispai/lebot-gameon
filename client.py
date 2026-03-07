import httpx

from models import TicTacToeAction, TicTacToeObservation


class TicTacToeClient:
    """Client for interacting with the TicTacToe OpenEnv environment."""

    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url.rstrip("/")
        self._client: httpx.AsyncClient | None = None

    async def __aenter__(self):
        self._client = httpx.AsyncClient(base_url=self.base_url)
        return self

    async def __aexit__(self, *args):
        if self._client:
            await self._client.aclose()

    async def reset(self) -> TicTacToeObservation:
        resp = await self._client.post("/reset")
        resp.raise_for_status()
        return TicTacToeObservation(**resp.json())

    async def step(self, action: TicTacToeAction | dict) -> TicTacToeObservation:
        if isinstance(action, TicTacToeAction):
            payload = {"position": action.position}
        else:
            payload = action
        resp = await self._client.post("/step", json=payload)
        resp.raise_for_status()
        return TicTacToeObservation(**resp.json())

    async def state(self) -> dict:
        resp = await self._client.get("/state")
        resp.raise_for_status()
        return resp.json()