"""Self-play episode runner."""

from collections.abc import Callable
from dataclasses import dataclass

from tictactoe_ai.env import TicTacToeEnv
from tictactoe_ai.game import GameResult, GameState

MoveSelector = Callable[[GameState, tuple[int, ...]], int]


@dataclass(frozen=True)
class SelfPlayTurn:
    state: GameState
    move: int
    next_state: GameState
    result: GameResult


@dataclass(frozen=True)
class SelfPlayEpisode:
    turns: tuple[SelfPlayTurn, ...]
    final_state: GameState
    result: GameResult


def run_self_play_episode(select_move: MoveSelector) -> SelfPlayEpisode:
    """Run one full self-play episode using the same selector for both players."""
    env = TicTacToeEnv()
    turns = []

    while not env.done():
        state = env.state
        move = select_move(state, env.legal_moves())
        next_state, result = env.step(move)
        turns.append(
            SelfPlayTurn(
                state=state,
                move=move,
                next_state=next_state,
                result=result,
            )
        )

    return SelfPlayEpisode(
        turns=tuple(turns),
        final_state=env.state,
        result=env.result(),
    )


def run_self_play_episodes(
    select_move: MoveSelector,
    episode_count: int,
) -> tuple[SelfPlayEpisode, ...]:
    """Run multiple self-play episodes."""
    if episode_count < 0:
        raise ValueError("episode_count must be non-negative")

    return tuple(run_self_play_episode(select_move) for _ in range(episode_count))
