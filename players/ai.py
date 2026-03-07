import random
from math import inf

from games.base import GameState
from games.tictactoe import TicTacToe
from players.base import Player


class RandomPlayer(Player):
    """Player that picks a random valid move."""

    async def get_move(self, state: GameState) -> int:
        return random.choice(state.valid_moves)


class AIPlayer(Player):
    """Unbeatable AI using minimax with alpha-beta pruning."""

    async def get_move(self, state: GameState) -> int:
        best_score = -inf
        best_move = state.valid_moves[0]

        for move in state.valid_moves:
            board = list(state.board)
            board[move] = self.marker
            score = self._minimax(board, False, -inf, inf)
            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def _minimax(self, board: list, is_maximizing: bool, alpha: float, beta: float) -> float:
        winner = self._check_winner(board)
        if winner == self.marker:
            return 1
        if winner is not None:
            return -1
        if all(c is not None for c in board):
            return 0

        opponent = "O" if self.marker == "X" else "X"
        current = self.marker if is_maximizing else opponent

        if is_maximizing:
            best = -inf
            for i in range(9):
                if board[i] is None:
                    board[i] = current
                    best = max(best, self._minimax(board, False, alpha, beta))
                    board[i] = None
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
            return best
        else:
            best = inf
            for i in range(9):
                if board[i] is None:
                    board[i] = current
                    best = min(best, self._minimax(board, True, alpha, beta))
                    board[i] = None
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
            return best

    @staticmethod
    def _check_winner(board: list) -> str | None:
        from games.tictactoe import WIN_LINES
        for a, b, c in WIN_LINES:
            if board[a] is not None and board[a] == board[b] == board[c]:
                return board[a]
        return None