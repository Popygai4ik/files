import math
from turtle import *
from  main import *
f = open('27A.txt')
f.readline()
points = [list(map(float, s.replace(',','.').split()))for s in f]
classters = []
eps = 1
while points:
    classters.append([points[0]])
    del points[0]
    for p1 in classters[-1]:
        for p2 in points[:]:
            if math.dist(p2,p1) < eps:
                classters[-1].append(p2)
                points.remove(p2)
best = [[] for _ in range(len(classters))]
for i in range(len(best)):
    mini = 10**10
    for t1 in classters[i]:
        R = 0
        for t2 in classters[i]:
            R += math.dist(t2,t1)
        if R < mini:
            mini = R
            best[i]=t1
p_x = int((sum(x for x,y in best)/len(best))*1000)
p_y = int((sum(y for x,y in best)/len(best))*1000)
# 6537 5475
print(p_x,p_y)
# ris(classters)
# ris2(best)
# done()