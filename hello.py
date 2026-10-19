#f-strings and printing
# fname = "mradul"
# midname = "pratap"
# lastname = "singh"
# math=25
# cso=26
# phy=17
# pi=3.14159265
# print(fname,midname,lastname,sep=" ",end="\n")
# print(f"{fname} {midname} {lastname} scored {math} in math, {cso} in cso, {phy} in physics")
# print(f"pi to 3 decimal places {pi: .3f}")
# print(f"[{math:5d}] [{cso:<5d}] [{phy:05d}]")
# print(f"{math=}, {cso=}")
# print(f"{0.123456: .3%}")

#reading input // note- input() reads one line as a string, without trailing newline, convert it yourself

# n = int(input())
# arr = list(map(int,input().split())) #input(): Reads the entire line from the terminal as a single raw string: "3 1 4".   .split(): Chops that string at every whitespace, producing a list of text pieces: ["3", "1", "4"].   map(int, ...): Takes the int function and applies it to every piece in that list, converting them from text into actual math integers: 3, 1, 4.   list(...): The map command actually creates a lazy generator object to save memory, so wrapping it in list() forces it to immediately evaluate all the numbers and pack them into a standard Python list: [3, 1, 4]. 
# first, second = input().split()
# print(n,arr,first,second)
# print(sum(arr), max(arr), sorted(arr))

#try it - 1
# a,b = map(int,input().split())
# print(f"sum={a+b}")
# print(f"difference={a-b}")
# print(f"product={a*b}")
# print(f"floorquotient={a//b}")
# print(f"remainder={a%b}")

#try it - 2
# pi=3.14159
# print(f"pi to 2 decimal placed padded with width 10 = {pi:10.2f}")

#try it - 3
# int("3.7") - gives ValueError: invalid literal for int() with base 10
# print(int(float("3.7")))

#if/elif/else
# score = int(input())
# ok = 0<=score<=100
# if ok:
#     if score>=90:
#         grade = "A"
#     elif score>=75:
#         grade = "B"
#     else:
#         grade = "C"
# else:
#     grade="undefined"
# print(grade)

#while loop (no do while)

#collatz sequence
# n,steps = 999,0
# while n!=1:
#     n=n//2 if n%2==0 else 3*n+1
#     steps+=1
# print(f"steps:{steps}")

#while True (not true)
# x=0
# while True:
#     x+=7
#     if x%5==0:
#         break
# print(f"first multiple of 7 divisible by 5 is {x}")

#for loop
# nums = [10,20,30]
# for x in nums:
#     print(x,end=" ")
# print()
# for i,x in enumerate(nums):
#     print(f"nums[{i}]={x}")
# for i in range(3):
#     for j in range(3):
#         if i==j:
#             continue
#         else:
#             print(f"({i},{j})",end=" ")
#     print()
# print()
# names=["a","b","c"]
# for name,num in zip(names,nums):
#     print(f"({name},{num})",end=" ")
# print()

#for else
# n=31
# for d in range(2,int(n**0.5)+1):
#     if n%d==0:
#         print(f"{n} is divisible by {d}")
#         break
        
# else:
#     print(f"{n} is a prime")

#match case

# def describe(action):
#     match action:
#         case "up" | "w" | "W":
#             return "move up"
#         case "down" | "s" | "S":
#             return "move down"
#         case "right" | "d" | "D":
#             return "move right"
#         case "left" | "a" | "A":
#             return "move left"
#         #multiline f string in python

# print(f"""{describe("w")}
#       {describe("W")} 
#       {describe("s")}
#       {describe("D")}
#       {describe("right")}
#       {describe("down")}
#       {describe("A")}
#       {describe("up")}"""
# )

#try it 4
# for i in range(1,20+1):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)

#try it 5
# for i in range(10,0,-1):
#     print(f"7x{i}={7*i}")


#try it 6
# seq = [4, 6, 9, 11, 15]
# for elem in seq:
#     for i in range(2,int(elem**0.5)+1):
#         if(elem%i==0):
#             break
#     else:
#         print(elem)
#         break
# else:
#     print("None")

# a=[0,10,20,30,40,50]
# print(a[1:4])
# print(a[:3])
# print(a[3:])
# print(a[-2:])
# print(a[::2])
# print(a[::-1])
# b = a[:] #full slice = a copy, b=a doesnt make a copy
# b[0] = 99
# print (a[0], b[0]) 

#sorting with keys - v.sort() sort in place - sorted(v) returns new sorted list leaves v alone
# words = ["banana", "kiwi", "apple", "fig"]
# print(sorted(words)) #alphabetically
# print(sorted((words),key=len))
# print(sorted((words),key=len,reverse=True))
# print(sorted((words),reverse=True))

# pairs = [(3,"c"),(1,"z"),(3,"a"),(2,"b")]
# print(sorted(pairs))
# print(sorted((pairs),key=lambda p:(p[0],-ord(p[1]))))

#list comprehension
# arr = [x for x in range(1,6)]
# squares = [x*x for x in range(1,6)]
# squares2 = list(map(lambda x: x*x ,arr))
# print(squares)
# print(squares2)
# evens = [x for x in range(1,21) if x%2==0]
# words = ["alpha","giga","beta"]
# lengths = [len(x) for x in words]
# upper = [w.upper() for w in words]
# print(lengths,upper,sep="\n")

# n,m = 3,4
# bad = [[0]*n]*m
# bad[0][0]=1
# print("bad: ",bad)

# good = [[0]*n for y in range(m)]
# good[0][0]=1
# print("good: ",good)

# maze=["#..",".#.","..#"]
# for r,row in enumerate(maze):
#     for c,ch in enumerate(row):
#         if ch=="#":
#             print("wall at: ",r,c)

#try it 7
# a=[5,3,8,1,9,2]
# a.sort()
# print(a[-1:-4:-1])

#try it 8
# grid = [[r*c for c in range(1,6)] for r in range(1,6)]
# for x in grid:
#     for y in x:
#         print(y,end=" ")
#     print()

#try it 9
# seq = ["b:3", "a:10", "c:1"]
# print(sorted((seq),key=lambda s:(int(s.split(":")[1]))))

#try it 10
# n,m=4,5
# ls = [[0]*m]*n
# ls[0][0]=1
# print(ls)
# ls2 = [[0]*m for i in range(n)]
# ls2[0][0]=1
# print(ls2)

# line = "3 + 1 + 2"
# parts = line.split(" + ")
# print(parts)
# print("+".join(sorted(parts)))
# csv = "name,age,city"
# new=csv.split(",")
# print(new)
# words=["agents", "use", "tools"]
# print(" ".join(words),"-".join(words))
# nums = [1,2,3,4]
# print("".join(list(map(str,nums))))

