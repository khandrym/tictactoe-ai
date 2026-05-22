"""Core Tic-Tac-Toe game data."""

from dataclasses import dataclass
from typing import Literal

EMPTY = 0
X = 1
O = -1

Board = tuple[int, ...]
GameResult = Literal["ongoing", "x_win", "o_win", "draw"]

INITIAL_BOARD: Board = (EMPTY,) * 9

RESULT_ONGOING: GameResult = "ongoing"
RESULT_X_WIN: GameResult = "x_win"
RESULT_O_WIN: GameResult = "o_win"
RESULT_DRAW: GameResult = "draw"


@dataclass(frozen=True)
class GameState:
    board: Board = INITIAL_BOARD
    current_player: int = X


CELL_SYMBOLS = {
    EMPTY: ".",
    X: "X",
    O: "O",
}

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


def reset_game() -> GameState:
    """Return a fresh initial game state."""
    return GameState()


def step_game(state: GameState, move: int) -> GameState:
    """Return the next game state after the current player moves."""
    if is_game_over(state.board):
        raise ValueError("game is over")

    board = make_move(state.board, move, state.current_player)
    current_player = state.current_player
    if not is_game_over(board):
        current_player = next_player(state.current_player)

    return GameState(board=board, current_player=current_player)


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


def render_board(board: Board) -> str:
    """Return a compact text representation of the board."""
    rows = []
    for start in range(0, len(board), 3):
        try:
            row = " ".join(CELL_SYMBOLS[cell] for cell in board[start : start + 3])
        except KeyError as error:
            raise ValueError("board contains an invalid cell") from error
        rows.append(row)

    return "\n".join(rows)


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


def game_result(board: Board) -> GameResult:
    """Return the current game result."""
    winning_player = winner(board)
    if winning_player == X:
        return RESULT_X_WIN

    if winning_player == O:
        return RESULT_O_WIN

    if is_draw(board):
        return RESULT_DRAW

    return RESULT_ONGOING
