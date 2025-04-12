from turtle import *
tracer(0)
left(90)
screensize(2000,2000)
k = 30
pendown()
right(315)
for i in range(13):
    forward(12*k)
    right(45)
    forward(6*k)
    right(135)
penup()
for x in range(-20, 20):
    for y in range(-20,20):
        goto(x*k,y*k)
        dot(7, 'red')

done()
