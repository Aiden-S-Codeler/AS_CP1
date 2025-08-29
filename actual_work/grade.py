# Grade Maker
#commenting commently

grade_eng = int(input("What is your grade percent in English?"))
grade_CS14000 = int(input("What is your grade percent in Computer Sciences?"))
grade_worldciv = int(input("What is your grade percent in World Civilization?"))
grade_adv = int(input("What is your grade percent in Advisory?"))
grade_math = int(input("What is your grade percent in Math?"))
grade_art = int(input("What is your grade percent in? Art"))
grade_biology = int(input("What is your grade percent in Biology?"))

grade_avg = (grade_adv + grade_art + grade_biology + grade_eng + grade_CS14000 + grade_math + grade_worldciv)/7

print("your average grade is",  grade_avg)