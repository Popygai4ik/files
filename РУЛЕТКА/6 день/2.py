from turtle import *
left(90)
tracer(0)
k = 25
screensize(2000,2000)
for i in range(4):
    forward(16*k)
    right(90)
    forward(22*k)
    right(90)
penup()
forward(5*k)
right(90)
forward(5*k)
left(90)
pendown()
for i in range(16):
    forward(52 * k)
    right(90)
    forward(77 * k)
    right(90)


penup()
for x in range(-20, 30):
    for y in range(-20, 30):
        goto(x*k,y*k)
        dot()
done()