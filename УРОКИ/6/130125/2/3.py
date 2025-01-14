from turtle import *

tracer(0)
c = 40
left(90)
for i in range(9):
    forward(5*c)
    right(90)
    forward(4*c)
    right(90)
penup()
for x in range(-20, 20):
    for y in range(-20,20):
        goto(x*c, y*c)
        dot(5,'green')
done()