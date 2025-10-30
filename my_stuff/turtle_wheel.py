#AS 2nd turtle color wheel
import turtle
screen = turtle.Screen()
screen.bgcolor("#000000")
t = turtle.Turtle()
t.speed(1200)
t.teleport(-90, 0)
t.left(90)
t.shape("turtle")
color = ['red','OrangeRed','orange','DarkGoldenrod1','yellow','GreenYellow','green','LightSeaGreen','blue','purple']
n = 0
for b in range(1000):
    t.color(color[n%10])
    t.fillcolor(color[n%10])
    n += 1
    for i in range(36):
        t.forward(1)
        t.right(1)

turtle.done