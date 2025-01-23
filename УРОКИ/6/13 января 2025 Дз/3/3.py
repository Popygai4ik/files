from turtle import *
tracer(0)
left(90)
k = 100
begin_fill()
right(90)
for i in range(3):
    right(45)
    forward(10*k)
    right(45)
right(315)
forward(10*k)
for i in range(2):
    right(90)
    forward(10*k)
penup()
end_fill()
# for x in range(-20, 10):
#     for y in range(-20, 10):
#         goto(x*k, y*k)
can = getcanvas()
c= 0
#         dot(5, 'green')
for x in range(-500, 500):
    for y in range(-500, 500):
        if can.find_overlapping(x * k, y* k, x * k, y* k)== (5, ):
            c +=1
print(c)
done()