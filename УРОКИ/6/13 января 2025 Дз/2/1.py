from turtle import *
left(90)
tracer(0)
c = 30
for i in range(12):
    right(60)
    forward(5*c)
    left(30)
    backward(5*c)
penup()
for x in range(-10, 10):

    for y in range(-10, 10):
        setpos(x*c, y*c)
        dot(4, 'green')
done()