# AS 2nd maze program

# 4-5, importing things need for mave generation
import turtle
import random

# 8-24, seting up grids for deciding where walls go in the maze
row_grid = [
    ["c", "c", "c", "c", "c", "c"],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["c", "c", "c", "c", "c", "c"]
]

col_grid = [
    ["c", "c", "c", "c", "c", "o"],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["o", "c", "c", "c", "c", "c"]
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

# 57-, looping maze production until the maze is solvable
solvabilty = False
while solvabilty == False:
    for x in range(2, 5):
        for a in row_grid(x):
            open_close = random.randint(1, 2)
            if open_close == 1:
                