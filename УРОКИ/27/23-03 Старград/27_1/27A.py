import math
from turtle import *
def ris(a):
    tracer(0)
    screensize(2000,2000)
    penup()
    left(90)
    k = 50
    colors = ['red','black','pink','orange']
    for i in range(len(a)):
        for x,y in a[i]:
            goto(x*k,y*k)
            dot(5,colors[i])
def ris2(a):
    tracer(0)
    screensize(2000,2000)
    penup()
    left(90)
    k = 50
    colors = ['black','red','pink','orange']
    for i in range(len(a)):
        x,y = a[i]
        goto(x * k, y * k)
        dot(5, colors[i])


f = open('27A.txt')
f.readline()
points = [list(map(float, s.replace(',','.').split()))for s in f ]
# print(points)
k = 3
clastrw = [[] for _ in range(k)]
for x, y in points:
    if x > 0:
        clastrw[0].append([x,y])
    elif x < 0 and y>0.2:
        clastrw[1].append([x,y])
    else:
        clastrw[2].append([x,y])

clastrw = clastrw[:2]
k = k - 1
best = [[3.3357775620119314, 0.9456769780461322], [-4.460379939535058, 1.8798779656259534]]
# for i in range(k):
#     min_r = 10**10
#     for x_c, y_c in clastrw[i]:
#         R = 0
#         for x_t,y_t in clastrw[i]:
#             R +=  ((x_c - x_t) ** 2 + (y_c - y_t) ** 2) ** 0.5
#         if R < min_r:
#             min_r = R
#             best[i] = [x_c,y_c]
# ris(clastrw)
# ris2(best)
# done()
# print(best )
p_x = int((sum(x for x,y in best) / 2)*10000)
p_y = int((sum(y for x,y in best) / 2)*10000)
print(p_x,p_y)
# 5623 14127
#[[3.3357775620119314, 0.9456769780461322], [-4.460379939535058, 1.8798779656259534]]