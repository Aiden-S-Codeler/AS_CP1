# AS gambling game
start = False
chosen = False
balance = 100
bet = 0
import random

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
    is_inrange = False
    while is_inrange == False:
        bet = input(f"How much do you want to bet?\nCurrent balance: {balance}\n")
        if bet.isdigit():
            bet = int(bet)
            if bet <= balance:
                is_inrange = True
            else:
                print("Bet must be less than or equal to your balance.")
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

def slots():
    global balance
    global bet
    slots_pos = ["Apple", "Banana", "Lemon", "Grape", "Slot"]
    is_inrange = False
    while is_inrange == False:
        bet = input(f"How much do you want to bet?\nCurrent balance: {balance}\n")
        if bet.isdigit():
            bet = int(bet)
            if bet <= balance:
                is_inrange = True
            else:
                print("Bet must be less than or equal to your balance.")
        else:
            print("Please choose number.")
    slot_1 = slots_pos[random.randint(0, 4)]
    slot_2 = slots_pos[random.randint(0, 4)]
    slot_3 = slots_pos[random.randint(0, 4)]
    print(f"---{slot_1}---{slot_2}---{slot_3}---")
    if slot_1 == "Slot" and slot_1 == slot_2 and slot_1 == slot_3:
        print("JACK POT!")
        balance += bet * 10
    elif slot_1 == slot_2 and slot_1 == slot_3:
        balance += bet * 5
        print(f"You win! Current balance: {balance}")
    elif slot_1 == slot_2 or slot_1 == slot_3 or slot_2 == slot_3:
        balance += bet * 2
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
        slots()
    else:
        pass
    while chosen == True:
        replay = input("Would you like to play again? Please input Y is yes or N if no.\n")
        if replay == "Y":
            pass
            chosen = False
        elif replay == "N":
            print("Ending program.")
            start = True
            chosen = False
        else:
            print("Invalid entry.")