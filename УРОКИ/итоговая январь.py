def g(s,p,end):
    if s >= 81: return p in end
    if s < 81 and max(end)  == p:return False
    mov = [g((s*4)-3,p+1,end),g(s+2,p+1,end)]
    if (p+1)% 2 == end[0]% 2:
        return any(mov)
    else:
        return all(mov)
# for s in range(1, 81):
#     if g(s, 0,[2]):
#         print(s)
#     if g(s, 0,[2,4]):
#         print(s, '4')
def g2 (s, p, end):
    if s>= 81: return p in end
    if s< 81 and max(end) == p: return False
    mov = [g2(s * 2,p + 1, end), g2(s+3,p + 1, end),g2(s+ 1,p + 1, end)]
    if (p + 1) % 2 == end[0] % 2:
        return any(mov)
    else:
        return all(mov)

# for s in range(1, 81):
#     if g2(s, 0, [2]):
#         print(s)
#     if g2(s, 0, [2, 4]):
#         print(s, '4')

from turtle import *
#
# tracer(0)
# pendown()
# left(90)
# k = 20
# for i in range(4):
#     forward(k * 10)
#     right(270)
# penup()
# forward(k*3)
# right(270)
# forward(5*k)
# right(90)
# pendown()
# for i in range(2):
#     forward(k * 10)
#     right(270)
#     forward(12*k)
#     right(270)
# penup()
# for x in range(-20, 20):
#
#     for y in range(-20, 20):
#         setpos(x * k, y*k)
#         dot()
# done()
tracer(0)
pendown()
left(90)
k= 20
for i in range(6):
    forward(6*k)
    right(300)
penup()
forward(3*k)
right(270)
forward(5*k)
right(90)
pendown()
for i in range(2):
    forward(7*k)
    right(270)
    forward(9*k)
    right(270)

penup()
for x in range(-20, 20):

    for y in range(-20, 20):
        setpos(x * k, y*k)
        dot()
done()