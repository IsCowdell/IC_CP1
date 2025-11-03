#import turle and random and then make it so that the turtles will go into different direciton and make them go away from each other make and end and begning point make evrythings the same mesurementslik ehieght and width and length

#IC 1st maze
yes = True
import turtle as t
import random 
t.Screen()
t.setup(1000,1000)
side = random.randint(10,500)

side1 = t.forward(300) and t.right(200)
col_grid = t.forward(side)

for x in range(1,4):
    t.right(90)
    t.forward(300)


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
