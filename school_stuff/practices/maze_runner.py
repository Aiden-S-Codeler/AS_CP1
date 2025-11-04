# AS 2nd maze program

# 4-5, importing things need for mave generation
import turtle
import random

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
    [0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0]
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

# 57-79, looping maze design until the maze is solvable
solvability = False
while solvability == False:
    for w in range(2, 5):
        for x in range(6):
            open_close = random.randint(1, 2)
            if open_close == 1:
                row_grid[w][x] = 0
            else:
                row_grid[w][x] = 1
    for y in range(6):
        for z in range(2, 5):
            open_close = random.randint(1, 2)
            if open_close == 1:
                col_grid[y][z] = 0
            else:
                col_grid[y][z] = 1
    if is_solvable(row_grid, col_grid) == False:
        pass
    elif is_solvable(row_grid, col_grid) == True:
        solvability = True
    else:
        continue
    is_solvable(row_grid, col_grid)

# 82-124, making turtles, setting them to correct specs, and screen to make maze on
screen = turtle.Screen()
ut1 = turtle.Turtle()
ut2 = turtle.Turtle()
ut3 = turtle.Turtle()
ut4 = turtle.Turtle()
ut5 = turtle.Turtle()
ut6 = turtle.Turtle()
ut1.pensize(2)
ut2.pensize(2)
ut3.pensize(2)
ut4.pensize(2)
ut5.pensize(2)
ut6.pensize(2)
ut1.teleport(0,30)
ut2.teleport(10,30)
ut3.teleport(20,30)
ut4.teleport(30,30)
ut5.teleport(40,30)
ut6.teleport(50,30)
ut1.right(90)
ut2.right(90)
ut3.right(90)
ut4.right(90)
ut5.right(90)
ut6.right(90)
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
st2.teleport(0,20)
st3.teleport(0,10)
st4.teleport(0,0)
st5.teleport(0,-10)
st6.teleport(0,-20)

# 127-, commanding turtles to draw their part of the maze
for 