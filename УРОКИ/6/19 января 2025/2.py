from turtle import *
tracer(0)
left(90)
k = 20
pendown()
for i in range(7):
    forward(6*k)
    right(270)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * k, y*k)
        dot()
done()