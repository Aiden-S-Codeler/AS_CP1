# as 2nd TURTLE
import turtle
n = 0
r = 1
d = 2
l = 3
u = 4
color = ['red','orange','yellow','green','blue','purple']
turtle.color("#FF3600")
turtle.speed(25000)
while True:
    turtle.forward(r)
    turtle.right(90)
    turtle.forward(d)
    turtle.right(90)
    turtle.forward(l)
    turtle.right(90)
    turtle.forward(u)
    turtle.right(90)
    turtle.color(color[n%6])
    r += 4
    d += 4
    l += 4
    u += 4
    n += 1
    if n >= 500:
        break
    else:
        continue


turtle.done()