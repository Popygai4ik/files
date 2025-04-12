from turtle import *
left(90)
tracer(0)
k = 25
screensize(2000,2000)
for i in range(22):
    forward(19*k)
    left(216)


penup()
for x in range(-20, 30):
    for y in range(-20, 30):
        goto(x*k,y*k)
        dot()
done()