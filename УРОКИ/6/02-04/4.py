from turtle import *
tracer(0)
screensize(2000,2000)
left(90)
k = 25
for i in range(6):
    forward(3*k)
    right(90)
penup()
forward(1*k)
right(270)
forward(1*k)
right(90)
pendown()
for i in range(6):
    forward(4*k)
    right(90)
    forward(5*k)
    right(90)
penup()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*k,y*k)
        dot()
done()