from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class GameState:
    board: Any
    current_player: str
    winner: str | None
    done: bool
    valid_moves: list


class Game(ABC):
    """Abstract base class for two-player board games."""

    @abstractmethod
    def reset(self) -> GameState:
        """Reset the game to initial state and return it."""

    @abstractmethod
    def make_move(self, move: Any) -> GameState:
        """Apply a move and return the new state. Raises ValueError for invalid moves."""

    @abstractmethod
    def get_valid_moves(self) -> list:
        """Return list of valid moves for the current player."""

    @abstractmethod
    def get_state(self) -> GameState:
        """Return the current game state."""

    @abstractmethod
    def check_winner(self) -> str | None:
        """Return the winning player marker, or None if no winner yet."""

    @abstractmethod
    def is_done(self) -> bool:
        """Return True if the game is over (win or draw)."""