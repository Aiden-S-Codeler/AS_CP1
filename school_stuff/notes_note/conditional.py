# AS 2nd Conditionals
import random

number = random.randint(1,20)

if number == 20:
    print(f"crit: {number}")
elif number > 10:
    print(f"success: {number}")
elif number <= 10:
    print(f"miss: {number}")
else:
    (f"how did you acheive this outcome?: {number}")

# > greater than
# < less than
# == equals
# >= greater than or equal to
# <= less than or equal to
# != not equal to
