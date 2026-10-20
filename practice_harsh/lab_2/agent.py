from environment import Environment
from Policy import bts
from Policy import value_learning
from Policy import q_learning
import json
env = Environment()
data ={}

env.reset()
i=1

while (env.learning_data["done"]):
    history = env.ask(bts.move())
    bts.analyse(history)
    data["bts"][i] = history
    i+=1

"""--------------------------------=================--------------------------------"""

env.reset()
i=1

while (env.learning_data["done"]):
    history = env.ask(value_learning.move())
    value_learning.analyse(history)
    data["value_learning"][i] = history
    i+=1

"""--------------------------------=================--------------------------------"""

env.reset()
i=1

while (env.learning_data["done"]):
    history = env.ask(q_learning.move())
    q_learning.analyse(history)
    data["q_learning"][i] = history
    i+=1

with open ("Documentation.json", "w") as f:
    json.dump (data)
