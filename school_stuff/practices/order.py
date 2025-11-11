# AS 2nd menu
# 3-20, setting up menu
main = {
    "burger" : 95,
    "taco" : 92,
    "47.3 pounds of north atlantic cod" : 7,
    "panino" : 107
}
side = {
    "fries" : 333,
    "sliders" : 5000,
    "fish and chips. the fish just happens to be 47.9 pounds of north atlantic cod" : -5000,
    "cube of meat" : 8
}
drink = {
    "coffee" : 8,
    "soda" : 27,
    "47.5 pounds of north atlantic cod thats been blended" : -7,
    "coffee^2" : 9
}

# 23-61, setting up ordering process
total = 0
main_ord = ""
drink_ord = ""
side_ord1 = ""
side_ord2 = ""
def order(main_ord, drink_ord, side_ord1, side_ord2, total):
    main_ord = input(f"what would you like to order for your main: (options: {main.keys()})")
    drink_ord = input(f"what would you like to order for your drink: (options: {drink.keys()})")
    side_ord1 = input(f"what would you like to order for your side: (options: {side.keys()})")
    side_ord2 = input(f"what would you like to order for your side: (options: {side.keys()})")
    while True:
        if main_ord in main:
            total += main[main_ord]
            break
        else:
            print("invalid")
            continue
    while True:
        if drink_ord in drink:
            total += drink[drink_ord]
            break
        else:
            print("invalid")
            continue
    while True:
        if side_ord1 in side:
            total += side[side_ord1]
            break
        else:
            print("invalid")
            continue
    while True:
        if side_ord2 in side:
            total += side[side_ord2]
            break
        else:
            print("invalid")
            continue
    return(main_ord, drink_ord, side_ord1, side_ord2, total)

# 64-, letting user order
main_ord, drink_ord, side_ord1, side_ord2, total = order(main_ord, drink_ord, side_ord1, side_ord2, total)
print(f"Your order: {main_ord}, {drink_ord}, {side_ord1}, {side_ord2}\nYour total: {total}")