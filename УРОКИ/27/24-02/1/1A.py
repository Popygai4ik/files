import math
from turtle import *

f = open('27A.txt')
f.readline()
points = [list(map(float, s.replace(',', '.').split())) for s in f]
# print(points)
k = 2
klaster = [[] for i in range(k)]
for x, y, brigt in points:
    if x > -1:
        klaster[0].append([x, y, brigt])
    else:
        klaster[1].append([x, y, brigt])
def sre(cls):
    s1 = sum([br for x,y,br in cls])
    return s1/len(cls)

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
# visila(klaster)
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
res = []
for popa in klaster:
    # print(popa)
    res.append(sre(popa))
print(int(sum(res)*1000))
# done()
