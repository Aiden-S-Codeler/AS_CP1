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

# 57-, make random maze
def turtle_engineering(row_grid, col_grid):
    for row1 in row_grid:
        for column2 in row1:
            if row1[column2] == 1:
                continue
            else:
                open_close = random.randint(1, 2)
                if open_close == 1:
                    row1[column2] = 0
                else:
                    row1[column2] = 1
    for column1 in col_grid:
        for row2 in column1:
            if column1[row2] == 1:
                pass
            else:
                open_close = random.randint(1, 2)
                if open_close == 1:
                    column1[row2] = 0
                else:
                    column1[row2] = 1
    return(row_grid, col_grid)

# 78-, looping maze production untill its solvable
while solvability == False:
    turtle_engineering(row_grid, col_grid)
    row_grid, col_grid = turtle_engineering(row_grid, col_grid)
    if is_solvable(row_grid, col_grid) == False:
        row_grid = [
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1]
        ]
        col_grid = [
            [1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1]
        ]
        print("p")
        continue
    else:
        solvability = True

# 82-, making turtles, setting them to correct specs, and screen to make maze on
screen = turtle.Screen()
ut1 = turtle.Turtle()
ut1.pensize(2)
ut1.teleport(0,30)
ut1.right(90)
st1 = turtle.Turtle()
st1.pensize(2)
st1.teleport(0,30)

# -, commanding turtles to draw their part of the maze
xval = 0
yval = 30
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
for row_ in row_grid:
    for column_ in row_:
        if column_ == 1:
            st1.pendown()
            st1.forward(20)
        else:
            st1.penup()
            st1.forward(20)
    yval -= 20
    st1.teleport(0, yval)
    

turtle.done()