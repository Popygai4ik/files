from turtle import *
tracer(0)
left(90)
k = 30
pendown()
for i in range(6):
    forward(3*k)
    right(300)
penup()
forward(3*k)
right(270)
forward(2*k)
right(90)
pendown()
for i in range(2):
    forward(3 * k)
    right(270)
    forward(4*k)
    right(270)
penup()
for x in range(-20, 20):

    for y in range(-20, 20):
        setpos(x * k, y * k)
        dot()
done()