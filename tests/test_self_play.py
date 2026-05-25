import pytest

from tictactoe_ai.game import EMPTY, RESULT_ONGOING, RESULT_X_WIN, O, X
from tictactoe_ai.self_play import run_self_play_episode, run_self_play_episodes


def test_run_self_play_episode_plays_until_game_over() -> None:
    episode = run_self_play_episode(lambda _state, moves: moves[0])

    assert episode.result == RESULT_X_WIN
    assert len(episode.turns) == 7
    assert episode.final_state.current_player == X


def test_run_self_play_episode_records_turn_transitions() -> None:
    episode = run_self_play_episode(lambda _state, moves: moves[0])
    first_turn = episode.turns[0]

    assert first_turn.state.board == (EMPTY,) * 9
    assert first_turn.move == 0
    assert first_turn.next_state.board == (
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
    assert first_turn.result == RESULT_ONGOING


def test_run_self_play_episode_records_terminal_transition() -> None:
    episode = run_self_play_episode(lambda _state, moves: moves[0])
    last_turn = episode.turns[-1]

    assert last_turn.result == RESULT_X_WIN
    assert last_turn.next_state == episode.final_state


def test_run_self_play_episode_uses_same_selector_for_both_players() -> None:
    players = []

    def select_first_move(state, moves):
        players.append(state.current_player)
        return moves[0]

    run_self_play_episode(select_first_move)

    assert players == [X, O, X, O, X, O, X]


def test_run_self_play_episode_rejects_illegal_selector_move() -> None:
    with pytest.raises(ValueError, match="empty cell"):
        run_self_play_episode(lambda _state, _moves: 0)


def test_run_self_play_episodes_returns_requested_count() -> None:
    episodes = run_self_play_episodes(lambda _state, moves: moves[0], 3)

    assert len(episodes) == 3
    assert [episode.result for episode in episodes] == [
        RESULT_X_WIN,
        RESULT_X_WIN,
        RESULT_X_WIN,
    ]


def test_run_self_play_episodes_allows_zero_count() -> None:
    assert run_self_play_episodes(lambda _state, moves: moves[0], 0) == ()


def test_run_self_play_episodes_rejects_negative_count() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        run_self_play_episodes(lambda _state, moves: moves[0], -1)
