import math

from main import *
from turtle import *

f = open('27A.txt')
f.readline()
points = [list(map(float, s.replace(',','.').split())) for s in f]
# print(points)
classters = []
eps = 0.5
while points:
    classters.append([points[0]])
    del points[0]
    for p1 in classters[-1]:
        for p2 in points[:]:
            # print(p1,p2)
            if math.dist(p1,p2)<eps:
                classters[-1].append(p2)
                points.remove(p2)
best = [[] for i in range(len(classters))]
for i in range(len(classters)):
    mimi = 10**10
    for t1 in classters[i]:
        r = 0
        for t2 in classters[i]:
            r += math.dist(t1,t2)
        if r < mimi:
            mimi = r
            best[i] = t1
p_x = int((sum(x for x,y in best)/len(best))*10000)
p_y = int((sum(y for x,y in best)/len(best))*10000)
print(p_x,p_y)
# ris(classters)
# ris2(best)
# done()