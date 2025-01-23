from turtle import *

tracer(0)
c = 30
lt(90)
rt(45)
forward(4*c)
for i in range(10):
    rt(45)
    forward(7 * c)
    rt(135)
    forward(4 * c)

up()
for x in range(-10, 20):
    for y in range(-10, 20):
        goto(x * c, y * c)
        dot(5, 'green')

update()
exitonclick()