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
        dot(6, colo[i])

f = open('27A.txt')
f.readline()
from turtle import *
points = [list(map(float,s.replace(',','.').split())) for s in f]
k = 2
muser = [[],[],[]]
classters = [[]for k in range(2)]
for x,y in points:
    if x > 0 and y > 0:
        classters[0].append([x,y])
    elif -3 < x < 0.2 and -2.4 < y<0:
        classters[1].append([x,y])
    # else:
    #     muser[2].append([x,y])
# print(classters)
# rs(classters)
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
#28748 7840


# rs2(besr)
# done()