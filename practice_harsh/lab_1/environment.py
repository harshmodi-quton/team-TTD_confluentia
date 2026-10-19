import numpy as np
class Environment:
    MAX_LIMIT = 10
    def reset(self, seed= None):
        rng = np.random.default_rng(seed)
        self.secret= rng.integers(1,101)
        self.queries=0
        self.episode = True
        return "try to find the secret number"

    def action(self, n):
        if (self.episode):
            if(self.queries< self.MAX_LIMIT):
                self.queries+=1
                if(self.queries == self.MAX_LIMIT): self.episode = False
                if (n == self.secret):
                    self.episode=False
                    return "Correct"
                elif(n> self.secret):
                    if(self.episode): 
                        return "Try Lower"
                    else:
                        return "wrong it was ur last attempt, it is lower"
                elif (n< self.secret):
                    if(self.episode): 
                        return "Try Higher"
                    else:
                        return "wrong it was ur last attempt, it is higher"
                else :
                    if(self.episode): 
                        return "Questionable input"
                    else:
                        return "wrong it was ur last attempt"
            else :
                self.episode= False
                return "Query limit reached"
        else:
            return "Illegal try"