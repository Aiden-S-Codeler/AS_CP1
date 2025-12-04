#AS 2nd Only Forward

import random

print("placeholder")
print(input("press enter to start"))

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
has_bomb = False
has_wararmor = False
has_warstick = False

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

