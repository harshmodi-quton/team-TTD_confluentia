GRID = [
    "...#.",
    ".#.#.",
    ".#...",
    "...#.",
    "##...",
]



class Environment:

    def reset(self):
        self.learning_data ={
            "position": (0,0),
            "reward": 0,
            "done": False
        }
        self.internal_track={
            "steps" : 0, 
            "position": (0,0),
            "end": (4,4)
        }

    def ask(self, direction):
        if (not self.internal_track["done"]):
            x,y =self.internal_track["position"]
            if (direction=="UP"):
                if(y>0 and GRID[y-1][x] is not "#"):
                    y-=1
            elif(direction== "DOWN"):
                if (y<4 and GRID[y+1][x] is not "#"):
                    y+=1
            elif(direction== "LEFT"):
                if(x>0 and GRID[y][x-1] is not "#"):
                    x-=1
            elif(direction== "RIGHT"):
                if (x<4 and GRID[y][x+1] is not "#"):
                    x+=1
        self.learning_data["position"]= self.internal_track["position"]=(x,y)    
        if(self.internal_track["position"]==self.internal_track["end"]):
            self.learning_data["reward"]= self.learning_data["reward"]+ 1.0
            self.learning_data["done"]= True
        else :
            self.learning_data["reward"]= self.learning_data["reward"]- 0.01
        self.internal_track["steps"]=self.internal_track["steps"]+ 1
        if(self.internal_track["steps"]==50):
            self.learning_data["done"]= True
        return self.learning_data