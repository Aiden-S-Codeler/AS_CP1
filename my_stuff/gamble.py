# AS gambling game
start = False
chosen = False
balance = 100
bet = 0
import random
# can you fix the balance thing
def roulette():
    global balance
    global bet
    correct_color = False
    while correct_color == False:
        cbet = input("What color do you want to bet on? (red, black, green)\n")
        if cbet == "red" or cbet == "black" or cbet == "green":
            correct_color = True
        else:
            print("Please choose a valid color.")
    is_num = False
    while is_num == False:
        bet = input(f"How much do you want to bet?\nCurrent balance: {balance}\n")
        if bet.isdigit():
            is_num = True
            bet = int(bet)
        else:
            print("Please choose number.")
    rnumber = random.randint(0,100)
    if rnumber == 0:
        rnumber = "green"
    elif rnumber % 2 == 0:
        rnumber = "red"
    else:
        rnumber = "black"
    if rnumber == cbet:
        balance += bet
        print(f"You win! Current balance: {balance}")
    else:
        balance -= bet
        print(f"You lose. Current balance: {balance}")
    bet = 0
        

while start == False:
    while chosen == False:
        game_list = ["black jack", "texas hold 'em", "roulette", "slots"]
        game_choose = input("What game would you like to play?\nchoices: black jack, texas hold 'em, roulette, slots\n")
        if game_choose in game_list:
            print("Good choice.")
            chosen = True
        else:
            print("Game choice not among games available.")
    if game_choose == "roulette":
        roulette()
    elif game_choose == "black jack":
        pass
    elif game_choose == "texas hold 'em":
        pass
    elif game_choose == "slots":
        pass
    else:
        pass
    while chosen == True:
        replay = input("Would you like to play again? Please input Y is yes or N if no.")
        if replay == "Y":
            pass
            chosen = False
        elif replay == "N":
            print("Ending program.")
            start = True
            chosen = False
        else:
            print("Invalid entry.")