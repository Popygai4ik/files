from turtle import *
tracer(0)
left(90)
k = 20
pendown()
for i in range(8):
    forward(7*k)
    right(90)
penup()
forward(2*k)
right(90)
forward(k*3)
left(90)
pendown()
for i in range(2):
    forward(6*k)
    right(90)
    forward(8*k)
    right(90)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * k, y*k)
        dot()
done()