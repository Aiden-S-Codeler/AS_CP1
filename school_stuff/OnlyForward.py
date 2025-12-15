#AS 2nd Only Forward

import random                                                                        

print("      .i1;.    ..     :  .,   .,     .,                                    ")
print("    L8,   :@i  G@L    @. ;0    C8   :@,                                    ")
print("   t8       @: Gi.@.  @. ;0     :@.10                                      ")
print("   t8      .@: Gi  0G.@. ;0      .@L                                       ")
print("    G@.   .@i  Gi   ,@@. ;0       @;                                       ")
print("     .,;i;.    ,.     ;. .;;;;;:  :.                                       ")
print("     ,.                                                                    ")
print("    f,     i@@@@@@i  .C@@@G.   t@@@0,.0,  .L,   L:  1L    ;@@@8;  f@@@0i   ")
print("   :@.    .@.      :@,    .@1 .@.  :@.8,  8G,  01 .01@.  .@:  .@..@.   1@. ")
print("  .G@.    i@GGGC  i@       0t 1C..i@, G:.0.L:.0: .@,.@,  ,@..:@; Lf    .@. ")
print("  .@@.    @:      LC      t@  @, C0   Ci@, fi@:.t@;;;L8  @i i@   @.   .8:  ")
print("  .@@C   i0       .@8:.:0@,  L0  .@t  f@.  f@. @t    ,@ ;@   G0 GG,,f@L.   ")
print("  .8@@;                                                                    ")
print("   1@@@1                                                                   ")
print("   .8@@@8.             i,.                                                 ")
print("     t@@@@@G.          .@@@@@@0i.                                          ")
print("      ,@@@@@@@@8;,......C@@@@@@@@@@@L                                      ")
print("        t@@@@@@@@@@@@@@@@@@@@@@@@@@.                                       ")
print("          ,8@@@@@@@@@@@@@@@@@@@@@:                                         ")
print("             .i8@@@@@@@@@@@@@@@t                                           ")
print("                          ,@@0.                                            ")
print("                           0,                                              ")

print(input("press enter to start "))

money = 0

has_coolsword = False
has_redam = False
has_bomb = False
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
                    money += 10
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
            elif action == "blackhole":
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
        print(input("Now that you have defeated the goblingo, you have picked up the Goblingos red amulet. You feel power flowing through you. "))
    
    print(input("As you move on from the grueling fight, you notice a shop in the distance. "))
    while True:
        choice = input("What would you like to do: buy, rob, persuade, or leave. ")
        if choice == "buy":
            while True:
                buy_choice = input("Would you like to but the bomb for $5, the armor for $5, or the stick for $10? ")
                if buy_choice == "bomb":
                    if money >= 5:
                        has_bomb = True
                        money -= 5
                        print(f"You purchased the bomb. You have ${money} left.")
                        break
                    else:
                        print("Sorry but your to poor.")
                        break
                elif buy_choice == "armor":
                    if money >= 5:
                        has_wararmor = True
                        money -= 5
                        ac += 4
                        print(f"You purchased the armor. You have ${money} left.")
                        break
                    else:
                        print("Sorry but your to poor.")
                        break
                elif buy_choice == "stick":
                    if money >= 10:
                        has_warstick = True
                        money -= 10
                        print(f"You purchased the Stick. You have ${money} left.")
                        break
                    else:
                        print("Sorry but your to poor.")
                        break
                else:
                    print("Thats not a valid option. Did you only type the name fo the item?")
                    break
        elif choice == "rob":
            robroll = random.randint(1, 20)
            if robroll >= 16:
                if has_wararmor == False:
                    has_wararmor == True
                    ac += 4
                    print("You succesfuly run off with some shiny new armor.")
                    break
                elif has_warstick == False:
                    has_warstick == True
                    print("You run off with the really cool stick.")
                    break
                elif has_bomb == False:
                    has_bomb == True
                    print("You ran off with some explosives. Nice!!!")
                    break
                else:
                    print("You already have everything, so you tried to take the shopkeeper himself and failed.")
                    break
            else:
                print("You dont manage to snatch anything.")
                break
        elif choice == "persuade":
            giftroll = random.randint(1, 20) + (charisma / 2)
            if giftroll >= 16:
                if has_wararmor == False:
                    has_wararmor = True
                    ac += 4
                    print("You were gifted with some shiny new armor.")
                elif has_warstick == False:
                    has_warstick = True
                    print("You were gifted with the really cool stick.")
                elif has_bomb == False:
                    has_bomb = True
                    print("You were gifted some explosives. Nice!!!")
                else:
                    print("You already have everything.")
            else:
                print("You dont manage to get anything.")
        elif choice == "leave":
            print("You decide to leave the shop.")
            break
        else:
            print("Invalid choice.")
            continue
    return(uclass, health, ac, money, strength, constitution, inteligence, charisma, has_coolsword, gob_friend, has_redam, has_bomb, has_wararmor, has_warstick, has_bhstaff, has_blueam, has_book, has_schocloak, has_schostick, has_sax, has_greenam, has_drums, has_piccolo, has_sunglasses)

def waterpath(uclass, health, ac, money, strength, constitution, inteligence, charisma, has_coolsword, frog_friend, has_redam, has_bomb, has_wararmor, has_warstick, has_bhstaff, has_blueam, has_book, has_schocloak, has_schostick, has_sax, has_greenam, has_drums, has_piccolo, has_sunglasses):
    print(input("You chose the water path.\nThe moment you enter, you hear the sound of the ponds rippling.\nYou also see three chests. "))
    visitchest1 = False
    visitchest3 = False
    while True:
        whatchest = input("What chest do you choose: 1, 2, or 3? ")
        if whatchest == "1" or whatchest == "2" or whatchest == "3":
            if whatchest == "1":
                if visitchest1 == False:
                    has_bhstaff = True
                    print(input("Congrats! You have picked up the Dark Staff! "))
                    visitchest1 = True
                else:
                    print("You have already checked here.")
            elif whatchest == "2":
                print(input("KABOOM!!! The chest explodes, destroying the other two chests in the process.\n You leave for the next area. "))
                break
            elif whatchest == "3":
                if visitchest3 == False:
                    money += 10
                    print(input("Congrats! You have picked up $10! "))
                    visitchest3 = True
                else:
                    print("You have already checked here.")
        else:
            print("Invalid choice.")
            continue
    
    print(input("You enter the next grove and here a splashing sound from the right. As you look, you see a yellow creature leap out from the pond at you.\nAs you leap back to dodge, you can tell the the creature is a frog. "))
    ghealth = 50
    if uclass == "warrior":
        print("You start first.")
        atkboost = 0
        while True:
            action = input("Would you like to stab, rage, bomb, bludgeon, or befriend? ")
            if action == "befriend":
                roll = random.randint(1, 20) + (strength/2)
                if roll >= 18:
                    frog_friend = True
                    print(input("You have befriended the frog! You win the fight. "))
                    break
                else:
                    print("You failed to befriend the frog. :( ")
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
                            print(f"CRIT!!! You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                            print(f"You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                            print(f"CRIT!!! You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                            print(f"You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                    print(f"You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                    print(f"You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                print(input("Frogs turn. "))
            if random.randint(1, 20) >= ac:
                gobdmg = random.randint(10, 15)
                health -= gobdmg
                print(f"Frog did {gobdmg} damage. Current health: {health}. ")
            else:
                print("Frog missed")
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
                roll = random.randint(1, 20) + (strength/2)
                if roll >= 18:
                    frog_friend = True
                    print(input("You have befriended the frog! You win the fight. "))
                    break
                else:
                    print("You failed to befriend the frog. :( ")
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
                            print(f"CRIT!!! You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                                print(f"CRIT!!! You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                                print(f"You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                            print(f"You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                                print(f"CRIT!!! You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                                print(f"Cool stick triggered a second attack. You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                            print(f"CRIT!!! You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                            print(f"You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                        print(f"You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                        print(f"Cool stick triggered a second attack. You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                        print(f"You did {dmg_roll} damage. frog has {ghealth} health left. ")
                else:
                    print("You dont have access to this attack yet.\nYou will unlock this in a shop at the end of the water path is you decide to go there and purchase it. ")
                    continue
            elif action == "blackhole":
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
                    print(f"You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                print(input("frog turn. "))
            if random.randint(1, 20) >= ac:
                gobdmg = random.randint(5, 10)
                health -= gobdmg
                print(f"frog did {gobdmg} damage. Current health: {health}. ")
            else:
                print("frog missed")
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
                roll = random.randint(1, 20) + (strength/2)
                if roll >= 18:
                    frog_friend = True
                    print(input("You have befriended the frog! You win the fight. "))
                    break
                else:
                    print("You failed to befriend the frog. :( ")
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
                            print(f"CRIT!!! You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                            print(f"You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                            print(f"CRIT!!! You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                            print(f"You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                    print(f"You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                    print(f"You did {dmg_roll} damage. frog has {ghealth} health left. ")
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
                print(input("frog turn. "))
            if random.randint(1, 20) >= ac:
                gobdmg = random.randint(5, 10)
                health -= gobdmg
                print(f"frog did {gobdmg} damage. Current health: {health}. ")
            else:
                print("frog missed")
            if health < 1:
                print(input("You lose. Press enter to restart fight."))
                health = 50
                ghealth = 40
                atkboost = 0
                continue
            else:
                print(input("Your turn. "))
    if frog_friend == True:
        print(input("Now that you have befriended the frog, it will help you fight the final boss. "))
    else:
        print(input("Now that you have defeated the frog, you have picked up the frog blue amulet. You feel power flowing through you. "))
        has_blueam = True
    
    print(input("As you move on from the grueling fight, you notice a shop in the distance. "))
    while True:
        choice = input("What would you like to do: buy, rob, persuade, or leave. ")
        if choice == "buy":
            while True:
                buy_choice = input("Would you like to but the book for $5, the cloak for $5, or the stick for $10? ")
                if buy_choice == "book":
                    if money >= 5:
                        has_book = True
                        money -= 5
                        print(f"You purchased the book. You have ${money} left.")
                        break
                    else:
                        print("Sorry but your to poor.")
                        break
                elif buy_choice == "cloak":
                    if money >= 5:
                        has_schocloak = True
                        money -= 5
                        inteligence += 4
                        print(f"You purchased the cloak. You have ${money} left.")
                        break
                    else:
                        print("Sorry but your to poor.")
                        break
                elif buy_choice == "stick":
                    if money >= 10:
                        has_schostick = True
                        money -= 10
                        print(f"You purchased the Stick. You have ${money} left.")
                        break
                    else:
                        print("Sorry but your to poor.")
                        break
                else:
                    print("Thats not a valid option. Did you only type the name fo the item?")
                    break
        elif choice == "rob":
            robroll = random.randint(1, 20)
            if robroll >= 16:
                if has_schocloak == False:
                    has_schocloak == True
                    ac += 4
                    print("You succesfuly run off with the cloak.")
                    break
                elif has_schostick == False:
                    has_schostick == True
                    print("You run off with the really cool stick.")
                    break
                elif has_book == False:
                    has_book == True
                    print("You ran off with the book.")
                    break
                else:
                    print("You already have everything, so you tried to take the shopkeeper himself and failed.")
                    break
            else:
                print("You dont manage to snatch anything.")
                break
        elif choice == "persuade":
            giftroll = random.randint(1, 20) + (charisma / 2)
            if giftroll >= 16:
                if has_schocloak == False:
                    has_schocloak = True
                    ac += 4
                    print("You were gifted with the cloak.")
                elif has_schostick == False:
                    has_schostick = True
                    print("You were gifted with the really cool stick.")
                elif has_book == False:
                    has_book = True
                    print("You were gifted the book.")
                else:
                    print("You already have everything.")
            else:
                print("You dont manage to get anything.")
        elif choice == "leave":
            print("You decide to leave the shop.")
            break
        else:
            print("Invalid choice.")
            continue
    return(uclass, health, ac, money, strength, constitution, inteligence, charisma, has_coolsword, frog_friend, has_redam, has_bomb, has_wararmor, has_warstick, has_bhstaff, has_blueam, has_book, has_schocloak, has_schostick, has_sax, has_greenam, has_drums, has_piccolo, has_sunglasses)

def townpath(uclass, health, ac, money, strength, constitution, inteligence, charisma, has_coolsword, dog_friend, has_redam, has_bomb, has_wararmor, has_warstick, has_bhstaff, has_blueam, has_book, has_schocloak, has_schostick, has_sax, has_greenam, has_drums, has_piccolo, has_sunglasses):
    print(input("You chose the town path.\nThe moment you enter, you hear the sound of foot traffic.\nYou also see a chest in the middle of your pathway. "))
    visitchest1 = False
    visitchest3 = False
    while True:
        whatchest = input("What chest do you choose: 1, 1, or 1? ")
        if whatchest == "1" or whatchest == "2":
            if whatchest == "1":
                if visitchest1 == False:
                    has_sax = True
                    money += 10
                    print(input("Congrats! You have picked up the saxaphone and $10!\n You leave for the next area. "))
                    visitchest1 = True
                    break
                else:
                    print("You have already checked here.")
            elif whatchest == "2":
                print(input("Thinking that there must be another chest nearby, you walk around for 30 minutes before giving up and coming back to the chest."))
                continue
        else:
            print("Invalid choice.")
            continue
    
    print(input("You enter the next street and here a panting sound from the right. As you look, you see a grey creature walk out from the alley towards you.\nAs you look down, you can tell the the creature is a dog. "))
    ghealth = 50
    if uclass == "warrior":
        print("You start first.")
        atkboost = 0
        while True:
            action = input("Would you like to stab, rage, bomb, bludgeon, or befriend? ")
            if action == "befriend":
                roll = random.randint(1, 20) + (inteligence/2)
                if roll >= 18:
                    dog_friend = True
                    print(input("You have befriended the dog! You win the fight. "))
                    break
                else:
                    print("You failed to befriend the dog. :( ")
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
                            print(f"CRIT!!! You did {dmg_roll} damage. Dog has {ghealth} health left. ")
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
                            print(f"You did {dmg_roll} damage. Dog has {ghealth} health left. ")
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
                            print(f"CRIT!!! You did {dmg_roll} damage. Dog has {ghealth} health left. ")
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
                            print(f"You did {dmg_roll} damage. Dog has {ghealth} health left. ")
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
                    print(f"You did {dmg_roll} damage. Dog has {ghealth} health left. ")
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
                    print(f"You did {dmg_roll} damage. Dog has {ghealth} health left. ")
                else:
                    print("You dont have access to this attack yet.\nYou will unlock this in a shop at the end of the fire path is you decide to got there and purchase it. ")
                    continue
            else:
                print("invalid option")
                continue
            if ghealth < 1:
                print(input("You win the fight. "))
                has_greenam = True
                break
            else:
                print(input("Dog turn. "))
            if random.randint(1, 20) >= ac:
                gobdmg = random.randint(10, 15)
                health -= gobdmg
                print(f"Dog did {gobdmg} damage. Current health: {health}. ")
            else:
                print("Dog missed")
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
                roll = random.randint(1, 20) + (inteligence/2)
                if roll >= 18:
                    dog_friend = True
                    print(input("You have befriended the Dog! You win the fight. "))
                    break
                else:
                    print("You failed to befriend the Dog. :( ")
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
                            print(f"CRIT!!! You did {dmg_roll} damage. Dog has {ghealth} health left. ")
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
                                print(f"CRIT!!! You did {dmg_roll} damage. Dog has {ghealth} health left. ")
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
                                print(f"You did {dmg_roll} damage. Dog has {ghealth} health left. ")
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
                            print(f"You did {dmg_roll} damage. Dog has {ghealth} health left. ")
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
                                print(f"CRIT!!! You did {dmg_roll} damage. Dog has {ghealth} health left. ")
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
                                print(f"Cool stick triggered a second attack. You did {dmg_roll} damage. Dog has {ghealth} health left. ")
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
                            print(f"CRIT!!! You did {dmg_roll} damage. Dog has {ghealth} health left. ")
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
                            print(f"You did {dmg_roll} damage. Dog has {ghealth} health left. ")
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
                        print(f"You did {dmg_roll} damage. Dog has {ghealth} health left. ")
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
                        print(f"Cool stick triggered a second attack. You did {dmg_roll} damage. Dog has {ghealth} health left. ")
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
                        print(f"You did {dmg_roll} damage. Dog has {ghealth} health left. ")
                else:
                    print("You dont have access to this attack yet.\nYou will unlock this in a shop at the end of the water path is you decide to go there and purchase it. ")
                    continue
            elif action == "blackhole":
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
                    print(f"You did {dmg_roll} damage. Dog has {ghealth} health left. ")
                else:
                    print("You dont have access to this attack yet.\nYou will unlock this in a chest at the beginning of the water path is you decide to go there and pick it up. ")
                    continue
            else:
                print("invalid option")
                continue
            if ghealth < 1:
                print(input("You win the fight. "))
                has_greenam = True
                break
            else:
                print(input("Dog turn. "))
            if random.randint(1, 20) >= ac:
                gobdmg = random.randint(5, 10)
                health -= gobdmg
                print(f"Dog did {gobdmg} damage. Current health: {health}. ")
            else:
                print("Dog missed")
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
                roll = random.randint(1, 20) + (inteligence/2)
                if roll >= 18:
                    dog_friend = True
                    print(input("You have befriended the Dog! You win the fight. "))
                    break
                else:
                    print("You failed to befriend the Dog. :( ")
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
                            print(f"CRIT!!! You did {dmg_roll} damage. Dog has {ghealth} health left. ")
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
                            print(f"You did {dmg_roll} damage. Dog has {ghealth} health left. ")
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
                            print(f"CRIT!!! You did {dmg_roll} damage. Dog has {ghealth} health left. ")
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
                            print(f"You did {dmg_roll} damage. Dog has {ghealth} health left. ")
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
                    print(f"You did {dmg_roll} damage. Dog has {ghealth} health left. ")
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
                    print(f"You did {dmg_roll} damage. Dog has {ghealth} health left. ")
                else:
                    print("You dont have access to this attack yet.\nYou will unlock this in a shop at the end of the town path is you decide to got there and purchase it. ")
                    continue
            else:
                print("invalid option")
                continue
            if ghealth < 1:
                print(input("You win the fight. "))
                has_greenam = True
                break
            else:
                print(input("Dog turn. "))
            if random.randint(1, 20) >= ac:
                gobdmg = random.randint(5, 10)
                health -= gobdmg
                print(f"Dog did {gobdmg} damage. Current health: {health}. ")
            else:
                print("Dog missed")
            if health < 1:
                print(input("You lose. Press enter to restart fight."))
                health = 50
                ghealth = 40
                atkboost = 0
                continue
            else:
                print(input("Your turn. "))
    if dog_friend == True:
        print(input("Now that you have befriended the Dog, it will help you fight the final boss. "))
    else:
        print(input("Now that you have defeated the Dog, you have picked up the Dogs green amulet. You feel power flowing through you, along with the guilt of murdering a puppy.\nYou have the aura of a dog murderer on you, so everyone likes you less now. "))
        has_greenam = True
        charisma -= 5
    
    print(input("As you move on from that experience, you notice a shop in the distance. "))
    while True:
        choice = input("What would you like to do: buy, rob, persuade, or leave. ")
        if choice == "buy":
            while True:
                buy_choice = input("Would you like to but the drums for $5, the sunglasses for $5, or the piccolo for $10? ")
                if buy_choice == "drums":
                    if money >= 5:
                        has_drums = True
                        money -= 5
                        print(f"You purchased the drums. You have ${money} left.")
                        break
                    else:
                        print("Sorry but your to poor.")
                        break
                elif buy_choice == "sunglasses":
                    if money >= 5:
                        has_sunglasses = True
                        money -= 5
                        charisma += 4
                        print(f"You purchased the sunglasses. You have ${money} left.")
                        break
                    else:
                        print("Sorry but your to poor.")
                        break
                elif buy_choice == "piccolo":
                    if money >= 10:
                        has_piccolo = True
                        money -= 10
                        print(f"You purchased the piccolo. You have ${money} left.")
                        break
                    else:
                        print("Sorry but your to poor.")
                        break
                else:
                    print("Thats not a valid option. Did you only type the name fo the item?")
                    break
        elif choice == "rob":
            robroll = random.randint(1, 20)
            if robroll >= 16:
                if has_sunglasses == False:
                    has_sunglasses == True
                    charisma += 4
                    print("You succesfuly run off with the sunglasses.")
                    break
                elif has_piccolo == False:
                    has_piccolo == True
                    print("You run off with the really piccolo.")
                    break
                elif has_drums == False:
                    has_drums == True
                    print("You ran off with the drums.")
                    break
                else:
                    print("You already have everything, so you tried to take the shopkeeper himself and failed.")
                    break
            else:
                print("You dont manage to snatch anything.")
                break
        elif choice == "persuade":
            giftroll = random.randint(1, 20) + (charisma / 2)
            if giftroll >= 16:
                if has_sunglasses == False:
                    has_sunglasses = True
                    charisma += 4
                    print("You were gifted with the sunglasses.")
                elif has_piccolo == False:
                    has_piccolo = True
                    print("You were gifted with the piccolo.")
                elif has_drums == False:
                    has_drums = True
                    print("You were gifted the drums.")
                else:
                    print("You already have everything.")
            else:
                print("You dont manage to get anything.")
        elif choice == "leave":
            print("You decide to leave the shop.")
            break
        else:
            print("Invalid choice.")
            continue
    return(uclass, health, ac, money, strength, constitution, inteligence, charisma, has_coolsword, dog_friend, has_redam, has_bomb, has_wararmor, has_warstick, has_bhstaff, has_blueam, has_book, has_schocloak, has_schostick, has_sax, has_greenam, has_drums, has_piccolo, has_sunglasses)

visitfire = False
visitwater = False
visittown = False

while True:
    while True:
        choose_path = input("What path would you like to take: fire, water, or town?")
        if choose_path == "fire":
            uclass, health, ac, money, strength, constitution, inteligence, charisma, has_coolsword, gob_friend, has_redam, has_bomb, has_wararmor, has_warstick, has_bhstaff, has_blueam, has_book, has_schocloak, has_schostick, has_sax, has_greenam, has_drums, has_piccolo, has_sunglasses = firepath(uclass, health, ac, money, strength, constitution, inteligence, charisma, has_coolsword, gob_friend, has_redam, has_bomb, has_wararmor, has_warstick, has_bhstaff, has_blueam, has_book, has_schocloak, has_schostick, has_sax, has_greenam, has_drums, has_piccolo, has_sunglasses)
            visitfire = True
            break
        elif choose_path == "water":
            uclass, health, ac, money, strength, constitution, inteligence, charisma, has_coolsword, frog_friend, has_redam, has_bomb, has_wararmor, has_warstick, has_bhstaff, has_blueam, has_book, has_schocloak, has_schostick, has_sax, has_greenam, has_drums, has_piccolo, has_sunglasses = waterpath(uclass, health, ac, money, strength, constitution, inteligence, charisma, has_coolsword, frog_friend, has_redam, has_bomb, has_wararmor, has_warstick, has_bhstaff, has_blueam, has_book, has_schocloak, has_schostick, has_sax, has_greenam, has_drums, has_piccolo, has_sunglasses)
            visitwater = True
            break
        elif choose_path == "town":
            uclass, health, ac, money, strength, constitution, inteligence, charisma, has_coolsword, dog_friend, has_redam, has_bomb, has_wararmor, has_warstick, has_bhstaff, has_blueam, has_book, has_schocloak, has_schostick, has_sax, has_greenam, has_drums, has_piccolo, has_sunglasses = townpath(uclass, health, ac, money, strength, constitution, inteligence, charisma, has_coolsword, dog_friend, has_redam, has_bomb, has_wararmor, has_warstick, has_bhstaff, has_blueam, has_book, has_schocloak, has_schostick, has_sax, has_greenam, has_drums, has_piccolo, has_sunglasses)
            visittown = True
            break
        else:
            print("Invalid choice.")
            continue
    while True:
        choose_path = input("Now that you have made it through that path, would you like to take: fire path, water path, town path, ot move onto the boss?")
        if choose_path == "fire" or choose_path == "fire path":
            if visitfire == False:
                uclass, health, ac, money, strength, constitution, inteligence, charisma, has_coolsword, gob_friend, has_redam, has_bomb, has_wararmor, has_warstick, has_bhstaff, has_blueam, has_book, has_schocloak, has_schostick, has_sax, has_greenam, has_drums, has_piccolo, has_sunglasses = firepath(uclass, health, ac, money, strength, constitution, inteligence, charisma, has_coolsword, gob_friend, has_redam, has_bomb, has_wararmor, has_warstick, has_bhstaff, has_blueam, has_book, has_schocloak, has_schostick, has_sax, has_greenam, has_drums, has_piccolo, has_sunglasses)
                visitfire = True
                continue
            else:
                print("You already did this path.")
        elif choose_path == "water" or choose_path == "water path":
            if visitwater == False:
                uclass, health, ac, money, strength, constitution, inteligence, charisma, has_coolsword, frog_friend, has_redam, has_bomb, has_wararmor, has_warstick, has_bhstaff, has_blueam, has_book, has_schocloak, has_schostick, has_sax, has_greenam, has_drums, has_piccolo, has_sunglasses = waterpath(uclass, health, ac, money, strength, constitution, inteligence, charisma, has_coolsword, frog_friend, has_redam, has_bomb, has_wararmor, has_warstick, has_bhstaff, has_blueam, has_book, has_schocloak, has_schostick, has_sax, has_greenam, has_drums, has_piccolo, has_sunglasses)
                visitwater = True
                continue
            else:
                print("You already did this path.")
        elif choose_path == "town" or choose_path == "town path":
            if visittown == False:
                uclass, health, ac, money, strength, constitution, inteligence, charisma, has_coolsword, dog_friend, has_redam, has_bomb, has_wararmor, has_warstick, has_bhstaff, has_blueam, has_book, has_schocloak, has_schostick, has_sax, has_greenam, has_drums, has_piccolo, has_sunglasses = townpath(uclass, health, ac, money, strength, constitution, inteligence, charisma, has_coolsword, dog_friend, has_redam, has_bomb, has_wararmor, has_warstick, has_bhstaff, has_blueam, has_book, has_schocloak, has_schostick, has_sax, has_greenam, has_drums, has_piccolo, has_sunglasses)
                visittown = True
                continue
            else:
                print("You already did this path.")
        elif choose_path == "boss":
            ghealth = 150
            if uclass == "warrior":
                print("You start first.")
                atkboost = 0
                while True:
                    action = input("Would you like to stab, rage, bomb, or bludgeon? ")
                    if action == "stab":
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
                                    print(f"CRIT!!! You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                                    print(f"You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                                    print(f"CRIT!!! You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                                    print(f"You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                            print(f"You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                            print(f"You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
                        else:
                            print("You dont have access to this attack yet.\nYou will unlock this in a shop at the end of the fire path is you decide to got there and purchase it. ")
                            continue
                    else:
                        print("invalid option")
                        continue
                    if gob_friend == True:
                        ghealth -= 10
                        print(f"Goblingo did 10 damage to Belphagor. Remaining health: {ghealth}")
                    else:
                        pass
                    if frog_friend == True:
                        ghealth -= 10
                        print(f"Frog did 10 damage to Belphagor. Remaining health: {ghealth}")
                    else:
                        pass
                    if dog_friend == True:
                        ghealth -= 10
                        print(f"Dog did 10 damage to Belphagor. Remaining health: {ghealth}")
                    else:
                        pass
                    if ghealth < 1:
                        print(input("You win the fight. "))
                    else:
                        print(input("Belphagor's turn. "))
                    bossatk = random.randint(1, 3)
                    if bossatk == 1:
                        bossbeam = random.randint(20, 30)
                        if has_redam == True and has_blueam == True and has_greenam == True:
                            bossbeam = bossbeam / 2
                            health -= bossbeam - (constitution / 2)
                            print(input(f"Due to the combined power of the 3 amulets, the beam from Belphagor did half the damage. You took {bossbeam} damage. You have {health} left. "))
                        else:
                            health -= bossbeam - (constitution / 2)
                            print(input(f"Belphagor used a beam attack. You took {bossbeam} damage. You have {health} left. "))
                    elif bossatk == 2:
                        bossbeam = random.randint(10, 40)
                        if has_redam == True and has_blueam == True and has_greenam == True:
                            bossbeam = bossbeam / 2
                            health -= bossbeam - (constitution / 2)
                            print(input(f"Due to the combined power of the 3 amulets, the punch from Belphagor did half the damage. You took {bossbeam} damage. You have {health} left. "))
                        else:
                            health -= bossbeam - (constitution / 2)
                            print(input(f"Belphagor used a punch attack. You took {bossbeam} damage. You have {health} left. "))
                    else:
                        bossbeam = random.randint(1, 20)
                        if has_redam == True and has_blueam == True and has_greenam == True:
                            bossbeam = bossbeam / 2
                            ghealth += bossbeam
                            print(input(f"Due to the combined power of the 3 amulets, Belphagor only healed half of what he would do normally. Belpahgor has {ghealth} health. "))
                        else:
                            ghealth += bossbeam
                            print(input(f"Belphagor healed {bossbeam}. Belpahgor has {ghealth} health. "))
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
                    if action == "thunder":
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
                                    print(f"CRIT!!! You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                                        print(f"CRIT!!! You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                                        print(f"You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                                    print(f"You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                                        print(f"CRIT!!! You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                                        print(f"Cool stick triggered a second attack. You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                                    print(f"CRIT!!! You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                                    print(f"You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                                print(f"You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                                print(f"Cool stick triggered a second attack. You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                                print(f"You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
                        else:
                            print("You dont have access to this attack yet.\nYou will unlock this in a shop at the end of the water path is you decide to go there and purchase it. ")
                            continue
                    elif action == "blackhole":
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
                            print(f"You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                        print(input("Belphagor's turn. "))
                    bossatk = random.randint(1, 3)
                    if bossatk == 1:
                        bossbeam = random.randint(20, 30)
                        if has_redam == True and has_blueam == True and has_greenam == True:
                            bossbeam = bossbeam / 2
                            health -= bossbeam - (constitution / 2)
                            print(input(f"Due to the combined power of the 3 amulets, the beam from Belphagor did half the damage. You took {bossbeam} damage. You have {health} left. "))
                        else:
                            health -= bossbeam - (constitution / 2)
                            print(input(f"Belphagor used a beam attack. You took {bossbeam} damage. You have {health} left. "))
                    elif bossatk == 2:
                        bossbeam = random.randint(10, 40)
                        if has_redam == True and has_blueam == True and has_greenam == True:
                            bossbeam = bossbeam / 2
                            health -= bossbeam - (constitution / 2)
                            print(input(f"Due to the combined power of the 3 amulets, the punch from Belphagor did half the damage. You took {bossbeam} damage. You have {health} left. "))
                        else:
                            health -= bossbeam - (constitution / 2)
                            print(input(f"Belphagor used a punch attack. You took {bossbeam} damage. You have {health} left. "))
                    else:
                        bossbeam = random.randint(1, 20)
                        if has_redam == True and has_blueam == True and has_greenam == True:
                            bossbeam = bossbeam / 2
                            ghealth += bossbeam
                            print(input(f"Due to the combined power of the 3 amulets, Belphagor only healed half of what he would do normally. Belpahgor has {ghealth} health. "))
                        else:
                            ghealth += bossbeam
                            print(input(f"Belphagor healed {bossbeam}. Belpahgor has {ghealth} health. "))
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
                    if action == "song":
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
                                    print(f"CRIT!!! You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                                    print(f"You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                                    print(f"CRIT!!! You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                                    print(f"You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                            print(f"You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                            print(f"You did {dmg_roll} damage. Belphagor has {ghealth} health left. ")
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
                        print(input("Belphagor's turn. "))
                    bossatk = random.randint(1, 3)
                    if bossatk == 1:
                        bossbeam = random.randint(20, 30)
                        if has_redam == True and has_blueam == True and has_greenam == True:
                            bossbeam = bossbeam / 2
                            health -= bossbeam - (constitution / 2)
                            print(input(f"Due to the combined power of the 3 amulets, the beam from Belphagor did half the damage. You took {bossbeam} damage. You have {health} left. "))
                        else:
                            health -= bossbeam - (constitution / 2)
                            print(input(f"Belphagor used a beam attack. You took {bossbeam} damage. You have {health} left. "))
                    elif bossatk == 2:
                        bossbeam = random.randint(10, 40)
                        if has_redam == True and has_blueam == True and has_greenam == True:
                            bossbeam = bossbeam / 2
                            health -= bossbeam - (constitution / 2)
                            print(input(f"Due to the combined power of the 3 amulets, the punch from Belphagor did half the damage. You took {bossbeam} damage. You have {health} left. "))
                        else:
                            health -= bossbeam - (constitution / 2)
                            print(input(f"Belphagor used a punch attack. You took {bossbeam} damage. You have {health} left. "))
                    else:
                        bossbeam = random.randint(1, 20)
                        if has_redam == True and has_blueam == True and has_greenam == True:
                            bossbeam = bossbeam / 2
                            ghealth += bossbeam
                            print(input(f"Due to the combined power of the 3 amulets, Belphagor only healed half of what he would do normally. Belpahgor has {ghealth} health. "))
                        else:
                            ghealth += bossbeam
                            print(input(f"Belphagor healed {bossbeam}. Belpahgor has {ghealth} health. "))
                    if health < 1:
                        print(input("You lose. Press enter to restart fight."))
                        health = 50
                        ghealth = 40
                        atkboost = 0
                        continue
                    else:
                        print(input("Your turn. "))
            break
        else:
            print("Invalid choice.")
            continue
    doyoucontinue = input("You beat Belphagor, the world is saved, and you can go back home. Would you like to play again? Type yes if you want to continue, or anything else if you want to leave.")
    if doyoucontinue == "yes":
        continue
    else:
        break