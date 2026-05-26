import pytest

from tictactoe_ai.game import EMPTY, GameState, X
from tictactoe_ai.q_learning import QLearningAgent


def test_q_value_returns_zero_for_unknown_state_action() -> None:
    agent = QLearningAgent()
    state = GameState()

    assert agent.q_value(state, 4) == 0.0


def test_choose_action_returns_lowest_legal_move_when_values_are_equal() -> None:
    agent = QLearningAgent()
    state = GameState()

    assert agent.choose_action(state, (2, 4, 6)) == 2


def test_choose_action_returns_best_known_legal_move() -> None:
    board = (
        X,
        EMPTY,
        EMPTY,
        EMPTY,
        EMPTY,
        EMPTY,
        EMPTY,
        EMPTY,
        EMPTY,
    )
    state = GameState(board=board)
    agent = QLearningAgent(
        q_values={
            (board, 1): 0.25,
            (board, 2): 0.75,
            (board, 3): 0.50,
        }
    )

    assert agent.choose_action(state, (1, 2, 3)) == 2


def test_choose_action_ignores_illegal_known_move() -> None:
    board = (
        X,
        EMPTY,
        EMPTY,
        EMPTY,
        EMPTY,
        EMPTY,
        EMPTY,
        EMPTY,
        EMPTY,
    )
    state = GameState(board=board)
    agent = QLearningAgent(
        q_values={
            (board, 0): 10.0,
            (board, 1): 1.0,
        }
    )

    assert agent.choose_action(state, (1, 2, 3)) == 1


def test_choose_action_rejects_empty_legal_moves() -> None:
    agent = QLearningAgent()
    state = GameState()

    with pytest.raises(ValueError, match="legal_moves"):
        agent.choose_action(state, ())
