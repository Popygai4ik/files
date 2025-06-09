import math
from main import *
f = open('27B.txt')
f.readline()
points = [list(map(float, s.replace(',','.').split()))for s in f]
classters = []
eps = 0.5
while points:
    classters.append([points[0]])
    del points[0]
    for p1 in classters[-1]:
        for p2 in points[:]:
            if math.dist(p1,p2) < eps:
                classters[-1].append(p2)
                points.remove(p2)
    if len(classters[-1]) <= 3:
        del classters[-1]

min_d = 100134329549345823045283858235
masha = 0
for i in range(len(classters)):
    for p1 in classters[i]:
        for j in range(i + 1, len(classters)):
            for p2 in classters[j]:
                masha = max(masha,math.dist(p1,p2))
                min_d = min(min_d,math.dist(p1,p2))
print(min_d*10000, masha*10000)
# 248646132215882101654
# print(len(classters))
ris(classters)
done()