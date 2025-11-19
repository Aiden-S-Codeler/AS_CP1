# AS 2nd Calculator the sequel

# 4-8, creating adding system
def sum(*num):
    final = 0
    for i in num:
        final += i
    return final

# 11-18, creating averaging system
def average(*num):
    final = 0
    length = 0
    for i in num:
        final +=  i
        length += 1
    final = final / length
    return final

# 21-23, creating grabbing smallest number system
def mini(*num):
    final = min(num)
    return final

# 26-28, creating grabbing biggest number system
def maxi(*num):
    final = max(num)
    return final

# 31-35, creating multiplying system
def product(*num):
    final = 1
    for i in num:
        final *= i
    return final

# 38-41, running all systems
print(sum(5, 6, 7, 8, 9, 1, 2, 3, 4))
print(average(5, 6, 7, 8, 9, 1, 2, 3, 4))
print(mini(5, 6, 7, 8, 9, 1, 2, 3, 4))
print(maxi(5, 6, 7, 8, 9, 1, 2, 3, 4))
print(product(5, 6, 7, 8, 9, 1, 2, 3, 4))