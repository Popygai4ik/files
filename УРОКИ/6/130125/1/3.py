from turtle import *

tracer(0)
c = 30
lt(90)
for i in range(2):
    forward(13 * c)
    rt(90)
    forward(5 * c)
    rt(90)
up()
for x in range(-10, 20):
    for y in range(-10, 20):
        goto(x * c, y * c)
        dot(5, 'green')

update()
exitonclick()