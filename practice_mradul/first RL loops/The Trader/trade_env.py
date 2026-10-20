#Exercise 2: Mini Arbitrage Trader (TradeEnv)01. Task: You start with cash = 100.0 and shares = 0. Survive 5 days of randomly fluctuating stock prices and end with total net worth $> 110.0$.02. Tools: trade(action) where action is "buy" (spend all cash on shares at today's price), "sell" (sell all shares for cash at today's price), or "hold".03. State: self.cash, self.shares, self.price, self.steps, self.solved.04. Step: Execute the trade at self.price, then update self.price by adding a random change random.randint(-10, 15).05. Termination: Ends when self.steps >= 5. At step 5, compute portfolio_value = self.cash + self.shares * self.price. If portfolio_value > 110.0, set self.solved = True.06. Verifier: Return min(1.0, (portfolio_value - 100.0) / 50.0) if self.solved else 0.0.
import random

Trade_TOOL = {
    "name": "Trade",
    "description": "Trading stocks by taking action either buy, sell or hold",
    "parameters": {
        "type": "object",
        "properties": {"act": {"type": "string"}},
        "required": ["act"],
    }
}


class Trade_env:
    def reset(self,seed=None):
        self.rng = random.Random(seed)
        self.cash=100.0
        self.shares=0
        self.price=float(self.rng.randint(20,50))
        self.steps,self.solved=0,False
        self.portfolio_value = 100.0
        return f"current state: cash = {self.cash}, shares = {self.shares}, price = {self.price}, steps = {self.steps}"
    
    def step(self,act):
        self.change=self.rng.randint(-10,15)
        self.steps+=1
        if act == "buy":
            new_shares = self.cash//self.price
            self.shares+=new_shares
            self.cash-=new_shares*self.price
        elif act == "sell":
            self.cash+=self.shares*self.price
            self.shares=0
        elif act == "hold":
            self.shares+=0
        else:
            return "invalid_action", self.steps>5

        self.price+=self.change

        if self.steps == 5:
            self.portfolio_value = self.cash + self.shares * self.price
            if self.portfolio_value > 110.0:
                self.solved = True
                return "Trade successful", True
        
        obs = f"current state: cash = {self.cash}, shares = {self.shares}, price = {self.price}, steps = {self.steps}"
        done = self.solved or self.steps>=5
        return obs, done
            

            
    def verify(self):
        return min(1.0, (self.portfolio_value - 100.0) / 50.0) if self.solved else 0.0


if __name__ == "__main__":
    env = Trade_env()
    print("RESET:", env.reset(seed=86))
    
    actions = ["buy", "hold", "hold", "hold", "sell"]
    done = False
    
    for act in actions:
        obs, done = env.step(act)
        print(f"Action: {act:5s} | Obs: {obs} | Done: {done}")
        if done:
            break
            
    print("Final Reward:", env.verify())