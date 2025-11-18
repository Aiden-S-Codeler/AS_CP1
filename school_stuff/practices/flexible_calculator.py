# AS 2nd Calculator the sequel

#4-, creating adding system
def sum(*num):
    while True:
        add_num = input("Please enter a number. If you are done adding numbers, please say 'done'. ")
        if add_num.isdigit():
            num.append(float(add_num))
        elif add_num.lower() == "done":
            break
        else:
            print("invalid")
            continue
    final = 0
    for i in num:
        final += i
    return final

#
def average(*num):
    pass

#
def min(*num):
    pass

#
def max(*num):
    pass

#
def product(*num):
    pass

funlist = []

print(sum(funlist))