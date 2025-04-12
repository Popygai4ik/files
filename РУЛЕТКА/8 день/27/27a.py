import math

f = open('f0236998-6fb3-4ac3-a4c3-7d8895cc4bfc_27A.txt')
f.readline()
from main import *
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
best = [[] for i in range(len(classters))]
for i in range(len(classters)):
    mini = 10**10
    for p1 in classters[i]:
        R= 0
        for p2 in classters[i]:
            R+= math.dist(p1,p2)
        if R < mini:
            mini = R
            best[i] = [p1[0],p1[1]]
p_x =  int((sum(x for x,y in best) / len(best)) * 10000)
p_y =  int((sum(y for x,y in best) / len(best)) * 10000)
print(p_x,p_y)
# 25049 29918