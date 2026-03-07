from games.tictactoe import TicTacToe


def test_initial_state():
    game = TicTacToe()
    state = game.reset()
    assert state.current_player == "X"
    assert state.winner is None
    assert not state.done
    assert len(state.valid_moves) == 9


def test_make_move():
    game = TicTacToe()
    game.reset()
    state = game.make_move(4)
    assert state.board[4] == "X"
    assert state.current_player == "O"


def test_win_detection():
    game = TicTacToe()
    game.reset()
    game.make_move(0)  # X
    game.make_move(3)  # O
    game.make_move(1)  # X
    game.make_move(4)  # O
    state = game.make_move(2)  # X wins top row
    assert state.winner == "X"
    assert state.done


def test_draw():
    game = TicTacToe()
    game.reset()
    # X O X / X X O / O X O
    for pos in [0, 1, 2, 4, 3, 6, 5, 8, 7]:
        game.make_move(pos)
    state = game.get_state()
    assert state.winner is None
    assert state.done


def test_invalid_move():
    game = TicTacToe()
    game.reset()
    game.make_move(0)
    try:
        game.make_move(0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass