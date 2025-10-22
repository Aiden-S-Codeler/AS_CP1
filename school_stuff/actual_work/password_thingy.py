#AS 2nd



#loop while they are making password
while True:

    # ask what password should be

    password = input("What would you like you password to be? ")

    # make / restart point counter

    point = 0

    # check length and give point if password 8 characters or longer

    if len(password) >= 8:
        point += 1
    else:
        pass

    # make lists to loop through to see if any special / numerical / uppercase / lowercase charcters are in the password (its good if they are)

    num_char = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    sp_char = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    sp_char.split
    up_or_low_char = "qwertyuiopasdfghjklzxcvbnm"
    up_or_low_char.split

    # loop to check if charcters are in password

    for x in num_char:
        if x in password:
            point += 1
            break
        else:
            pass
    
    for y in sp_char:
        if y in password:
            point += 1
            break
        else:
            pass
    
    for l in up_or_low_char:
        if l in password:
            point += 1
            break
        else:
            pass
    
    for u in up_or_low_char:
        if u.upper() in password:
            point += 1
            break
        else:
            pass
    
    # check password strength and tell user how strong password is (1 or lower: incredibly weak, 2: weak, 3: medium strength, 4: strong, 5 [or more somehow]: very strong)

    if point <= 1:
        print("you have a very weak password")
    elif point == 2:
        print("you have a weak password")
    elif point == 3:
        print("you have a medium strength password")
    elif point == 4:
        print("you have a strong password")
    elif point >= 5:
        print("you have a very strong password")
    else:  
        # if point isn't one of the previous, then it ended up as a peice of text, and code should probably restart
<<<<<<< HEAD
        print("something broke. restarting... ")
        continue

    # ask if want to change password
    while True:
        pass_change = input("Is this the password you want")
        if pass_change == "yes":
            break
=======
        print("something broke. Restarting...")
        continue

    # ask if password is what they want, if yes; end, if not; restart
    if input("Would you like to make this your password? ( yes / no (anything that is not yes or no will be counted as no)) ") == "yes":
        print("Finalizing... ")
        break
    else:
        print("Restaring...")
        continue
>>>>>>> 84cbde62eb7392aa8a42405cd1e20f1483480313
