class Robobatteryenv:
    def __init__ (self):
        self.current=0
        self.goal=5
        self.steps=0

    def reset(self):
        self.current=0
        self.steps=0
        return self.current

    def step(self,move):
        
        self.steps+=1
        if move == 1:
            self.current+=1
        elif move == 0:
            self.current-=1
        else:
            info = f"action: not moved | {move} is not a valid move, please enter a move from the valid choices of 0 or 1"
            return [self.current,self.goal,self.steps],0,False,info

        obs=[self.current,self.goal,self.steps]
        reward = 0
        done = False
        info = f"action: moved | current position: {self.current} | goal: {self.goal} | steps: {self.steps}"
        
        
        if self.current == self.goal:
            reward,done = 10,True
            return obs,reward,done,info
       
        else:
            reward=-1
        
        return obs,reward,done,info
        
        
            