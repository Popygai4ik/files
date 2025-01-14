from turtle import *
tracer(0)
left(90)
k = 20
for i in range(3):
    pendown()
    for i in range(2):
        forward(10*k)
        right(90)
        forward(10*k)
        right(90)

    penup()
    forward(10*k)
    right(90)
    forward(5*k)
    right(90)
for x in range(-10, 50):
    for y in range(-10, 50):
        goto(x * k, y*k)
        dot(5, 'green')
done()