"""Lab 2 - Q-learning on a 5x5 grid, from scratch (Python + numpy only).

Three ways to find the way from S to G:
1. BFS - you see the whole map (pure CP)
2. Value iteration - you know the rules, so you run a DP (Bellman)
3. Q-learning - you only get to PLAY: act, observe, get reward (RL)
"""

import random
from collections import deque
# import numpy as np 

Gridworld_TOOL = {
    "name": "Gridworld",
    "description": "Select valid moves from choices [\"up\",\"down\",\"left\",\"right\"], goal: to reach G from starting position S ",
    "parameters": {
        "type": "object",
        "properties": {"move": {"type": "string"}},
        "required": ["move"],
    }
}

class gridworld_env:
    def __init__(self,max_steps=30):
       
       self.GRID = [
                     "S..#.",
                     ".#.#.",
                     ".#...",
                     "...#.",
                     "##..G",
                   ]
       self.rows=len(self.GRID)  
       self.cols=len(self.GRID[0])
       H=self.rows
       W=self.cols
       def find(ch):
            for i in range(H):
                for j in range(W):
                    if self.GRID[i][j]==ch:
                        return i*W+j #gives one unique id instead of a tuple (coord_1,coord2)
       self.START=find("S")      
       self.GOAL=find("G")
       self.N_MOVES=4
       self.N_STATES=H*W
       self.max_steps=max_steps
       self.MOVES={"up":(-1,0),"down":(1,0),"left":(0,-1),"right":(0,1)}
             

    def reset(self,seed=None):
        
        self.pos=self.START
      
        self.steps,self.solved=0,False

        self.done=False

        return f"current position: {self.pos},goal: {self.GOAL},steps: {self.steps},grid: {self.GRID}"

    def transition(self,s,a):
        H=self.rows
        W=self.cols
        r,c=divmod(s,W)
        dr, dc = self.MOVES.get(a, (0, 0)) #I used .get() cuz if it encounters any illegal move it passes a default value (0,0)
        nr,nc=r+dr,c+dc
        if 0<=nr<H and 0<=nc<W and self.GRID[nr][nc]!="#":
            s=nr*W+nc
            if s==self.GOAL:
                reward=1.0
                return s,reward,True
        reward=-0.01 #every step counts - don't waste steps
        return s,reward,False

    def step(self,move):
        if self.done: #1
            return "returned early",0.0,self.done  
        self.steps+=1 #2
        s2, reward, reached = self.transition(self.pos, move)
        self.solved=reached
        self.pos=s2
        self.done = self.solved or self.steps >= self.max_steps
        return f"current position: {self.pos},goal: {self.GOAL},steps: {self.steps},grid: {self.GRID}",reward,self.done
        


    def verify(self):
        # 05. Compute final Reward
        return 1.0-self.steps*0.02 if self.solved else 0.0
#1--BFS--



#2--value_iteration--



#3--qlearning--

