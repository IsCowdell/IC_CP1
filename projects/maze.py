import turtle as t
import random

def setup():
    screen = t.Screen()
    screen.setup(800, 800)
    screen.title("Simple Maze")
    screen.bgcolor("white")
    
    maze_turtle = t.Turtle()
    maze_turtle.speed(0)
    maze_turtle.hideturtle()
    maze_turtle.pensize(2)
    return screen, maze_turtle

def draw_maze(turtle, size, rows, cols):
    # Calculate cell size and starting position
    cell_size = size // max(rows, cols)
    start_x = -size // 2
    start_y = size // 2
    
    # Create maze grid
    maze = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # Each cell has right and bottom walls by default
            row.append({'right': True, 'bottom': True})
        maze.append(row)
    
    # Generate maze using randomized DFS
    def carve_path(row, col):
        maze[row][col]['visited'] = True
        
        directions = [(0, 1, 'right'), (1, 0, 'bottom'), 
                     (0, -1, 'left'), (-1, 0, 'top')]
        random.shuffle(directions)
        
        for dy, dx, wall in directions:
            new_row, new_col = row + dy, col + dx
            
            if (0 <= new_row < rows and 0 <= new_col < cols and 
                not maze[new_row][new_col].get('visited', False)):
                
                if wall == 'right' and new_col < cols:
                    maze[row][col]['right'] = False
                elif wall == 'left' and col > 0:
                    maze[new_row][new_col]['right'] = False
                elif wall == 'bottom' and new_row < rows:
                    maze[row][col]['bottom'] = False
                elif wall == 'top' and row > 0:
                    maze[new_row][new_col]['bottom'] = False
                
                carve_path(new_row, new_col)
    
    # Start maze generation from top-left corner
    carve_path(0, 0)
    
    # Draw the maze
    turtle.clear()
    turtle.penup()
    
    # Draw the outer border
    turtle.goto(start_x, start_y)
    turtle.pendown()
    turtle.setheading(0)
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    
    # Draw the maze walls
    for i in range(rows):
        for j in range(cols):
            x = start_x + j * cell_size
            y = start_y - i * cell_size
            
            # Draw right wall
            if maze[i][j]['right']:
                turtle.penup()
                turtle.goto(x + cell_size, y)
                turtle.pendown()
                turtle.setheading(270)
                turtle.forward(cell_size)
            
            # Draw bottom wall
            if maze[i][j]['bottom']:
                turtle.penup()
                turtle.goto(x, y - cell_size)
                turtle.pendown()
                turtle.setheading(0)
                turtle.forward(cell_size)
    
    # Mark start and end
    turtle.penup()
    # Start point (green)
    turtle.goto(start_x + cell_size/2, start_y - cell_size/2)
    turtle.dot(cell_size/2, "green")
    # End point (red)
    turtle.goto(start_x + size - cell_size/2, start_y - size + cell_size/2)
    turtle.dot(cell_size/2, "red")

screen, turtle = setup()
draw_maze(turtle, 600, 8, 8)  # 600 pixels wide, 8x8 grid
screen.mainloop()
