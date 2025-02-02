from turtle import *

left(90)
tracer(0)
pendown()
k = 20
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
    forward(3*k)
    right(270)
    forward(4*k)
    right(270)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k,y*k)
        dot()
done()
