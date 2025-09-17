# AS 2nd random number

import random

print(random.random()) #float betweeN 1 and 0
print(random.randint(1, 6)) #random int between x and y (x, y)

name = input("gimme name: \n").strip().title()

# D&D random stat maker
stat1 = random.randint(1, 10) + random.randint(1, 10)
stat2 = random.randint(1, 10) + random.randint(1, 10)
stat3 = random.randint(1, 10) + random.randint(1, 10)
stat4 = random.randint(1, 10) + random.randint(1, 10)
stat5 = random.randint(1, 10) + random.randint(1, 10)
stat6 = random.randint(1, 10) + random.randint(1, 10)

print(f"Your stat options are: {stat1},  {stat2},  {stat3},  {stat4},  {stat5},  {stat6}")