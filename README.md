# kore-beta-bot

https://www.kaggle.com/competitions/kore-2022-beta/discussion/317737

Usage:

```python
from src.main import agent
from kaggle_environments import make

env = make("kore_fleets")
env.run([agent, agent])
env.render(mode="ipython", width=1000, height=800)
```
