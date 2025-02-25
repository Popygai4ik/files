import math
from statistics import pvariance
from turtle import *

f = open('27A.txt')
f.readline()
points = [list(map(float, s.replace(',', '.').split())) for s in f]
k = 2
klaster = [[] for i in range(k)]
for x, y, brigt in points:
    if x > 0:
        klaster[0].append([x, y, brigt])
    else:
        klaster[1].append([x, y, brigt])
def sre(cls):
    print(cls)
    s1 = sum([br for x,y,br in cls])
    return s1/len(cls)
def desp(li):
    return pvariance(li)
def y2(list):
    res = 0
    print(list)
    for j in list:
        sr = sre(j)
        dis = desp(j)
        st_ot = dis*0.5
        for x,y,b in j:
            if (b - sr) > st_ot*1.5:
                res +=1
    return res

def visila(clas):
    left(90)
    penup()
    tracer(0)
    k = 50
    clo = ['green', 'black', 'red', 'blue']
    for gi in range(len(clas)):
        for x, y, brig in clas[gi]:
            goto(x * k, y * k)
            dot(4, clo[gi])


def visila2(best):
    left(90)
    penup()
    tracer(0)
    k = 50
    clo = ['red', 'blue', 'black']
    for i in range(len(best)):
        # print(best[i])
        x, y, b = best[i][0], best[i][1], best[i][2]
        goto(x * k, y * k)
        dot(10, clo[i])


# print(points)
visila(klaster)
best = [[] for i in range(k)]
for i in range(k):
    min_ras = 8798799797978
    for x_c, y_c, b1 in klaster[i]:
        R = 0
        for x_t, y_t, b2 in klaster[i]:
            R += math.dist([x_c, y_c], [x_t, y_t])
        if R < min_ras:
            min_ras = R
            best[i] = [x_c, y_c, b1]
# print(best)
# visila2(best)
P_yx = int(sum([x+y for x,y,b in best])*10000)
print(P_yx)
print(y2(points))
# done()
