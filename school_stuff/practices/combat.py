#AS 2nd combet simulator
import random

import random
stat_1 = [int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6))]
stat_1.remove(min(stat_1))
stat_1 = sum(stat_1)
stat_2 = [int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6))]
stat_2.remove(min(stat_2))
stat_2 = sum(stat_2)
stat_3 = [int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6))]
stat_3.remove(min(stat_3))
stat_3 = sum(stat_3)
stat_4 = [int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6))]
stat_4.remove(min(stat_4))
stat_4 = sum(stat_4)
stat_5 = [int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6))]
stat_5.remove(min(stat_5))
stat_5 = sum(stat_5)
stat_6 = [int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6))]
stat_6.remove(min(stat_6))
stat_6 = sum(stat_6)
print(f"Your stats are: {stat_1}, {stat_2}, {stat_3}, {stat_4}, {stat_5}, {stat_6}")


class_chosen = "Bard"
print(f"Your class is: {class_chosen}")

stat_list = [stat_1, stat_2, stat_3, stat_4, stat_5, stat_6]
stren = 0
dex = 0
con = 0
intel = 0
wis = 0
char = 0
while stren == 0:
    what_stren = input("Which of your stats do you want to be your strength? ")
    if what_stren.isdigit():
        what_stren = int(what_stren)
    else:
        print("Setting strength to 5 for trolling.")
        stren = 5
    if what_stren in stat_list:
        stren = what_stren
        stat_list.remove(what_stren)
    else:
        print("Setting strength to 5 for trolling.")
        stren = 5
print(f"remaining stats are: {stat_list}")
while dex == 0:
    what_dex = input("Which of your stats do you want to be your dexterity? ")
    if what_dex.isdigit():
        what_dex = int(what_dex)
    else:
        print("Setting dexterity to 5 for trolling.")
        dex = 5
    if what_dex in stat_list:
        dex = what_dex
        stat_list.remove(what_dex)
    else:
        print("Setting dexterity to 5 for trolling.")
        dex = 5
print(f"remaining stats are: {stat_list}")
while con == 0:
    what_con = input("Which of your stats do you want to be your constitution? ")
    if what_con.isdigit():
        what_con = int(what_con)
    else:
        print("Setting constitution to 5 for trolling.")
        con = 5
    if what_con in stat_list:
        con = what_con
        stat_list.remove(what_con)
    else:
        print("Setting constitution to 5 for trolling.")
        con = 5
print(f"remaining stats are: {stat_list}")
while intel == 0:
    what_intel = input("Which of your stats do you want to be your inteligence? ")
    if what_intel.isdigit():
        what_intel = int(what_intel)
    else:
        print("Setting inteligence to 5 for trolling.")
        intel = 5
    if what_intel in stat_list:
        intel = what_intel
        stat_list.remove(what_intel)
    else:
        print("Setting inteligence to 5 for trolling.")
        intel = 5
print(f"remaining stats are: {stat_list}")
while wis == 0:
    what_wis = input("Which of your stats do you want to be your wisdom? ")
    if what_wis.isdigit():
        what_wis = int(what_wis)
    else:
        print("Setting wisdom to 5 for trolling.")
        wis = 5
    if what_wis in stat_list:
        wis = what_wis
        stat_list.remove(what_wis)
    else:
        print("Setting wisdom to 5 for trolling.")
        wis = 5
print(f"remaining stats are: {stat_list}")
while char == 0:
    what_char = input("Which of your stats do you want to be your charisma? ")
    if what_char.isdigit():
        what_char = int(what_char)
    else:
        print("Setting charisma to 5 for trolling.")
        char = 5
    if what_char in stat_list:
        char = what_char
        stat_list.remove(what_char)
    else:
        print("Setting charisma to 5 for trolling.")
        char = 5

lvl = 3
health = 0
d12_hlist = ["Barbarian"]
d10_hlist = ["Fighter", "Pladin", "Ranger"]
d8_hlist = ["Artificer", "Bard", "Cleric", "Druid", "Monk", "Rogue", "Warlock"]
d6_hlist = ["Sorceror", "Wizard"]
if class_chosen in d12_hlist:
    health = 12
    for i in range(lvl - 1):
        health = health + random.randint(1, 12)
elif class_chosen in d10_hlist:
    health = 10
    for i in range(lvl - 1):
        health = health + random.randint(1, 10)
elif class_chosen in d8_hlist:
    health = 8
    for i in range(lvl - 1):
        health = health + random.randint(1, 8)
elif class_chosen in d6_hlist:
    health = 6
    for i in range(lvl - 1):
        health = health + random.randint(1, 6)
else:
    pass
print(f"Your total health at your level is {health}")

bear_h = random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10) + 12
bear_ac = 11

player_ac = 10 + dex - 10

def bear_turn(health):
    decide = random.randint(1, 3)
    if decide == 1:
        print("Bear used: claw")
        dice_roll = random.randint(1, 20) + 5
        if dice_roll >= player_ac:
            health -= random.randint(1, 8) + 4
        else:
            print("bear missed")
    elif decide == 2:
        print("Bear used: bite")
        dice_roll = random.randint(1, 20) + 5
        if dice_roll >= player_ac:
            health -= random.randint(1, 6) + random.randint(1, 6) + 4
        else:
            print("bear missed")
    elif decide == 3:
        print("Bear used: mual")
        dice_roll = random.randint(1, 20) + 5
        if dice_roll >= player_ac:
            health -= random.randint(1, 6) + random.randint(1, 6) + 4
        else:
            print("bear missed")
            dice_roll = random.randint(1, 20) + 5
        if dice_roll >= player_ac:
            health -= random.randint(1, 8) + 4
        else:
            print("bear missed")
    else:
        print("Something broke. My bad")
    return(health)

atk_boost = 0

def player_turn(health, bear_h, player_ac, atk_boost):
    while True:
        decide = input("What action would you like to take? 1: Attack Boost, 2: Defense Boost, 3: Healing, 4: Attack Spell. (Please choose the number value of you choice) ")
        if decide == "1":
            atk_boost += 2
            print(f"Current boost to attacks: {atk_boost}")
            break
        elif decide == "2":
            player_ac += 2
            print(f"Current defence: {player_ac}")
            break
        elif decide == "3":
            health += random.randint(1, 12)
            print(f"Current Health: {health}")
            break
        elif decide == "4":
            dice_roll = random.randint(1, 20) + (10 + (char - 10))
            if dice_roll >= bear_ac:
                bear_h -= random.randint(1, 12) + (10 + (char - 10))
            else:
                print("you missed")
            break
        else:
            print("bad")
            continue
    return(health, bear_h, player_ac, atk_boost)

print("You, John Bard, a world renowned bard, are walking through a forest. You sit down on a mossy rock\nto practice your music, when suddenly, a brown bear jumps out of the bushes to attack you.\n")
while True:
    print("Deciding who goes first...")
    bear_roll = random.randint(1, 20)
    player_roll =  random.randint(1, 20)
    if bear_roll == player_roll:
        print("You and Bear rolled the same. Rolling competitive.")
        continue
    elif bear_roll > player_roll:
        print("Bear rolled highest. It goes first.")
        while True:
            health = bear_turn(health)
            if health <= 0:
                print("Bear wins.")
                break
            else:
                pass
            print(f"current player health: {health}")
            health, bear_h, atk_boost, player_ac = player_turn(health, bear_h, atk_boost, player_ac)
            if bear_h <= 0:
                print("You win!")
                break
            else:
                pass
            print(f"current bear health: {bear_h}")
    else:
        print("You rolled highest. You go first.")
        while True:
            health, bear_h, atk_boost, player_ac = player_turn(health, bear_h, atk_boost, player_ac)
            if bear_h <= 0:
                print("You wins!")
                break
            else:
                pass
            print(f"current bear health: {bear_h}")
            health = bear_turn(health)
            if health <= 0:
                print("Bear wins.")
                break
            else:
                pass
            print(f"current player health: {health}")
    break