from turtle import *
tracer(0)
k = 30
left(90)
pendown()
for i in range(6):
    forward(8*k)
    right(90)
penup()
forward(1 * k)
right(90)
forward(3 * k)
left(90)
pendown()
for i in range(12):
    forward(6*k)
    right(120)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * k, y*k)
        dot()
done()