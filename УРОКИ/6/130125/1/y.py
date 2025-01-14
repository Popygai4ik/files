from turtle import *
c = 20
tracer(0)
lt(90)
# rt(45)
# forward(5* c)
for i in range(13):
    forward(6*c)
    rt(90)
up()
for x in range(-20, 20):

    for y in range(-100, 100):
        goto(x*c, y*c)
        dot(5, 'red')
update()
exitonclick()

