# AS dnd random gen
# Stats

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

# Class

class_list = ["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorceror", "Warlock", "Wizard"]
rand_class = int(random.randint(0, 12))
class_chosen = class_list[rand_class]
print(f"Your class is: {class_chosen}")

# Race

race_list = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half Elf", "Halfling", "Half Orc", "Human", "Variant Human", "Teifling", "Aarakocra", "Aasimar", "Air Genasi", "Bug Bear", "Centaur", "Changeling", "Deep Gnome", "Duergar", "Earth Genasi", "Eladrin", "Fairy", "Firbolg", "Fire Genasi", "Githyanki", "Githzerai", "Goblin", "Goliath", "Harengon", "Hobgoblin", "Kenku", "Kobold", "Lizardfolk", "Minotaur", "Orc", "Satyr", "Sea Elf", "Shadar Kai", "Shifter", "Tabaxi", "Tortle", "Triton", "Water Genasi", "Yuan-Ti"]
rand_race = int(random.randint(0, 41))
if rand_race == 0:
    dragonborn_list = ["Red", "Blue", "Black", "White", "Green", "Copper", "Gold", "Brass", "Silver", "Bronze", "Amethyst", "Crystal", "Emerald", "Sapphire", "Topaz"]
    rand_dragonborn = int(random.randint(0, 14))
    race_chosen = dragonborn_list[rand_dragonborn] + " Dragonborn"
else:
    race_chosen = race_list[rand_race]
print(f"Your race is: {race_chosen}")

# where stats go
stat_list = [stat_1, stat_2, stat_3, stat_4, stat_5, stat_6]
str = 0
dex = 0
con = 0
int = 0
wis = 0
char = 0
while str == 0:
    what_str = input("Which of your stats do you want to be your strength?")
    if what_str.isdigit():
        what_str = int(what_str)
    else:
        print("Setting strength to 5 for trolling.")
        str = 5
    if what_str in stat_list:
        str = what_str
        stat_list.remove(what_str)
    else:
        print("Setting strength to 5 for trolling.")
        str = 5
while dex == 0:
    what_dex = input("Which of your stats do you want to be your dexterity?")
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

# Background

rand_personality = random.randint(1, 8)
rand_ideal = random.randint(1, 6)
rand_bond = random.randint(1, 6)
rand_flaw = random.randint(1, 6)
print(f"Your first rolls for background information are: Personality Trait: {rand_personality}, Ideal: {rand_ideal}, Bond: {rand_bond}, Flaw: {rand_flaw}")
rand_personality2 = random.randint(1, 8)
rand_ideal2 = random.randint(1, 6)
rand_bond2 = random.randint(1, 6)
rand_flaw2 = random.randint(1, 6)
while rand_personality2 == rand_personality:
    rand_personality2 = random.randint(1, 8)
while rand_ideal2 == rand_ideal:
    rand_ideal2 = random.randint(1, 6)
while rand_bond2 == rand_bond:
    rand_bond2 = random.randint(1, 6)
while rand_flaw2 == rand_flaw:
    rand_flaw2 = random.randint(1, 6)
print(f"Your second rolls for background information are: Personality Trait: {rand_personality2}, Ideal: {rand_ideal2}, Bond: {rand_bond2}, Flaw: {rand_flaw2}")