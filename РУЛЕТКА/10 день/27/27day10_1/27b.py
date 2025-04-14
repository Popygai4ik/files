import math

f = open('27B.txt')
f.readline()
from main import *
from turtle import *
points = [list(map(float, s.replace(',','.').split())) for s in f]
classters = []
eps = 0.5
while points:
    classters.append([points[0]])
    del points[0]
    for p1 in classters[-1]:
        for p2 in points[:]:
            if math.dist(p1,p2)<eps:
                classters[-1].append(p2)
                points.remove(p2)
ris(classters)
min_res = 10**10
max_res = 0
for i in range(len(classters)):
    for p1 in classters[i]:
        for j in range(i + 1, len(classters)):
            for p2 in classters[j]:
                min_res = min(min_res, math.dist(p1,p2))
                max_res = max(max_res, math.dist(p1, p2))
print((int((max_res) *10000)),int((min_res)*10000))
# 81383 24534101795 8280
done()