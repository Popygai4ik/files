from turtle import *

left(90)
pendown()
tracer(0)
k = 20
for _ in range(4):
    forward(k*3)
    right(90)
forward(3*k)
right(270)
forward(2*k)
right(270)
for _ in range(2):
    forward(k*6)
    right(270)
    forward(6*k)
    right(270)
right(180)
forward(3*k)
right(180)
for _ in range(2):
    forward(k*9)
    right(270)
    forward(9*k)
    right(270)
penup()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*k,k*y)
        dot()

done()