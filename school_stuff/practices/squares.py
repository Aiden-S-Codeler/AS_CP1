# AS 2nd squaring numbers
square = lambda a : a * a #making it possible to square
numlist = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285] #making list of numbers to square
for i in numlist: #looping through list and squaring all the numbers
    print(f"Original number: {i}. Squared number: {square(i)}")