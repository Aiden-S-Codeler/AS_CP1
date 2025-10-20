# AS 2nd function notes

balance = 100
bet = 0
import random
import time

def blackjack():
    global balance
    global bet
    start_val = random.randint(1, 10) + random.randint(1, 10)
    deal_start_val = random.randint(1, 10) + random.randint(1, 10)
    while deal_start_val < 16:
        deal_start_val += random.randint(1, 10)
        if deal_start_val > 21:
            deal_start_val = random.randint(1, 10) + random.randint(1, 10)
        else:
            pass
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
    done = False
    while done == False:
        print(f"You currently have a card value of: {start_val}")
        hit_stand = input("Would you like to hit or stand?: ")
        if hit_stand == "hit":
            start_val += random.randint(1, 10)
            if start_val > 21:
                print(f"You busted with a value of {start_val}.")
                balance -= bet
                print(f"You lose. Current balance: {balance}")
                done = True
            else:
                print(f"Current value: {start_val}")
        elif hit_stand == "stand":
            if start_val == 21:
                balance += bet * 2
                print(f"You got a black jack! Dealer had {deal_start_val}. Current balance: {balance}")
                done = True
            elif start_val > deal_start_val:
                balance += bet
                print(f"You win! Dealer had {deal_start_val}. Current balance: {balance}")
                done = True
            else:
                balance -= bet
                print(f"You lose. Dealer had {deal_start_val}. Current balance: {balance}")
                done = True
        else:
            print("Invalid choice.")
    bet = 0
    print("")
    time.sleep(1)

blackjack()
