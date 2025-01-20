from turtle import *
tracer(0)
k = 20
left(90)
pendown()
for i in range(7):
    right(90)
    forward(3*k)
    for j in range(2):
        left(90)
        forward(3*k)
left(20)

for i in range(7):
    right(90)
    forward(3*k)
    for j in range(2):
        left(90)
        forward(3*k)
penup()
for x in range(-20, 20):

    for y in range(-20, 20):
        setpos(x * k, y*k)
        dot()
done()