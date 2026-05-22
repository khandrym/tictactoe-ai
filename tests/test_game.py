import pytest

from tictactoe_ai.game import (
    EMPTY,
    GameState,
    INITIAL_BOARD,
    O,
    RESULT_DRAW,
    RESULT_ONGOING,
    RESULT_O_WIN,
    RESULT_X_WIN,
    X,
    game_result,
    is_draw,
    is_game_over,
    legal_moves,
    make_move,
    next_player,
    render_board,
    reset_game,
    step_game,
    winner,
)


def test_legal_moves_returns_all_cells_for_empty_board() -> None:
    board = (EMPTY,) * 9

    assert legal_moves(board) == (0, 1, 2, 3, 4, 5, 6, 7, 8)


def test_legal_moves_excludes_occupied_cells() -> None:
    board = (
        X,
        EMPTY,
        O,
        EMPTY,
        X,
        EMPTY,
        O,
        EMPTY,
        EMPTY,
    )

    assert legal_moves(board) == (1, 3, 5, 7, 8)


def test_legal_moves_returns_empty_tuple_for_full_board() -> None:
    board = (
        X,
        O,
        X,
        O,
        X,
        O,
        O,
        X,
        O,
    )

    assert legal_moves(board) == ()


def test_reset_game_returns_initial_state() -> None:
    state = reset_game()

    assert state.board == INITIAL_BOARD
    assert state.current_player == X


def test_step_game_places_current_player_mark_and_switches_player() -> None:
    state = reset_game()

    next_state = step_game(state, 4)

    assert next_state.board == (
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
    assert next_state.current_player == O


def test_step_game_uses_state_current_player() -> None:
    state = GameState(current_player=O)

    next_state = step_game(state, 0)

    assert next_state.board == (
        O,
        EMPTY,
        EMPTY,
        EMPTY,
        EMPTY,
        EMPTY,
        EMPTY,
        EMPTY,
        EMPTY,
    )
    assert next_state.current_player == X


def test_step_game_keeps_current_player_after_winning_move() -> None:
    state = GameState(
        board=(
            X,
            X,
            EMPTY,
            O,
            O,
            EMPTY,
            EMPTY,
            EMPTY,
            EMPTY,
        ),
        current_player=X,
    )

    next_state = step_game(state, 2)

    assert winner(next_state.board) == X
    assert next_state.current_player == X


def test_step_game_rejects_move_after_game_over() -> None:
    state = GameState(
        board=(
            X,
            X,
            X,
            O,
            O,
            EMPTY,
            EMPTY,
            EMPTY,
            EMPTY,
        ),
        current_player=O,
    )

    with pytest.raises(ValueError, match="game is over"):
        step_game(state, 5)


def test_make_move_returns_board_with_player_mark() -> None:
    board = (EMPTY,) * 9

    assert make_move(board, 4, X) == (
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


def test_make_move_does_not_change_original_board() -> None:
    board = (EMPTY,) * 9

    make_move(board, 4, X)

    assert board == (EMPTY,) * 9


def test_make_move_rejects_occupied_cell() -> None:
    board = make_move((EMPTY,) * 9, 4, X)

    with pytest.raises(ValueError, match="empty cell"):
        make_move(board, 4, O)


def test_make_move_rejects_move_outside_board() -> None:
    board = (EMPTY,) * 9

    with pytest.raises(ValueError, match="board index"):
        make_move(board, 9, X)


def test_make_move_rejects_invalid_player() -> None:
    board = (EMPTY,) * 9

    with pytest.raises(ValueError, match="X or O"):
        make_move(board, 4, EMPTY)


def test_next_player_returns_o_after_x() -> None:
    assert next_player(X) == O


def test_next_player_returns_x_after_o() -> None:
    assert next_player(O) == X


def test_next_player_rejects_invalid_player() -> None:
    with pytest.raises(ValueError, match="X or O"):
        next_player(EMPTY)


def test_render_board_returns_text_grid() -> None:
    board = (
        X,
        EMPTY,
        O,
        EMPTY,
        X,
        EMPTY,
        O,
        EMPTY,
        X,
    )

    assert render_board(board) == "X . O\n. X .\nO . X"


def test_render_board_rejects_invalid_cell() -> None:
    board = (
        X,
        EMPTY,
        O,
        EMPTY,
        2,
        EMPTY,
        O,
        EMPTY,
        X,
    )

    with pytest.raises(ValueError, match="invalid cell"):
        render_board(board)


def test_winner_returns_x_for_completed_row() -> None:
    board = (
        X,
        X,
        X,
        EMPTY,
        O,
        EMPTY,
        O,
        EMPTY,
        EMPTY,
    )

    assert winner(board) == X


def test_winner_returns_o_for_completed_column() -> None:
    board = (
        O,
        X,
        EMPTY,
        O,
        X,
        EMPTY,
        O,
        EMPTY,
        X,
    )

    assert winner(board) == O


def test_winner_returns_x_for_completed_diagonal() -> None:
    board = (
        X,
        O,
        EMPTY,
        EMPTY,
        X,
        O,
        EMPTY,
        EMPTY,
        X,
    )

    assert winner(board) == X


def test_winner_returns_none_without_completed_line() -> None:
    board = (
        X,
        O,
        X,
        X,
        O,
        O,
        O,
        X,
        X,
    )

    assert winner(board) is None


def test_is_draw_returns_true_for_full_board_without_winner() -> None:
    board = (
        X,
        O,
        X,
        X,
        O,
        O,
        O,
        X,
        X,
    )

    assert is_draw(board)


def test_is_draw_returns_false_when_board_has_winner() -> None:
    board = (
        X,
        X,
        X,
        O,
        O,
        X,
        O,
        X,
        O,
    )

    assert not is_draw(board)


def test_is_draw_returns_false_when_moves_remain() -> None:
    board = (
        X,
        O,
        X,
        EMPTY,
        O,
        O,
        O,
        X,
        X,
    )

    assert not is_draw(board)


def test_is_game_over_returns_true_when_board_has_winner() -> None:
    board = (
        O,
        X,
        EMPTY,
        O,
        X,
        EMPTY,
        O,
        EMPTY,
        X,
    )

    assert is_game_over(board)


def test_is_game_over_returns_true_when_board_is_draw() -> None:
    board = (
        X,
        O,
        X,
        X,
        O,
        O,
        O,
        X,
        X,
    )

    assert is_game_over(board)


def test_is_game_over_returns_false_when_game_continues() -> None:
    board = (
        X,
        O,
        X,
        EMPTY,
        O,
        O,
        O,
        X,
        X,
    )

    assert not is_game_over(board)


def test_game_result_returns_x_win() -> None:
    board = (
        X,
        X,
        X,
        O,
        O,
        EMPTY,
        EMPTY,
        EMPTY,
        EMPTY,
    )

    assert game_result(board) == RESULT_X_WIN


def test_game_result_returns_o_win() -> None:
    board = (
        O,
        X,
        EMPTY,
        O,
        X,
        EMPTY,
        O,
        EMPTY,
        X,
    )

    assert game_result(board) == RESULT_O_WIN


def test_game_result_returns_draw() -> None:
    board = (
        X,
        O,
        X,
        X,
        O,
        O,
        O,
        X,
        X,
    )

    assert game_result(board) == RESULT_DRAW


def test_game_result_returns_ongoing() -> None:
    board = (
        X,
        O,
        X,
        EMPTY,
        O,
        O,
        O,
        X,
        X,
    )

    assert game_result(board) == RESULT_ONGOING
