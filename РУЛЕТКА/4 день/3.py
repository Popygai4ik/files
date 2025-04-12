from turtle import *
k = 10

tracer(0)
screensize(2000,2000)
for _ in range(2):
    forward(18*k)
    right(90)
    forward(16*k)
    right(90)
penup()
forward(28*k)
left(270)
backward(10)
pendown()

for _ in range(4):
    forward(37*k)
    right(90)
    forward(46*k)
    right(90)
penup()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*k,y*k)
        dot()
done()