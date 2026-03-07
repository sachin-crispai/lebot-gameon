from dataclasses import dataclass, field


@dataclass
class TicTacToeAction:
    """Action: place a piece at a board position (0-8)."""
    position: int


@dataclass
class TicTacToeObservation:
    """Observation returned after each step."""
    board: list[str | None]
    current_player: str
    winner: str | None
    done: bool
    valid_moves: list[int]
    reward: float = 0.0
    message: str = ""