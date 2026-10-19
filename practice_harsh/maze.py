MAZE = ["S........",        ".........",        "....,....",        ".........",        "........G"]
def solve(maze):
    global row
    row= len(maze)
    global column
    column = len(maze[0])
    grid = [[None]*len(maze[0]) for _ in range (len(maze))]
    for i, w in enumerate (maze):
        for j, ch in enumerate (maze[i]):
            if ch== "#":
                grid [i][j] = "#"
            elif ch== "S":
                loc_S = (i,j)
                grid[i][j]=0
            elif ch =="G":
                loc_G = (i, j)
                grid[i][j]= None
    check(loc_S, 0, grid)
    least= grid[loc_G[0]][loc_G[1]]
    draw(loc_G, least, grid,loc_S)
    print (least)
    for i, w in enumerate (grid):
        for ch in grid[i]:
            if ch=="*" or ch== "#":
                print (ch, end = "")
            else :
                print (end = ".")
        print ()

    
def check(pos, n, grid):
    for w in [(1,0),(0,1),(-1,0),(0,-1)]:
        if 0<=pos[0]+w[0]< row and 0<= pos[1]+w[1]<column :
            if grid[pos[0]+w[0]][pos[1]+w[1]]==None:
                grid[pos[0]+w[0]][pos[1]+w[1]]= n+1
                check((pos[0]+w[0],pos[1]+w[1]), n+1, grid)
    
def draw(pos, n, grid,loc_S):
    grid[pos[0]][pos[1]] = "*"
    for w in [(-1,0),(1,0),(0,1),(0,-1)]:
        if 0<=pos[0]+w[0]< row and 0<= pos[1]+w[1]< column :    
            if grid[pos[0]+w[0]][pos[1]+w[1]]==n-1:
                n-=1
                grid[pos[0]+w[0]][pos[1]+w[1]]= "*"
                draw((pos[0]+w[0],pos[1]+w[1]), n, grid,loc_S)
    

solve (MAZE)