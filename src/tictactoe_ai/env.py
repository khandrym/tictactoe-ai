"""Stateful Tic-Tac-Toe environment."""

from tictactoe_ai.game import (
    GameResult,
    GameState,
    RESULT_ONGOING,
    game_result,
    legal_moves,
    render_board,
    reset_game,
    step_game,
)


class TicTacToeEnv:
    def __init__(self) -> None:
        self.state = reset_game()

    def reset(self) -> GameState:
        self.state = reset_game()
        return self.state

    def legal_moves(self) -> tuple[int, ...]:
        if self.done():
            return ()

        return legal_moves(self.state.board)

    def step(self, move: int) -> tuple[GameState, GameResult]:
        self.state = step_game(self.state, move)
        return self.state, game_result(self.state.board)

    def render(self) -> str:
        return render_board(self.state.board)

    def result(self) -> GameResult:
        return game_result(self.state.board)

    def done(self) -> bool:
        return self.result() != RESULT_ONGOING
