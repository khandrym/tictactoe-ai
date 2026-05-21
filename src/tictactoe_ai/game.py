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
