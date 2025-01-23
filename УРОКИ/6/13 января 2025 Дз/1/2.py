from turtle import *
tracer(0)
c = 30
lt(90)
for i in range(24):
    rt(90)
    forward(1*c)
    lt(45)
    forward(-1*c)
up()
for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x *c, y*c)
        dot(5,'green')

update()
exitonclick()