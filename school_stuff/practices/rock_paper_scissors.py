# AS 2nd rock paper scissors

playing = True
import random

while playing == True:
    play = input("rock, paper, or scissors?" )
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
        print("Something broke. Restarting...")
        continue
    print(f"You played: {play}. The AI played: {robot}")
    if play == robot:
      print("Tie.")
    elif play == "rock" and robot == "paper":
      print("You lose.")
    elif play == "paper" and robot == "scissors":
      print("You lose.")
    elif play == "scissors" and robot == "rock":
      print("You lose.")
    elif play == "paper" and robot == "rock":
      print("You Win!")
    elif play == "scissors" and robot == "paper":
      print("You Win!")
    elif play == "rock" and robot == "scissors":
      print("You Win!")
    else:
       print("Something broke. Restarting...")
       continue
    cont = input("Would you like to keep playing? ")
    if cont == "yes":
      continue
    else:
       print("goodbye")
       break