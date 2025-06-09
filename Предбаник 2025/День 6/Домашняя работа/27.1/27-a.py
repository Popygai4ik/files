import math
from main import *
f = open('27.2.А.txt')
# print(f.readlines())
f.readline()
points = [list(map(float, s.replace(',','.').split())) for s in f]
# print(points)
classters  = []
eps = 0.9
while points:
    classters.append([points[0]])
    del points[0]
    for p1 in classters[-1]:
        for p2 in points[:]:
            if math.dist(p1,p2) < eps:
                classters[-1].append(p2)
                points.remove(p2)

besty = [[] for i in range(len(classters))]
for i in range(len(classters)):
    mini = 100000000123123
    for p1 in classters[i]:
        r = 0
        for p2 in classters[i]:
            r += math.dist(p1,p2)
        if r < mini:
            mini = r
            besty[i] = p1

p_x = sum(x for x,y in besty)/len(besty)
p_y = sum(y for x,y in besty)/len(besty)
print(p_x * 10000, p_y*10000)
# 831316213