import random
class Judge:
    def __init__(self, seed):
        self.secret= random.Random(seed).randint(1, 100)
        self.queries=0
        self.max_quieries= 10
    def ask(self, n):
        self.queries+=1
        if self.queries<= self.max_queries:
            if(n== self.secret):
                return "correct"
            elif(n<self.secret):
                return "higher"
            else: return "lower"
        else:
            raise RuntimeError("query limit exeeded")
def search(solver):
    lo=1, hi=100
    while True:
        mid= (lo+ hi) // 2
        answer = solver.ask(mid)
        if(answer=="correct"): return mid
        else:
            lo=mid +1 if answer== "higher" else hi= mid -1 
worst = 0
for seed in range(1000):
    solver= Judge(seed)
    found = search(solver)
    assert found == solver.secret
    worst = max(worst, solver.queries)
print("solved 1000 games, worst case:", worst, "queries")
