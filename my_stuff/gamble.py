# AS gambling game
start = False
chosen = False
balance = 100
bet = 0
def roulette():


while start == False:
    while chosen == False:
        game_list = ["black jack", "texas hold 'em", "roulette", "slots"]
        game_choose = input("What game would you like to play?\nchoices: black jack, texas hold 'em, roulette, slots\n")
        if game_choose in game_list:
            print("Good choice.")
            chosen = True
        else:
            print("Game choice not among games available.")
