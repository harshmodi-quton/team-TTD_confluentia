from environment import Robobatteryenv
from policies import Qlearning_agent

env=Robobatteryenv()
agent=Qlearning_agent()

episodes=500
for i in range(episodes):
    raw_state = env.reset()
    curr_state = raw_state
    game_over=False

    while not game_over:
        action=agent.choose_action(curr_state)
        next_obs,reward,done,info = env.step(action)
        next_state=next_obs[0]

        agent.learn(curr_state,action,reward,next_state)

        curr_state = next_state
        game_over = done


print("Training completed: final output Q_table")
for position in sorted(agent.q_table.keys()):
    print(f"Position {position}: {agent.q_table[position]}")
print(next_obs[2])
