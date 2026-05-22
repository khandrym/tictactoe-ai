"""Core Tic-Tac-Toe game data."""

EMPTY = 0
X = 1
O = -1

Board = tuple[int, ...]

INITIAL_BOARD: Board = (EMPTY,) * 9

WIN_LINES: tuple[tuple[int, int, int], ...] = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def legal_moves(board: Board) -> tuple[int, ...]:
    """Return indexes of empty cells."""
    return tuple(index for index, cell in enumerate(board) if cell == EMPTY)


def winner(board: Board) -> int | None:
    """Return the winning player, if any."""
    for first, second, third in WIN_LINES:
        player = board[first]
        if player != EMPTY and player == board[second] == board[third]:
            return player

    return None


def is_draw(board: Board) -> bool:
    """Return whether the board is full without a winner."""
    return winner(board) is None and not legal_moves(board)
