from tictactoe_ai.game import EMPTY, O, X, legal_moves


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
