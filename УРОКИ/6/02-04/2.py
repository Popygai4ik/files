from turtle import *
tracer(0)
screensize(2000,2000)
k = 25
for i in range(2):
    forward(17*k)
    left(90)
    forward(34*k)
    left(90)
penup()
forward(10*k)
right(90)
forward(15*k)
right(90)
pendown()
for i in range(2):
    forward(40*k)
    right(90)
    forward(24*k)
    right(90)
penup()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*k,y*k)
        dot()
done()