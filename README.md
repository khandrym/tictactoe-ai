# Tic-Tac-Toe AI

Small Python lab for learning how game agents are trained through self-play.

## Example

```python
from tictactoe_ai.env import TicTacToeEnv

env = TicTacToeEnv()
env.step(4)

print(env.render())
print(env.result())
```
