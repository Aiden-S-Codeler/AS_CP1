# as 2nd Prite Treasure Split

print("You are Pirate Jim. \nYour crew got a large amount of money from a recent sale of plundered goods. \nEach member already got $500 dollars for the job. The First Mate will get 3 shares. The Captain will get 7 shares.")

bounty = input("how much money is there post crew payment (after everyone gets 500 dollars)")
crew_size = input("how big is the crew (not including you, the captain, and the first mate)")

bounty_check = bounty.isdigit()
crew_check = crew_size.isdigit()

if bounty_check == True and crew_check == True:
    bounty = int(bounty)
    crew_size = int(crew_size)
else:
    print("The code would have broken because of you so you no longer get any money. \nNow setting bounty and crew size to default size.")
    bounty = 10000
    crew_size = 39

total_bounty = (crew_size * 500) + bounty
share_size = bounty / (crew_size + 11)
captain_get = share_size * 7
fmate_get = share_size * 3
everyone_else = (share_size * 1) + 500

print(f"The total bounty before all payments is ${total_bounty:.2f}")
print(f"The Captain will get ${captain_get:.2f}")
print(f"The First Mate will get ${fmate_get:.2f}")
print(f"Everyone else will get ${everyone_else:.2f}")