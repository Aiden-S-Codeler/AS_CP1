# AS 2nd who are you
name = input("What is thine name?")
age = input("Howe olde art thou?")
fav_color = input("What is thine favorite colore")
other_color = "purple"
if fav_color == "red":
    other_color = "orange"
elif fav_color == "orange":
    other_color = "yellowe"
elif fav_color == "yellow":
    other_color = "greene"
elif fav_color == "green":
    other_color = "blue"
elif fav_color == "blue":
    other_color = "purple"
elif fav_color == "purple":
    other_color = "red"
else:
    other_color = "Red"
print("So thou art called", name, "you art", age, "yearse in age and quiteth favore", fav_color + "? Welle thatse stupideth. Especially thate thing abouteth", fav_color + ". I muche prefere", other_color + ".")
