from turtle import *

tracer(0)
c = 40
lt(90)
for i in range(7):
    forward(10 * c)
    rt(120)

up()
for x in range(-10, 20):
    for y in range(-10, 20):
        goto(x * c, y * c)
        dot(5, 'green')

update()
exitonclick()