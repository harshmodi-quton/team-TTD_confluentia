from environment import Robobatteryenv
import random
env=Robobatteryenv()

class probabilistic_agent:

    state = env.reset()
    print(f"we are starting on {state}")
    seed=42
    rng = random.Random(seed)

    game_over = False

class Qlearning_agent:
    def __init__(self):
        self.q_table = {} #-4 to +5 through 0 starting state = 0
        self.epsilon=0.1 #epsilon_greedy - explore randomly 10 percent of the time
        self.alpha=0.1 #learning_rate -
        self.gamma=0.9 #discount_factor - how much it cares about future rewards

    def check_state(self,state):
        if state not in self.q_table:
            self.q_table[state]=[0,0]

    def choose_action(self,state):
        if state not in self.q_table:
            self.q_table[state]=[0,0]

        # EXPLORE - 10% of times
        if random.random()<self.epsilon: #random.random() chooses a pseudo random floating point between [0.0,1), so induces a condition of 10% of the times
            return random.randint(0,1)
        
        # EXPLOIT - 90% of times
        else:
            left_score,right_score = self.q_table[state][0],self.q_table[state][1]
            if left_score>right_score:
                return 0
            elif left_score<right_score:
                return 1
            else:
                return random.randint(0,1) #if scores are tied, agent chooses a random move

    def learn(self,state,action,reward,next_state):
        self.check_state(state)
        self.check_state(next_state)

        old_value = self.q_table[state][action]
        next_max = max(self.q_table[next_state])

        new_value = old_value + self.alpha * (reward + (self.gamma * next_max) - old_value)

        self.q_table[state][action]=new_value        


