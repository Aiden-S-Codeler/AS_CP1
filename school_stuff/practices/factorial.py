#AS 2nd factorial
# ask user to input a specific number
# do a while loop inside an if statement to check if they put an interger // i have to make the while loop the outer one
# else they dont put an interger loop back and ask again for a number
# if the do, break from the loop
# define a function
# find all numer less than input by checking if num < input
# add all numbers to a list
# multiply all number against eachother and display the input and the result

while True:
    number = input("Give me a number. ")
    if number.isdigit() == True:
        number = int(number)
        break
    else:
        continue

def factorial(uinput):
    num = 1
    factor_list = []
    if uinput > num:
        factor_list.append(uinput)
        uinput -= 1
    else:
        pass
    for i in factor_list:
        num *= i
    print(f"Original: {factor_list[0]}. Factored: {num}")

print(factorial(number))