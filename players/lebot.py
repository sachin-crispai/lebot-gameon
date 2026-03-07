from games.base import GameState
from players.ai import AIPlayer


# Grid positions mapped to physical coordinates (x, y, z) in mm.
# These will be calibrated to the actual LEBOT arm workspace.
BOARD_COORDINATES = {
    0: (100, 100, 0),
    1: (150, 100, 0),
    2: (200, 100, 0),
    3: (100, 150, 0),
    4: (150, 150, 0),
    5: (200, 150, 0),
    6: (100, 200, 0),
    7: (150, 200, 0),
    8: (200, 200, 0),
}

# Pickup locations for X and O pieces
PIECE_PICKUP = {
    "X": (50, 150, 0),
    "O": (250, 150, 0),
}


class LeBotPlayer(AIPlayer):
    """LEBOT robot arm player.

    Uses AI (minimax) to decide the move, then commands the physical
    robot arm to pick up a piece and place it on the board.

    Requires the `lerobot` package: pip install lerobot
    """

    def __init__(self, marker: str, robot_config: dict | None = None):
        super().__init__(marker)
        self.robot_config = robot_config or {}
        self._robot = None

    async def get_move(self, state: GameState) -> int:
        move = await super().get_move(state)
        await self._execute_physical_move(move)
        return move

    async def _execute_physical_move(self, position: int) -> None:
        """Command the LEBOT arm to physically place a piece.

        TODO: Integrate with LeRobot SDK once hardware is connected.
        Currently logs the intended action.
        """
        pickup = PIECE_PICKUP[self.marker]
        target = BOARD_COORDINATES[position]
        print(f"[LEBOT] Picking up '{self.marker}' piece at {pickup}")
        print(f"[LEBOT] Placing piece at board position {position} -> {target}")

        if self._robot is not None:
            # Future: self._robot.move_to(pickup)
            # Future: self._robot.grip()
            # Future: self._robot.move_to(target)
            # Future: self._robot.release()
            pass

    def connect(self, **kwargs) -> None:
        """Connect to the physical LEBOT robot arm.

        TODO: Initialize LeRobot connection with calibration data.
        """
        try:
            # from lerobot import Robot
            # self._robot = Robot(**self.robot_config, **kwargs)
            print("[LEBOT] Robot connection stub — install lerobot for hardware support")
        except ImportError:
            print("[LEBOT] lerobot not installed — running in simulation mode")