# AS gambling game 2014 (trust)

import random

start = False
while start == False:
    game_choice = input("What game do you want to play?\nchoices: roulette, black jack, texas hold 'em, slots\n")
    game_list = ["roulette", "black jack", "texas hold 'em", "slots"]
    if game_choice in game_list:
        start = True
    else:
        print("Chosen game not in games available. Please try again.\n")

start_money = 100

def roulette():
    color = input("What color do you bet on: Red, Black, or Green")
    r_number = random.randint(0, 100)
