#AS 2nd ceaser cypher
import string

low_letters = string.ascii_lowercase #this will get all the lowercase letters for later
up_letters = string.ascii_uppercase #this will get all the uppercase letters for later

def encode(): #create an encoding system
    #get the message to encrypt
    code = input("Please enter the code to encrypt: ")
    #ask them how many to shift to get new message and check if its a number
    while True:
        key = input("Please enter key for the code: ")
        if key.isdigit(): #if it is a number, make it an interger and stop looping
            key = int(key)
            break
        else: #if its not a number restart
            continue
    #now we encrypt massage
    final = "" #for later use
    for i in code:
        if i in low_letters: #if the letter is a lowercase
            position = low_letters.find(i) #find its position
            new_position = (position + key) % 26 #find the position of letter
            new_letter = low_letters[new_position] #find letter
            final += new_letter #add the new letter
        elif i in up_letters: #if the letter is uppercase
            position = up_letters.find(i) #find its position
            new_position = (position + key) % 26 #find the position of letter
            new_letter = up_letters[new_position] #find letter
            final += new_letter #add the new letter
        else:
            final += i #its likely either a space or a symbol so we add it normally
    print(final) #give user encrypted code

def decode(): #create a decoding system
    #get the encrypted message
    code = input("Please enter the code to decrypt: ")
    #ask them how many to shift to get real message and check if its a number
    while True:
        key = input("Please enter key for the code: ")
        if key.isdigit(): #if it is a number, make it an interger and stop looping
            key = int(key)
            break
        else: #if its not a number restart
            continue
    #now we decrypt massage
    final = "" #for later use
    for i in code:
        if i in low_letters: #if the letter is a lowercase
            position = low_letters.find(i) #find its position
            new_position = (position - key) % 26 #find the position of shifted letter
            new_letter = low_letters[new_position] #find shifted letter
            final += new_letter #add the new letter
        elif i in up_letters: #if the letter is uppercase
            position = up_letters.find(i) #find its position
            new_position = (position - key) % 26 #find the position of shifted letter
            new_letter = up_letters[new_position] #find shifted letter
            final += new_letter #add the new letter
        else:
            final += i #its likely either a space or a symbol so we add it normally
    print(final) #give user decrypted code

while True: #ask user what you would like to do and loop until they quit the program
    user_selection = input("Would you like to 1: encode a message, 2: decode a message, 3: quit program\nPlease enter the number for the choice: ")
    if user_selection == "1":
        encode()
    elif user_selection == "2":
        decode()
    elif user_selection == "3":
        break
    else:
        continue