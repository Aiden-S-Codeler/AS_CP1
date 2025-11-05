# AS 2nd maze program

# 4-5, importing things need for mave generation
import turtle
import random
solvability = False
# 8-24, seting up grids for deciding where walls go in the maze
row_grid = [
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1]
]

col_grid = [
    [0, '', '', '', '', 1],
    [1, '', '', '', '', 1],
    [1, '', '', '', '', 1],
    [1, '', '', '', '', 1],
    [1, '', '', '', '', 1],
    [1, '', '', '', '', 0]
]

# 27-54, setting up function to check is the maze is solvable
def is_solvable(row_grid, col_grid):
    size = len(row_grid) - 1
    visited = set()
    stack = [(0, 0)]
    while stack:
        x, y = stack.pop()

        if x == size - 1 and y == size - 1:
            return True
        
        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x < size - 1 and col_grid[y][x+1] == 0:
            stack.append((x+1, y))
        
        if y < size - 1 and row_grid[y+1][x] == 0:
            stack.append((x, y+1))
        
        if x > 0 and col_grid[y][x] == 0:
            stack.append((x-1, y))
        
        if y > 0 and row_grid[y][x] == 0:
            stack.append((x, y-1))
    
    return False

# 57-79, make random maze

def turtle_engineering(row_grid, col_grid):
    for w in [1, 2, 3, 4]:
        for x in [0, 1, 2, 3, 4, 5]:
            open_close = random.randint(0, 1)
            if open_close == 0:
                row_grid[w][x] = 0
            else:
                row_grid[w][x] = 1
    for column1 in col_grid:
        for row2 in column1:
            if row2 == 1 or row2 == 0:
                pass
            else:
                open_close = random.randint(0, 1)
                if open_close == 0:
                    row_grid[w][x] = 0
                else:
                    row_grid[w][x] = 1
    return(row_grid, col_grid)
row_grid, col_grid = turtle_engineering(row_grid, col_grid)

# 82-, making turtles, setting them to correct specs, and screen to make maze on
screen = turtle.Screen()
ut1 = turtle.Turtle()
ut1.pensize(2)
ut1.teleport(0,30)
ut1.right(90)
st1 = turtle.Turtle()
st2 = turtle.Turtle()
st3 = turtle.Turtle()
st4 = turtle.Turtle()
st5 = turtle.Turtle()
st6 = turtle.Turtle()
st1.pensize(2)
st2.pensize(2)
st3.pensize(2)
st4.pensize(2)
st5.pensize(2)
st6.pensize(2)
st1.teleport(0,30)
st2.teleport(0,10)
st3.teleport(0,-10)
st4.teleport(0,-30)
st5.teleport(0,-50)
st6.teleport(0,-70)

# -, commanding turtles to draw their part of the maze
xval = 0
for column in col_grid:
    for row in column:
        if row == 1:
            ut1.pendown()
            ut1.forward(20)
        else:
            ut1.penup()
            ut1.forward(20)
    xval += 20
    ut1.teleport(xval, 30)
    

turtle.done()