from turtle import *


tracer(0)
left(90)
k = 2
pendown()
begin_fill()
for i in range(12):
    right(90)
    forward(125*k)
    right(90)
    forward(17*k)
end_fill()
done()