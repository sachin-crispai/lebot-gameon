from abc import ABC, abstractmethod

from games.base import GameState


class Player(ABC):
    """Abstract base class for game players."""

    def __init__(self, marker: str):
        self.marker = marker  # "X" or "O"

    @abstractmethod
    async def get_move(self, state: GameState) -> int:
        """Given the current game state, return the chosen move."""