# AS 2nd fix game

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        # below is is string, and cannot be compared to an int (old: input("Enter your guess: ")) syntax error
        guess = int(input("Enter your guess: "))
        # below will only allow you do 9 attempts (old: if attempts >= max_attempts:) logic error
        if attempts > max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        # still says to try again even after going over guess limit (old: if guess == number_to_guess:) logic error
        elif guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")  
        # did not make it so that you could go over guess limit (old: N/A) logic error
        attempts += 1
        continue
    print("Game Over. Thanks for playing!")
start_game()