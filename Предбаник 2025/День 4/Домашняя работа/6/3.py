from turtle import *

tracer(0)
k = 20



for i in range(3):
    forward(12*k)
    right(120)
penup()
right(60)
forward(6*k)
left(60)
pendown()
for i in range(3):
    forward(15*k)
    right(90)
    forward(24*k)
    right(90)
penup()
for x in range(-20, 20):
    for y in range(-20,20):
        setpos(x*k,y*k)
        dot()
done()