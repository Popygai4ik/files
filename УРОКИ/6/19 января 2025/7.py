from turtle import *

left(90)
pendown()
tracer(0)
screensize(2000, 2000)
k= 20
for i in range(4):
    forward(15*k)
    right(90)
    forward(19*k)
    right(90)
penup()
forward(k*8)
right(90)
forward(6*k)
left(90)
pendown()

for i in range(2):
    forward(89*k)
    right(90)
    forward(77*k)
    right(90)
penup()
for x in range(-20, 20):
    for y in range(-10, 20):
        goto(x*k, y*k)
        dot()
done()