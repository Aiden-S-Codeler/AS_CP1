# AS dnd random gen

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

class_list = ["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorceror", "Warlock", "Wizard"]
rand_class = int(random.randint(0, 12))
class_chosen = class_list[rand_class]
print(f"Your class is: {class_chosen}")

race_list = ["Dragon Born", "Dwarf", "Elf", "Gnome", "Half Elf", "Halfling", "Half Orc", "Human", "Teifling", "Aarakocra", "Aasimar", "Air Genasi", "Bug Bear", "Centaur", "Changeling", "Deep Gnome", "Duergar", "Earth Genasi", "Eladrin", "Fairy", "Firbolg", "Fire Genasi", "Githyanki", "Githzerai", "Goblin", "Goliath", "Harengon", "Hobgoblin", "Kenku", "Kobold", "Lizardfolk", "Minotaur", "Orc", "Satyr", "Sea Elf", "Shadar Kai", "Shifter", "Tabaxi", "Tortle", "Triton", "Water Genasi", "Yuan-Ti"]
rand_race = int(random.randint(0, 41))
race_chosen = race_list[rand_race]
if rand_race == 0:
    dragon_born_list = ["Red", "Blue", "Black", "White", "Green", "Copper", "Gold", "Brass", "Silver", "Bronze", "", "", "", "", ""]
    rand_dragon_born = int(random.randint(0, 14))
print(f"Your race is: {race_chosen}")