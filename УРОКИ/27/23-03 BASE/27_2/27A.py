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
    colors = ['pink','orange']
    for i in range(len(a)):
        x,y = a[i]
        goto(x * k, y * k)
        dot(10, colors[i])
f = open('27A.txt')
f.readline()
points = [list(map(float, s.replace(',','.').split())) for s in f]
classters = []
eps = 1
while points:
    classters.append([points[0]])
    del points[0]
    for p1 in classters[-1]:
        for p2 in points[:]:
            if math.dist(p1,p2) < eps:
                classters[-1].append(p2)
                points.remove(p2)
# ris(classters)
# done()
best = [[],[]]
for i in range(len(best)):
    mini = 10**10
    for  x_c,y_c in classters[i]:
        R= 0
        for x_t,y_t in classters[i]:
            R += math.dist([x_c,y_c],[x_t,y_t])
        if R < mini:
            mini = R
            best[i] = [x_c, y_c]
p_x = int((sum(x for x, y in best) / len(best))*10000)
p_y = int((sum(y for x, y in best) / len(best))*10000)
print(p_x,p_y)
ris(classters)
ris2(best)
done()