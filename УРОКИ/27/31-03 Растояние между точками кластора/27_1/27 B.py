import math


def rs(a):
    screensize(2000,2000)
    left(90)
    tracer(0)
    k = 50
    penup()
    colo = ['black','red','orange','pink']
    for i in range(len(a)):
        for x,y in a[i]:
            goto(x*k,y*k)
            dot(6,colo[i])
def rs2(a):
    screensize(2000,2000)
    left(90)
    tracer(0)
    k = 50
    penup()
    colo = ['red','orange','pink']
    for i in range(len(a)):
        x,y = a[i][0],a[i][1]
        goto(x * k, y * k)
        dot(10, colo[i])

f = open('27B.txt')
f.readline()
from turtle import *
points = [list(map(float,s.replace(',','.').split())) for s in f]
k = 3
eps = 0.5
classters = []
while points:
    classters.append([points[0]])
    del points[0]
    for t1 in classters[-1]:
        for t2 in points[:]:
            if math.dist(t1, t2) < eps:
                classters[-1].append(t2)
                points.remove(t2)
    if len(classters[-1])<= 4:
        del classters[-1]
print(classters)
rs(classters)
# rs(muser)

besr = [[] for _ in range(k)]
for i in range(k):
    mini = 10**10
    for p1 in classters[i]:
        R = 0
        for p2 in classters[i]:
            R += math.dist(p1,p2)
        if R < mini:
            mini = R
            besr[i] = [p1[0],p1[1]]
p_x = int((sum(x for x,y in besr)/len(besr))*100_000)
p_y = int((sum(y for x,y in besr)/len(besr))*100_000)
print(p_x,p_y)
#287487840884967133
# 88496 7133

rs2(besr)
done()