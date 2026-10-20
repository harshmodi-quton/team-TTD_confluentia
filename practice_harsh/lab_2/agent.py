from environment import Environment
from policy import Bts
from policy import Value_Learning
from policy import Q_Learning
from scorer import do_all
import json
env = Environment()
data ={}
bts= Bts()
value_learning = Value_Learning()
q_learning = Q_Learning()
env.reset()
i=1

while (not env.learning_data["done"]):
    history = env.ask(bts.move())
    bts.analyse(history)
    data["bts"][i] = history
    i+=1

"""--------------------------------=================--------------------------------"""

env.reset()
i=1

while (not env.learning_data["done"]):
    history = env.ask(value_learning.move())
    value_learning.analyse(history)
    data["value_learning"][i] = history
    i+=1

"""--------------------------------=================--------------------------------"""

env.reset()
i=1

while (not env.learning_data["done"]):
    history = env.ask(q_learning.move())
    q_learning.analyse(history)
    data["q_learning"][i] = history
    i+=1

with open ("Documentation.json", "w") as f:
    json.dump (data,f)

do_all()