import asyncio

from games.base import GameState
from players.base import Player


class HumanPlayer(Player):
    """Human player that receives moves from external input (API/WebSocket)."""

    def __init__(self, marker: str):
        super().__init__(marker)
        self._pending_move: asyncio.Future | None = None

    async def get_move(self, state: GameState) -> int:
        self._pending_move = asyncio.get_event_loop().create_future()
        move = await self._pending_move
        self._pending_move = None
        return move

    def submit_move(self, position: int) -> None:
        """Called by the API/WebSocket handler when the human submits a move."""
        if self._pending_move is not None and not self._pending_move.done():
            self._pending_move.set_result(position)