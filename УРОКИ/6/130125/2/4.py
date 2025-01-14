from turtle import *

tracer(0)
# left(90)
c = 50
for i in range(16):
    forward(5*c)
    left(70)
    backward(2*c)
    right(10)
penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x *c, y*c)
        dot(5, 'green')
done()