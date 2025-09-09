# AS 2nd Calculator

number1 = input("gimme number")
number2 = input("gimme another number")

proofnumber1 = number1.isdigit()
proofnumber2 = number2.isdigit()

if proofnumber1 == True:
    number1 = int(number1)
else:
    print("Put in an actual number you criminal D:")

if proofnumber2 == True:
    number2 = int(number1)
else:
    print("Put in an actual number you criminal D:")

add = number1 + number2
minus = number1 - number2
multy = number1 * number2
divide = number1 / number2
modulus = number1 % number2

if add == 69 or minus == 69 or multy == 69 or divide == 69 or modulus == 69:
    print("no")
elif add == 67 or minus == 67 or multy == 67 or divide == 67 or modulus == 67:
    print("no")
elif add == 420 or minus == 420 or multy == 420 or divide == 420 or modulus == 420:
    print("no")
else:
    print(add)
    print(minus)
    print(multy)
    print(divide)
    print(modulus)