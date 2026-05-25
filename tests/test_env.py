from tictactoe_ai.env import TicTacToeEnv
from tictactoe_ai.game import EMPTY, INITIAL_BOARD, RESULT_ONGOING, RESULT_X_WIN, O, X


def test_env_starts_with_initial_state() -> None:
    env = TicTacToeEnv()

    assert env.state.board == INITIAL_BOARD
    assert env.state.current_player == X
    assert env.result() == RESULT_ONGOING
    assert not env.done()


def test_env_reset_restores_initial_state() -> None:
    env = TicTacToeEnv()
    env.step(4)

    state = env.reset()

    assert state.board == INITIAL_BOARD
    assert state.current_player == X


def test_env_legal_moves_reflect_current_state() -> None:
    env = TicTacToeEnv()
    env.step(4)

    assert env.legal_moves() == (0, 1, 2, 3, 5, 6, 7, 8)


def test_env_step_updates_state_and_returns_result() -> None:
    env = TicTacToeEnv()

    state, result = env.step(4)

    assert state.board == (
        EMPTY,
        EMPTY,
        EMPTY,
        EMPTY,
        X,
        EMPTY,
        EMPTY,
        EMPTY,
        EMPTY,
    )
    assert state.current_player == O
    assert result == RESULT_ONGOING
    assert env.state == state


def test_env_step_returns_winning_result() -> None:
    env = TicTacToeEnv()
    env.step(0)
    env.step(3)
    env.step(1)
    env.step(4)

    state, result = env.step(2)

    assert result == RESULT_X_WIN
    assert state.current_player == X
    assert env.done()


def test_env_render_returns_current_board() -> None:
    env = TicTacToeEnv()
    env.step(4)

    assert env.render() == ". . .\n. X .\n. . ."
