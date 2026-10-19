from environment import Environment
from policy1 import BinarySearch
from agent import Agent
from collections import defaultdict
import json
env = Environment()
policy = BinarySearch()
agent = Agent(env, policy)
documentary={}
env.reset()
for w in range(10):
    env.reset()
    policy.__init__()
    agent.__init__(env, policy)
    value, history = agent.run_episode()
    documentary[w] = (value, history)

with open ("Documentation.json", "w") as f:
    json.dump(documentary, f)

while True:
    with open ("Documentation.json") as f:
        print("which file do u want to see")
        thisone= input()
        print(json.load(f) [thisone])
