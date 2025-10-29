#AS 2nd turtle race

import turtle
import random

# lines 4 - 8: set screen up
screen = turtle.Screen()
screen.setup(1200, 800)
screen.bgcolor("black")
screen.title("TURTLE RACING LETS GOOOOOOO!!!!!!!!!!!!!")

#lines 13 - 36: set up all 6 turtles
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
t6 = turtle.Turtle()
t1.color("red")
t2.color("orange")
t3.color("yellow")
t4.color("green")
t5.color("blue")
t6.color("purple")
t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
t4.shape("turtle")
t5.shape("turtle")
t6.shape("turtle")
t1.teleport(-300, 150)
t2.teleport(-300, 100)
t3.teleport(-300, 50)
t4.teleport(-300, 0)
t5.teleport(-300, -50)
t6.teleport(-300, -100)

#lines 39 - 45: set up finish line
finish = turtle.Turtle()
finish.color("#FFFFFF")
finish.pensize(20)
finish.teleport(300, 1200)
finish.right(90)
finish.speed(1200)
finish.forward(2400)

#lines 48 - 74: move turtle, check if any have gotten far enough to win, if their is a winner: announce winner, else: continue
while True:
    t1.forward(random.randint(1, 10))
    t2.forward(random.randint(1, 10))
    t3.forward(random.randint(1, 10))
    t4.forward(random.randint(1, 10))
    t5.forward(random.randint(1, 10))
    t6.forward(random.randint(1, 10))
    if t1.xcor() >= 300:
        print("RED WINS!!!")
        break
    elif t2.xcor() >= 300:
        print("ORANGE WINS!!!")
        break
    elif t3.xcor() >= 300:
        print("YELLOW WINS!!!")
        break
    elif t4.xcor() >= 300:
        print("GREEN WINS!!!")
        break
    elif t5.xcor() >= 300:
        print("BLUE WINS!!!")
        break
    elif t6.xcor() >= 300:
        print("PURPLE WINS!!!")
        break
    else:
        continue

turtle.done()