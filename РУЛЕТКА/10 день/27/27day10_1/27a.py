import math

f = open('27A.txt')
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

min_res = 10**10
max_res = 0
for i in range(len(classters)):
    for j in range(i+1,len(classters)):
        for p1 in classters[i]:
            for p2 in classters[j]:
                min_res = min(min_res, math.dist(p1,p2))
                max_res = min(max_res, math.dist(p1, p2))
print(max_res,min_res)