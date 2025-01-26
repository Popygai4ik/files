import math
from turtle import *
f = open('27-2/27A.txt')
f.readline()
points = [list(map(float, s.replace(',','.').split())) for s in f]
# print(points)
k = 50
screensize(2000, 2000)
tracer(0)
penup()
# for x, y in points:
#     setpos(x*k,y*k)
#     dot()
# for x in range(-10, 10):
#     for y in range(-10, 10):
#         setpos(x*k, y*k)
#         if x == 0 or y==0:
#             dot(5,'red')
#         else:
#             dot()
# done()
k_clas = 2
clas = [[] for _ in range(k_clas)]
for x,y in points:
    if y > 1:
        clas[0].append([x, y])
    else:
        clas[1].append([x, y])
# color = ['red', 'green']
b_clas = [[] for _ in range(k_clas)]
for i in range(k_clas):
    mini= 100000000000000000
    for C_X, Y_C in clas[i]:
        sumi_dist = 0
        for x1, y1 in clas[i]:
            sumi_dist += math.dist([C_X, Y_C], [x1,y1])
        if sumi_dist < mini:
            mini = sumi_dist
            b_clas[i] = [C_X, Y_C]
print(b_clas)
p_x = int((sum(x for x,y in b_clas) / k_clas) * 10000)
p_y = int((sum(y for x,y in b_clas) / k_clas) * 10000)
print(p_x, p_y)