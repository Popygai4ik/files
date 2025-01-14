from turtle import *
tracer(0)
k = 110
begin_fill()
left(90)
for i in range(21):
    forward(125*k)
    right(120)
end_fill()
can = getcanvas()
c = 0
for x in range(-500, 500):
    for y in range(-500, 500):
        if can.find_overlapping(x * k, y* k, x * k, y* k)== (5, ):
            c +=1
print(c)
done()