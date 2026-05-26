"""Tabular Q-learning agent."""

from dataclasses import dataclass, field

from tictactoe_ai.game import Board, GameState

QTable = dict[tuple[Board, int], float]


@dataclass
class QLearningAgent:
    q_values: QTable = field(default_factory=dict)

    def q_value(self, state: GameState, move: int) -> float:
        return self.q_values.get((state.board, move), 0.0)

    def choose_action(self, state: GameState, legal_moves: tuple[int, ...]) -> int:
        if not legal_moves:
            raise ValueError("legal_moves must not be empty")

        return max(
            legal_moves,
            key=lambda move: (self.q_value(state, move), -move),
        )
