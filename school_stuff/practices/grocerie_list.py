# AS 2nd CS1400 grocery list

shopping_list = []

while True:
    print("What of the following would you like to do to your grocery list; add item, remove item, check list, quit")
    choice = input("Enter choice here: ")
    if choice == "add item":
        item = input("What item would you like to add?: ")
        shopping_list.append(item)
        print(f"Added {item} to list.")
    elif choice == "remove item":
        item = input("What item would you like to remove?: ")
        if item in shopping_list: 
            shopping_list.remove(item)
            print(f"Removed {item} to list.")
        else:
            print("That item isn't in your list.")
    elif choice == "check list":
        print(shopping_list)
    elif choice == "quit":
        print("Ending program...")
        break
    else:
        print("Please choose valid option.")