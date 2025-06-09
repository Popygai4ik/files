import math
from main import *
f = open('27A.txt')
f.readline()
points = [list(map(float,s.replace(',','.').split()))for s in f]
eps = 1
classters = []
while points:
    classters.append([points[0]])
    del points[0]
    for p1 in classters[-1]:
        for p2 in points[:]:
            if math.dist(p1,p2) < eps:
                classters[-1].append(p2)
                points.remove(p2)

antibesty = [[] for _ in range(len(classters))]
for i in range(len(classters)):
    maxa =0
    for p1 in classters[i]:
        r = 0
        for p2 in classters[i]:
            r += math.dist(p1,p2)
        if r > maxa:
            maxa = r
            antibesty[i] = p1
p_x = sum(x for x,y in antibesty)/len(antibesty)
p_y = sum(y for x,y in antibesty)/len(antibesty)
# print(p_x* 10000)
print((p_x * 10000) // 1,(p_y * 10000) // 1)
# ris(classters)
# ris2(antibesty)
# done()
# 3321225234
