from turtle import *
screensize(2000,2000)
left(90)
pendown()
tracer(0)
k = 10
for i in range(4):
    forward(28*k)
    right(90)
    forward(26*k)
    right(90)
penup()
forward(8*k)
right(90)
forward(7*k)
left(90)
pendown()

for i in range(4):
    forward(67*k)
    right(90)
    forward(98*k)
    right(90)
penup()
for x in range(-30, 50):
    for y in range(-50, 50):
        goto(x*k,k*y)
        dot()
done()