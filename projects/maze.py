#import turle and random and then make it so that the turtles will go into different direciton and make them go away from each other make and end and begning point make evrythings the same mesurementslik ehieght and width and length
#IC 1st maze
yes = True
import turtle as t
import random 

t.Screen()
t.setup(1000,1000)
t.speed(900)
random_options = random.randint(0,1)
row_grid = [[1,1,0,0,1,0],
            [0,1,1,1,0,1]]
col_grid = [[0,1,1,0,0,1],
            [0,0,0,1,1,1]]
target_value = 1
target_value2 = 0
mick = t.Turtle()
joe = mick.clone()
sharah = mick.clone()
mick.color("green")

mick.penup()
mick.forward(50)
mick.pendown()
mick.forward(250)
mick.right(90)
mick.forward(-300)
joe.left(90)
joe.forward(300)
joe.right(90)
joe.forward(250)
joe.penup()
joe.forward(50)
joe.pendown()




def rowmaze(row_grid,random_options,target_value):
    if target_value in row_grid:
        for i in range(len(row_grid)):
            if row_grid[i] == target_value:
                row_grid[i] = random_options(0,1)
                sharah.forward(row_grid)
    return rowmaze


def colmaze(col_grid,random_options,target_value2):
    if target_value in col_grid:
        for c in range(len(col_grid)):
            if col_grid[c] == target_value2: 
                col_grid[c] == random_options(0,1)
                sharah.forward(col_grid)
    
    colmaze()


    
        
    

def is_sovlable(row_grid, col_grid):
    size = len(row_grid) - 1
    visited = set()
    stack = [(0,0)]
    while stack:
        x,y = stack.pop()
        if x == size -1 and y == size -1 :
            return True
        
        if (x,y) in visited:
            continue

        visited.add(x,y)

        if x < size - 1 and col_grid[y] [x+1] == 0:
            stack.append((x+1,y))

        if y < size - 1 and col_grid[y+1][x] == 0:
            stack.append((x,y+1))
            
