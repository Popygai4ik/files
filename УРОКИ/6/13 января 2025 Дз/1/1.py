from turtle import *

c = 20
tracer(0)
lt(90)
for i in range(9):
    rt(80)
    forward(5*c)
up()
for x in range(-10, 10):

    for y in range(-10, 10):
        goto(x* c, y*c)
        dot(5, 'red')
update()
exitonclick()