import math
from turtle import *
f = open('27-1/27B.txt')
f.readline()
points = [list(map(float, s.replace(',', '.').split())) for s in f]

k = 50
screensize(2000, 2000)
tracer(0)
penup()
# for x, y in points:
#     setpos(x*k, y*k)
#     dot()
# for x in range(-10, 10):
#     for y in range(-10, 10):
#         setpos(x*k, y*k)
#         if x == 0 or y == 0:
#             dot(10, 'blue')
#         else:
#             dot()
# done()
k_klas = 3
clas = [[] for _ in range(k_klas)]
for x, y in points:
    if y > 0:
        clas[0].append([x, y])
    elif y < 0 and x < -1:
        clas[1].append([x, y])
    else:
        clas[2].append([x,y])
color = ['red', 'green', 'blue']
for i in range(k_klas):
    for x, y in clas[i]:
        setpos(x*k, y*k)
        dot(4, color[i])
# done()
b_clas = [[] for _ in range(k_klas)]
for i in range(k_klas):
    mini= 100000000000000000
    for C_X, Y_C in clas[i]:
        sumi_dist = 0
        for x1, y1 in clas[i]:
            sumi_dist += math.dist([C_X, Y_C], [x1,y1])
        if sumi_dist < mini:
            mini = sumi_dist
            b_clas[i] = [C_X, Y_C]
print(b_clas)
goto(-3.3241994862908877 * k,2.257962477196189*k)
dot(14, 'blue')
goto(-4.1548425080906 * k,-2.652215153449879*k)
dot(14, 'blue')
goto(0.532818526302969 * k,-3.2026370041905645*k)
dot(14, 'blue')
p_x = int((sum(x for x,y in b_clas) / k_klas) * 10000)
p_y = int((sum(y for x,y in b_clas) / k_klas) * 10000)
print(p_x, p_y)
done()