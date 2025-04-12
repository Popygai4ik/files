from turtle import *
tracer(0)
screensize(2000,2000)
left(90)
k = 25
for i in range(2):
    forward(10*k)
    right(90)
    forward(18*k)
    right(90)
penup()
forward(5*k)
right(90)
forward(7*k)
left(90)
pendown()
for i in range(2):
    forward(10*k)
    right(90)
    forward(7*k)
    right(90)
penup()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*k,y*k)
        dot()
done()