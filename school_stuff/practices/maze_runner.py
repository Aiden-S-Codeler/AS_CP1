# AS 2nd maze program

# 4-5, importing things need for mave generation
import turtle
import random
solvability = False
# 8-24, seting up grids for deciding where walls go in the maze
row_grid = [
            [0, 1, 1, 1, 1, 1],
            [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)],
            [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)],
            [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)],
            [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)],
            [1, 1, 1, 1, 1, 0]
        ]

col_grid = [
            [1, 1, 1, 1, 1, 1],
            [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)],
            [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)],
            [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)],
            [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)],
            [1, 1, 1, 1, 1, 1]
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

# 57-74, make random maze
def turtle_engineering(row_grid, col_grid):
    row_grid = [
        [0, 1, 1, 1, 1, 1],
        [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)],
        [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)],
        [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)],
        [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)],
        [1, 1, 1, 1, 1, 0]
        ]
    col_grid = [
        [1, 1, 1, 1, 1, 1],
        [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)],
        [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)],
        [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)],
        [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)],
        [1, 1, 1, 1, 1, 1]
        ]
    return(row_grid, col_grid)

# 77-84, looping maze production untill its solvable
while solvability == False:
    if is_solvable(row_grid, col_grid) == False:
        turtle_engineering(row_grid, col_grid)
        row_grid, col_grid = turtle_engineering(row_grid, col_grid)
        print("p")
        continue
    else:
        solvability = True

# 87-94, making turtles, setting them to correct specs, and screen to make maze on
screen = turtle.Screen()
ut1 = turtle.Turtle()
ut1.pensize(2)
ut1.teleport(0,30)
ut1.right(90)
st1 = turtle.Turtle()
st1.pensize(2)
st1.teleport(0,30)

# 97-end, commanding turtles to draw their part of the maze

def slavery():
    xval = 0
    yval = 30
    funx = 0
    funy = 0
    for column in col_grid:
        for row in column:
            if row == 1:
                ut1.pendown()
                ut1.forward(20)
            else:
                ut1.penup()
                ut1.forward(20)
        funx += 1
        if funx == 4:
            xval += 20
        else:
            pass
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
        funy += 1
        if funy == 4:
            yval -= 20
        else:
            pass
        yval -= 20
        st1.teleport(0, yval)
    
slavery()
turtle.done()