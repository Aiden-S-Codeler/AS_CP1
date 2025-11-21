#AS 2nd turtle starter
import turtle
t = turtle.Turtle()
t.speed(20)
t.color("LightBlue")
t.penup()
t.teleport(0,0)
t.pendown()
def draw_branch(length):
    if length > 5:
        for i in range(3):
            t.forward(length)
            t.forward(length / 3)
            t.right(180)
            t.forward(length)
            t.right(60)
for a in range(6):
    draw_branch(100)
    t.right(60)
t.hideturtle()
turtle.done()