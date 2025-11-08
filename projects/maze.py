
# Ic period 1 Maze 
#importing turtle and random
import turtle as t
import random

# Screen setup
t.Screen()
t.setup(1000, 1000)
t.speed(0)

# Maze parameters
rows, cols = 6, 6
cell_size = 60

# Starting position for drawing
start_x = -cols * cell_size // 2
start_y = rows * cell_size // 2

# Function to draw a square
def draw_wall(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.right(90)

# drawing the maze so its looks good
for r in range(rows):
    for c in range(cols):
        x = start_x + c * cell_size
        y = start_y - r * cell_size

        # Mark start and end points
        if (r, c) == (0, 0):
            t.penup()
            t.goto(x + 10, y - cell_size // 2)
        elif (r, c) == (rows - 1, cols - 1):
            t.penup()
            t.goto(x + 10, y - cell_size // 2)
        else:
            # Randomly decide if cell is a wall
            if random.random() < 0.3:  # 30% chance for wall
                draw_wall(x, y, cell_size)

# Keep window open
t.done()
