#1-maze
# from collections import deque
# MAZE=["S.#......",
#       ".##.####.",
#       "....#..#.",
#       ".##...#..",
#       "...#.#..G"]
# def solve(maze):
#     rows,cols=len(maze),len(maze[0])
#     dist={(0,0):0}
#     q=deque([(0,0)])
#     while q:
#         r,c=q.popleft()
#         for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
#             nr,nc=r+dr,c+dc
#             if 0<=nr<rows and 0<=nc<cols and maze[nr][nc]!="#" and (nr,nc) not in dist:
#                 dist[(nr,nc)]=dist[(r,c)] + 1
#                 q.append((nr,nc))
#     return dist[(4,8)]
# print("distance:",solve(MAZE))

#1-maze with path traceback
# from collections import deque
# MAZE=["S.#......",
#       ".##.####.",
#       "....#..#.",
#       ".##...#..",
#       "...#.#..G"]
# def solve(maze):
#     rows,cols=len(maze),len(maze[0])
#     dist={(0,0):0}
#     q=deque([(0,0)])
#     while q:
#         r,c=q.popleft()
#         if maze[r][c] == "G":
#             path,cur=[],(r,c)
#             while cur is not (0,0):
#                 path.append(cur)
#                 cur = dist[cur]
#         for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
#             nr,nc=r+dr,c+dc
#             if 0<=nr<rows and 0<=nc<cols and maze[nr][nc]!="#" and (nr,nc) not in dist:
#                 dist[(nr,nc)]=dist[(r,c)] + 1
#                 q.append((nr,nc))
#     return dist[(4,8)]
# print("distance:",solve(MAZE))

#5
# import random
# def rolls():
#     seen=set()
#     count=0
#     for i in range(20000):
#         x=random.randint(1,6)
#         seen.add(x)
#         if len(seen)==6:
#             count=i+1
#             break
#     return count
# sample=[]
# samplesize=200000
# for j in range(samplesize):
#     sample.append(rolls())
# mean = sum(sample)/samplesize
# print(mean)
# sample.sort()
# moves=sample[int(0.90*len(sample))]
# print(f"90% of the cases ended in {moves} moves")

#guess the number
import random

class judge:
    def __init__(self, min=1,max=100, maxqueries=10):
        self.secret= random.randint(min,max)
        self.queries=0
        self.maxqueries=maxqueries
    def ask(self,n):
        self.queries+=1
        if(self.queries>self.maxqueries):
            raise RuntimeError("limit exceeded")
        if n==self.secret:
            return "correct"
        elif n<self.secret:
            return "higher"
        else:
            return "lower"

def solver(judge):
    low,high=1,100
    while True:
        mid=int((low+high)/2)
        answer=judge.ask(mid)
        if answer == "correct":
            return answer
        elif answer == "higher":
            low = mid+1
        else:
            high = mid-1

worst=0
scores = []
for i in range(2000):
    my_judge = judge()
    num=solver(my_judge)
    worst = max(worst,my_judge.queries)
    scores.append(my_judge.queries)
print(worst)
print("Average guesses:", sum(scores) / len(scores))
print("Worst game:", max(scores))
print("Best game:", min(scores))