from turtle import *

tracer(0)
c = 20
left(90)
for i in range(12):
    forward(5*c)
    right(120)

penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x*c, y*c)
        dot(5, 'green')
done()