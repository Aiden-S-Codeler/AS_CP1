#AS 2nd Only Forward

import random

print("placeholder")
print(input("press enter to start "))

money = 0

has_coolsword = False
has_redam = False
has_bomb = True
has_wararmor = False
has_warstick = False

has_bhstaff = False
has_blueam = False
has_book = False
has_schocloak = False
has_schostick = False

has_sax = False
has_greenam = False
has_drums = False
has_piccolo = False
has_sunglasses = False

gob_friend = False
frog_friend = False
dog_friend = False

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

stats = [stat_1, stat_2, stat_3, stat_4]

while True:
    class_choose = input("What class would you like (warrior, scholar, or bard)? ")
    if class_choose == "warrior":
        uclass = "warrior"
        health = 60
        ac = 17
    elif class_choose == "scholar":
        uclass = "scholar"
        health = 40
        ac = 13
    elif class_choose == "bard":
        uclass = "bard"
        health = 50
        ac = 15
    else:
        continue
    break

strength = 0
constitution = 0
inteligence = 0
charisma = 0

print(stats)
while True:
    while strength == 0:
        what_stat = input("Which of your stats do you want to be your strength? ")
        if what_stat.isdigit():
            what_stat = int(what_stat)
        else:
            print("That is not a digit.")
            continue
        if what_stat in stats:
            strength = what_stat
            stats.remove(what_stat)
        else:
            print("That number is not available.")
            continue
    print(f"remaining stats are: {stats}")
    while constitution == 0:
        what_stat = input("Which of your stats do you want to be your constitution? ")
        if what_stat.isdigit():
            what_stat = int(what_stat)
        else:
            print("That is not a digit.")
            continue
        if what_stat in stats:
            constitution = what_stat
            stats.remove(what_stat)
        else:
            print("That number is not available.")
            continue
    print(f"remaining stats are: {stats}")
    while inteligence == 0:
        what_stat = input("Which of your stats do you want to be your inteligence? ")
        if what_stat.isdigit():
            what_stat = int(what_stat)
        else:
            print("That is not a digit.")
            continue
        if what_stat in stats:
            inteligence = what_stat
            stats.remove(what_stat)
        else:
            print("That number is not available.")
            continue
    print(f"remaining stats are: {stats}")
    while charisma == 0:
        what_stat = input("Which of your stats do you want to be your charisma? ")
        if what_stat.isdigit():
            what_stat = int(what_stat)
        else:
            print("That is not a digit.")
            continue
        if what_stat in stats:
            charisma = what_stat
            stats.remove(what_stat)
        else:
            print("That number is not available.")
            continue
    break

def firepath(uclass, health, ac, money, strength, constitution, inteligence, charisma, has_coolsword, gob_friend, has_redam, has_bomb, has_wararmor, has_warstick, has_bhstaff, has_blueam, has_book, has_schocloak, has_schostick, has_sax, has_greenam, has_drums, has_piccolo, has_sunglasses):
    print(input("You chose the fire path.\nThe moment you enter, you feel the heat of the magma flowing down the cave walls radiating onto you.\nYou also see three chests. "))
    visitchest1 = False
    visitchest3 = False
    while True:
        whatchest = input("What chest do you choose: 1, 2, or 3? ")
        if whatchest == "1" or whatchest == "2" or whatchest == "3":
            if whatchest == "1":
                if visitchest1 == False:
                    has_coolsword = True
                    print(input("Congrats! You have picked up the Really Cool Sword! "))
                    visitchest1 = True
                else:
                    print("You have already checked here.")
            elif whatchest == "2":
                print(input("KABOOM!!! The chest explodes, destroying the other two chests in the process.\n You leave for the next area. "))
                break
            elif whatchest == "3":
                if visitchest3 == False:
                    has_coolsword = True
                    print(input("Congrats! You have picked up $10! "))
                    visitchest3 = True
                else:
                    print("You have already checked here.")
        else:
            print("Invalid choice.")
            continue
    
    print(input("You enter the next cavern and here a skuttering sound from above you. As you look up, you see a green creature leap down from the ceiling at you.\nAs you leap back to dodge, you can tell the the creature is a goblingo. "))
    ghealth = 40
    if uclass == "warrior":
        print("You start first.")
        atkboost = 0
        while True:
            action = input("Would you like to stab, rage, bomb, bludgeon, or befriend? ")
            if action == "befriend":
                roll = random.randint(1, 20) + (charisma/2)
                if roll >= 18:
                    gob_friend = True
                    print(input("You have befriended the goblingo! You win the fight. "))
                    break
                else:
                    print("You failed to befriend the goblingo. :( ")
            elif action == "stab":
                roll = random.randint(1, 20) + 3
                if roll >= 14:
                    if has_coolsword == True:
                        if roll == 23:
                            dmg_roll = (random.randint(5, 15) + 5 + atkboost + (strength / 2)) * 2
                            if has_redam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_blueam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_greenam == True:
                                dmg_roll += 5
                            else:
                                pass
                            ghealth -= dmg_roll
                            print(f"CRIT!!! You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                        else:
                            dmg_roll = random.randint(5, 15) + 5 + atkboost + (strength / 2)
                            if has_redam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_blueam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_greenam == True:
                                dmg_roll += 5
                            ghealth -= dmg_roll
                            print(f"You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                    else:
                        if roll == 23:
                            dmg_roll = (random.randint(5, 15) + atkboost + (strength / 2)) * 2
                            if has_redam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_blueam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_greenam == True:
                                dmg_roll += 5
                            ghealth -= dmg_roll
                            print(f"CRIT!!! You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                        else:
                            dmg_roll = random.randint(5, 15) + atkboost + (strength / 2)
                            if has_redam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_blueam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_greenam == True:
                                dmg_roll += 5
                            ghealth -= dmg_roll
                            print(f"You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                    atkboost = 0
                else:
                    print("You missed.")
            elif action == "rage":
                print("Yeah get angry. ;b   Your next attack will do 3 more damage.")
                atkboost += 3
            elif action == "bomb":
                if has_bomb == True:
                    dmg_roll = random.randint(10, 20) + 5 + (strength / 2)
                    if has_redam == True:
                        dmg_roll += 5
                    else:
                        pass
                    if has_blueam == True:
                        dmg_roll += 5
                    else:
                        pass
                    if has_greenam == True:
                            dmg_roll += 5
                    ghealth -= dmg_roll
                    print(f"You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                else:
                    print("You dont have access to this attack yet.\nYou will unlock this in a shop at the end of the fire path is you decide to got there and purchase it. ")
                    continue
            elif action == "bludgeon":
                if has_warstick == True:
                    dmg_roll = random.randint(1, 75) + 5 + atkboost + (strength / 2)
                    if has_redam == True:
                        dmg_roll += 5
                    else:
                        pass
                    if has_blueam == True:
                        dmg_roll += 5
                    else:
                        pass
                    if has_greenam == True:
                            dmg_roll += 5
                    ghealth -= dmg_roll
                    print(f"You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                else:
                    print("You dont have access to this attack yet.\nYou will unlock this in a shop at the end of the fire path is you decide to got there and purchase it. ")
                    continue
            else:
                print("invalid option")
                continue
            if ghealth < 1:
                print(input("You win the fight. "))
                has_redam = True
                break
            else:
                print(input("Goblins turn. "))
            if random.randint(1, 20) >= ac:
                gobdmg = random.randint(5, 10)
                health -= gobdmg
                print(f"Goblingo did {gobdmg} damage. Current health: {health}. ")
            else:
                print("Gob missed")
            if health < 1:
                print(input("You lose. Press enter to restart fight."))
                health = 60
                ghealth = 40
                atkboost = 0
                continue
            else:
                print(input("Your turn. "))
    elif uclass == "scholar":
        print("You start first.")
        atkboost = 0
        while True:
            action = input("Would you like to use thunder, study, fireball, blackhole, or befriend? ")
            if action == "befriend":
                roll = random.randint(1, 20) + (charisma/2)
                if roll >= 18:
                    gob_friend = True
                    print(input("You have befriended the goblingo! You win the fight. "))
                    break
                else:
                    print("You failed to befriend the goblingo. :( ")
            elif action == "thunder":
                roll = random.randint(1, 20) + 3
                if roll >= 14:
                    if has_schostick == True:
                        if roll == 23:
                            dmg_roll = random.randint(15, 30) + 5 + atkboost + (inteligence / 2)
                            if has_redam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_blueam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_greenam == True:
                                dmg_roll += 5
                            else:
                                pass
                            ghealth -= dmg_roll
                            print(f"CRIT!!! You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                            roll2 = random.randint(1, 20) + 3
                            if roll2 == 23:
                                dmg_roll = random.randint(15, 30) + 5 + atkboost + (inteligence / 2)
                                if has_redam == True:
                                    dmg_roll += 5
                                else:
                                    pass
                                if has_blueam == True:
                                    dmg_roll += 5
                                else:
                                    pass
                                if has_greenam == True:
                                    dmg_roll += 5
                                else:
                                    pass
                                ghealth -= dmg_roll
                                print(f"CRIT!!! You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                            else:
                                dmg_roll = (random.randint(15, 30) + 5 + atkboost + (inteligence / 2)) / 2
                                if has_redam == True:
                                    dmg_roll += 5
                                else:
                                    pass
                                if has_blueam == True:
                                    dmg_roll += 5
                                else:
                                    pass
                                if has_greenam == True:
                                    dmg_roll += 5
                                ghealth -= dmg_roll
                                print(f"You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                        else:
                            dmg_roll = (random.randint(15, 30) + 5 + atkboost + (inteligence / 2)) / 2
                            if has_redam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_blueam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_greenam == True:
                                dmg_roll += 5
                            ghealth -= dmg_roll
                            print(f"You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                            roll2 = random.randint(1, 20) + 3
                            if roll2 == 23:
                                dmg_roll = random.randint(15, 30) + 5 + atkboost + (inteligence / 2)
                                if has_redam == True:
                                    dmg_roll += 5
                                else:
                                    pass
                                if has_blueam == True:
                                    dmg_roll += 5
                                else:
                                    pass
                                if has_greenam == True:
                                    dmg_roll += 5
                                else:
                                    pass
                                ghealth -= dmg_roll
                                print(f"CRIT!!! You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                            else:
                                dmg_roll = (random.randint(15, 30) + 5 + atkboost + (inteligence / 2)) / 2
                                if has_redam == True:
                                    dmg_roll += 5
                                else:
                                    pass
                                if has_blueam == True:
                                    dmg_roll += 5
                                else:
                                    pass
                                if has_greenam == True:
                                    dmg_roll += 5
                                ghealth -= dmg_roll
                                print(f"Cool stick triggered a second attack. You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                    else:
                        if roll == 23:
                            dmg_roll = (random.randint(15, 30) + atkboost + (inteligence / 2)) * 2
                            if has_redam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_blueam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_greenam == True:
                                dmg_roll += 5
                            ghealth -= dmg_roll
                            print(f"CRIT!!! You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                        else:
                            dmg_roll = random.randint(15, 30) + atkboost + (inteligence / 2)
                            if has_redam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_blueam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_greenam == True:
                                dmg_roll += 5
                            ghealth -= dmg_roll
                            print(f"You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                    atkboost = 0
                else:
                    print("You missed.")
            elif action == "study":
                print("Yeah get smart. ;b   Your next attack will do 3 more damage.")
                atkboost += 3
            elif action == "fireball":
                if has_book == True:
                    if has_schostick == True:
                        dmg_roll = (random.randint(10, 20) + 5 + (inteligence / 2)) * 2
                        if has_redam == True:
                            dmg_roll += 5
                        else:
                            pass
                        if has_blueam == True:
                            dmg_roll += 5
                        else:
                            pass
                        if has_greenam == True:
                            dmg_roll += 5
                        else:
                            pass
                        ghealth -= dmg_roll
                        print(f"You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                        dmg_roll = (random.randint(10, 20) + 5 + (inteligence / 2)) * 2
                        if has_redam == True:
                            dmg_roll += 5
                        else:
                            pass
                        if has_blueam == True:
                            dmg_roll += 5
                        else:
                            pass
                        if has_greenam == True:
                            dmg_roll += 5
                        else:
                            pass
                        ghealth -= dmg_roll
                        print(f"Cool stick triggered a second attack. You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                    else:
                        dmg_roll = random.randint(20, 40) + 5 + (inteligence / 2)
                        if has_redam == True:
                            dmg_roll += 5
                        else:
                            pass
                        if has_blueam == True:
                            dmg_roll += 5
                        else:
                            pass
                        if has_greenam == True:
                                dmg_roll += 5
                        ghealth -= dmg_roll
                        print(f"You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                else:
                    print("You dont have access to this attack yet.\nYou will unlock this in a shop at the end of the water path is you decide to go there and purchase it. ")
                    continue
            elif action == "black hole":
                if has_bhstaff == True:
                    dmg_roll = random.randint(1, 100) + 5 + atkboost + (inteligence/ 2)
                    if has_redam == True:
                        dmg_roll += 5
                    else:
                        pass
                    if has_blueam == True:
                        dmg_roll += 5
                    else:
                        pass
                    if has_greenam == True:
                            dmg_roll += 5
                    ghealth -= dmg_roll
                    print(f"You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                else:
                    print("You dont have access to this attack yet.\nYou will unlock this in a chest at the beginning of the water path is you decide to go there and pick it up. ")
                    continue
            else:
                print("invalid option")
                continue
            if ghealth < 1:
                print(input("You win the fight. "))
                has_redam = True
                break
            else:
                print(input("Goblins turn. "))
            if random.randint(1, 20) >= ac:
                gobdmg = random.randint(5, 10)
                health -= gobdmg
                print(f"Goblingo did {gobdmg} damage. Current health: {health}. ")
            else:
                print("Gob missed")
            if health < 1:
                print(input("You lose. Press enter to restart fight."))
                health = 40
                ghealth = 40
                atkboost = 0
                continue
            else:
                print(input("Your turn. "))
    if uclass == "bard":
        print("You start first.")
        atkboost = 0
        while True:
            action = input("Would you like to song, powersong, screech, boom, or befriend? ")
            if action == "befriend":
                roll = random.randint(1, 20) + (charisma/2)
                if roll >= 18:
                    gob_friend = True
                    print(input("You have befriended the goblingo! You win the fight. "))
                    break
                else:
                    print("You failed to befriend the goblingo. :( ")
            elif action == "song":
                roll = random.randint(1, 20) + 3
                if roll >= 14:
                    if has_sax == True:
                        if roll == 23:
                            dmg_roll = (random.randint(10, 20) + 5 + atkboost + (charisma / 2)) * 2
                            if has_redam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_blueam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_greenam == True:
                                dmg_roll += 5
                            else:
                                pass
                            ghealth -= dmg_roll
                            print(f"CRIT!!! You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                        else:
                            dmg_roll = random.randint(10, 20) + 5 + atkboost + (charisma / 2)
                            if has_redam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_blueam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_greenam == True:
                                dmg_roll += 5
                            ghealth -= dmg_roll
                            print(f"You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                    else:
                        if roll == 23:
                            dmg_roll = (random.randint(10, 20) + atkboost + (charisma / 2)) * 2
                            if has_redam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_blueam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_greenam == True:
                                dmg_roll += 5
                            ghealth -= dmg_roll
                            print(f"CRIT!!! You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                        else:
                            dmg_roll = random.randint(10, 20) + atkboost + (charisma / 2)
                            if has_redam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_blueam == True:
                                dmg_roll += 5
                            else:
                                pass
                            if has_greenam == True:
                                dmg_roll += 5
                            ghealth -= dmg_roll
                            print(f"You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                    atkboost = 0
                else:
                    print("You missed.")
            elif action == "powersong":
                print("Yeah get groovy. ;b   Your next attack will do 3 more damage.")
                atkboost += 3
            elif action == "screech":
                if has_piccolo == True:
                    dmg_roll = random.randint(1, 75) + 5 + (charisma / 2)
                    if has_redam == True:
                        dmg_roll += 5
                    else:
                        pass
                    if has_blueam == True:
                        dmg_roll += 5
                    else:
                        pass
                    if has_greenam == True:
                            dmg_roll += 5
                    ghealth -= dmg_roll
                    print(f"You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                else:
                    print("You dont have access to this attack yet.\nYou will unlock this in a shop at the end of the town path is you decide to got there and purchase it. ")
                    continue
            elif action == "boom":
                if has_drums == True:
                    dmg_roll = random.randint(10, 20) + 5 + atkboost + (charisma / 2)
                    if has_redam == True:
                        dmg_roll += 5
                    else:
                        pass
                    if has_blueam == True:
                        dmg_roll += 5
                    else:
                        pass
                    if has_greenam == True:
                            dmg_roll += 5
                    ghealth -= dmg_roll
                    print(f"You did {dmg_roll} damage. Goblin has {ghealth} health left. ")
                else:
                    print("You dont have access to this attack yet.\nYou will unlock this in a shop at the end of the town path is you decide to got there and purchase it. ")
                    continue
            else:
                print("invalid option")
                continue
            if ghealth < 1:
                print(input("You win the fight. "))
                has_redam = True
                break
            else:
                print(input("Goblins turn. "))
            if random.randint(1, 20) >= ac:
                gobdmg = random.randint(5, 10)
                health -= gobdmg
                print(f"Goblingo did {gobdmg} damage. Current health: {health}. ")
            else:
                print("Gob missed")
            if health < 1:
                print(input("You lose. Press enter to restart fight."))
                health = 50
                ghealth = 40
                atkboost = 0
                continue
            else:
                print(input("Your turn. "))
    if gob_friend == True:
        print(input("Now that you have befriended the Goblingo, it will help you fight the final boss. "))
    else:
        print(input("Now that you have defeated the goblin, you have picked up the Goblingos red amulet. You feel power flowing through you. "))
    
    print(input("As you move on from the grueling fight, you notice a shop in the distance. "))