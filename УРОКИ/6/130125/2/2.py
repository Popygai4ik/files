from turtle import *

tracer(0)
c = 10
left(90)
for i in range(5):
    forward(10*c)
    right(144)
    forward(10*c)
    left(72)
penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x*c, y*c)
        dot(4, 'green')
done()