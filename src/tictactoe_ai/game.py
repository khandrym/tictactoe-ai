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


def make_move(board: Board, move: int, player: int) -> Board:
    """Return a new board after placing the player's mark."""
    if player not in (X, O):
        raise ValueError("player must be X or O")

    if move < 0 or move >= len(board):
        raise ValueError("move must be a board index")

    if board[move] != EMPTY:
        raise ValueError("move must target an empty cell")

    updated = list(board)
    updated[move] = player
    return tuple(updated)


def next_player(player: int) -> int:
    """Return the player who moves after the given player."""
    if player == X:
        return O

    if player == O:
        return X

    raise ValueError("player must be X or O")


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


def is_game_over(board: Board) -> bool:
    """Return whether the game has ended."""
    return winner(board) is not None or is_draw(board)
