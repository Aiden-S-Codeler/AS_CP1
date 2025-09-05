# AS 2nd Idiot Proofing
f_name = input("What is your first name?").strip().lower().title().replace(" ","")
l_name = input("What is your last name?").strip().lower().title().replace(" ","")
phone = input("What is your Phone Number?").strip().lower().replace(","," ").replace("-"," ")
grade = float(input("What is your GPA?").strip())
print(f"So your name is {f_name} {l_name}, your phone number is {phone}, and you have a GPA of {grade}.")