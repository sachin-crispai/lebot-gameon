"""OpenEnv Environment for Tic-Tac-Toe."""

from games.tictactoe import TicTacToe
from models import TicTacToeObservation


class TicTacToeEnvironment:
    """OpenEnv-compatible environment wrapping the TicTacToe game."""

    def __init__(self):
        self.game = TicTacToe()
        self.episode_id: str | None = None
        self.step_count = 0

    def reset(self) -> dict:
        self.game.reset()
        self.step_count = 0
        # TODO: generate unique episode_id
        self.episode_id = "ep_001"
        return self._obs(message="Game started. X goes first.").to_dict()

    def step(self, action: dict) -> dict:
        position = action["position"]
        try:
            state = self.game.make_move(position)
        except ValueError as e:
            return self._obs(reward=-1.0, message=str(e)).to_dict()

        self.step_count += 1

        reward = 0.0
        msg = f"Placed at {position}."
        if state.winner:
            reward = 1.0
            msg = f"{state.winner} wins!"
        elif state.done:
            reward = 0.5
            msg = "Draw!"

        return self._obs(reward=reward, message=msg).to_dict()

    def state(self) -> dict:
        return {
            "episode_id": self.episode_id,
            "step_count": self.step_count,
        }

    def _obs(self, reward: float = 0.0, message: str = "") -> TicTacToeObservation:
        gs = self.game.get_state()
        return TicTacToeObservation(
            board=gs.board,
            current_player=gs.current_player,
            winner=gs.winner,
            done=gs.done,
            valid_moves=gs.valid_moves,
            reward=reward,
            message=message,
        )


# Helper so obs can be serialized
def _patch_obs():
    from dataclasses import asdict
    TicTacToeObservation.to_dict = lambda self: asdict(self)

_patch_obs()
