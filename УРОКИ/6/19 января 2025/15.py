from turtle import *

left(90)
pendown()
tracer(0)
screensize(2000, 2000)
k= 20
for i in range(4):
    for j in range(4):
        for f in range(4):
            forward(3*k)
            right(60)
        forward(3*k)
    forward(3 * k)

penup()
for x in range(-20, 20):
    for y in range(-10, 20):
        goto(x*k, y*k)
        dot()
done()