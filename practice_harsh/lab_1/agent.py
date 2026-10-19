class Agent:
    def __init__(self, env, policy):
        self.env = env
        self.policy = policy

    def run_episode(self):
        history=[]
        while self.env.episode:
            guess = self.policy.choose_guess()
            feedback = self.env.action(guess)
            history.append((guess, feedback))
            self.policy.update(feedback)
        return (self.env.queries, history)