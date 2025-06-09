import math

from main import *
f = open('27.1.В.txt')
f.readline()
points = [list(map(float, s.replace(',','.').split())) for s in f]
classters = []
eps = 1
while points:
    classters.append([points[0]])
    del points[0]
    for p1 in classters[-1]:
        for p2 in points[:]:
            if math.dist(p1,p2) <= eps:
                classters[-1].append(p2)
                points.remove(p2)
besty = [[] for _ in range(len(classters))]
for i in range(len(classters)):
    miiiii = 10001234234145134
    for p1 in classters[i]:
        r = 0
        for p2 in classters[i]:
            r += math.dist(p1,p2)
        if r < miiiii:
            miiiii = r
            besty[i] = p1
p_x = sum(x for x,y in besty)/len(besty)
p_y = sum(y for x,y in besty)/len(besty)
# 10776548961571513576
print(p_x*10000,p_y*10000)
ris(classters)
ris2(besty)
done()
