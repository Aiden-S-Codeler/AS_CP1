# AS 2nd grade thingy
grade_list_num = []
grade_list_letter = []
class_number = 1
grade_letter = "A"
finish = False
while finish == False:
    grade_ask = input(f"what is your grade for class {class_number} numerically")
    if grade_ask.isdigit():
        pass
    else:
        finish = True
    while grade_ask.isdigit():
        grade_ask = int(grade_ask)
        grade_list_num.append(grade_ask)
        if grade_ask <= 60:
            grade_letter = "F"
        elif grade_ask < 70:
            grade_letter = "D"
        elif grade_ask < 80:
            grade_letter = "C"
        elif grade_ask < 90:
            grade_letter = "B"
        else:
            grade_letter = "A"
        grade_list_letter.append(grade_letter)
        finish_ask = input("have you done of of your classes (y/n)")
        if finish_ask == "n":
            finish = False
        else:
            finish = True
print(f"Your grades numerically are {grade_list_num}")
print(f"Your grades by letter are {grade_list_letter}")