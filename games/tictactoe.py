from games.base import Game, GameState

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6),              # diagonals
]


class TicTacToe(Game):
    """3x3 Tic-Tac-Toe game engine.

    Board is a flat list of 9 cells (indices 0-8).
    Values: None (empty), "X" (player 1), "O" (player 2).

    Layout:
        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
    """

    def __init__(self):
        self.board: list[str | None] = [None] * 9
        self.current_player: str = "X"
        self._winner: str | None = None

    def reset(self) -> GameState:
        self.board = [None] * 9
        self.current_player = "X"
        self._winner = None
        return self.get_state()

    def make_move(self, position: int) -> GameState:
        if self._winner is not None or all(c is not None for c in self.board):
            raise ValueError("Game is already over")
        if not (0 <= position <= 8):
            raise ValueError(f"Position must be 0-8, got {position}")
        if self.board[position] is not None:
            raise ValueError(f"Position {position} is already taken")

        self.board[position] = self.current_player
        self._winner = self.check_winner()

        if self._winner is None:
            self.current_player = "O" if self.current_player == "X" else "X"

        return self.get_state()

    def get_valid_moves(self) -> list[int]:
        if self.is_done():
            return []
        return [i for i, cell in enumerate(self.board) if cell is None]

    def get_state(self) -> GameState:
        return GameState(
            board=list(self.board),
            current_player=self.current_player,
            winner=self._winner,
            done=self.is_done(),
            valid_moves=self.get_valid_moves(),
        )

    def check_winner(self) -> str | None:
        for a, b, c in WIN_LINES:
            if self.board[a] is not None and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def is_done(self) -> bool:
        return self._winner is not None or all(c is not None for c in self.board)