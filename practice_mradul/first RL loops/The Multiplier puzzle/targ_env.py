import random

targ_TOOL = {
    "name": "targ",
    "description": "Initial state=1, Either multiply the current state by 2 or add 3 to current state comprising a step, to reach the target radom number",
    "parameters": {
        "type": "object",
        "properties": {"op": {"type": "string"}},
        "required": ["op"],
    }
}

class targ_env:
    
    def reset(self,seed=None):
        self.current=1
        rng=random.Random(seed)
        self.target=rng.randint(10,50)
        self.steps,self.solved=0,False
        return f"current state: {self.current} | target state: {self.target} | apply_op add 3 or multiply 2"

    
    def step(self,op):
        self.steps+=1

        if op=="+3":
            self.current+=3
       
        elif op=="*2":
            self.current*=2

        else:
            return f"Invalid op '{op}'. Use '+3' or '*2'.", self.steps >= 8

        if self.current == self.target:
            self.solved = True
            return "Target Number rached", True

        obs = f"current state: {self.current} | target state: {self.target}" if self.current <= self.target else "overshot"
        done = self.current > self.target or self.steps >= 8
        return obs, done
    
    
    def verify(self):
        return 1.0 - 0.08 * self.steps if self.solved else 0.0

if __name__ == "__main__":
    env = targ_env()
    print("RESET:", env.reset(seed=12))  

    for move in ["+3", "*2", "+3", "*2", "+3", "*2"]:
        obs, done = env.step(move)
        print(f"Action: {move} | Obs: {obs} | Done: {done}")
        if done:
            break
            
    print("Final Reward:", env.verify())
        
        
        
        

    
