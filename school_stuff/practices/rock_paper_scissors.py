# AS 2nd rock paper scissors

playing = True
import random

while playing == True:
    play = input("rock, paper, or scissors")
    if play == "rock" or play == "paper" or play == "scissors":
        pass
    else:
        print("Invalid statement, pleas make sure you have no captal letters")
        continue
    robot = random.randint(1, 3)
    if robot == 1:
        robot = "rock"
    elif robot == 2:
        robot = "paper"
    elif robot == 3:
        robot = "scissors"
    else:
        print("Something broke. Restarting.")
        continue