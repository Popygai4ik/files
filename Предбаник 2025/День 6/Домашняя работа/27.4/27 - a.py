import math
from  main import *
f = open('27A.txt')
f.readline()
points = [list(map(float,s.replace(',','.').split())) for s in f]
eps = 0.25
classters  = []
while points:
    classters.append([points[0]])
    del points[0]
    for p1 in classters[-1]:
        for p2 in points[:]:
            if math.dist(p1, p2) < eps:
                classters[-1].append(p2)
                points.remove(p2)
    if len(classters[-1]) < 10:
        del classters[-1]

besty = [[] for _ in range(len(classters))]
for i in range(len(classters)):
    mini = 123123123123
    for p1 in classters[i]:
        r = 0
        for p2 in classters[i]:
            r += math.dist(p1,p2)
        if r < mini:
            mini = r
            besty[i] = p1
p_x = sum(x for x,y in besty)/len(besty)
p_y = sum(y for x,y in besty)/len(besty)
p_s = sum((len(claster)/16) for claster in classters)
print((p_x + p_y)* 10000, p_s*1000)
ris(classters)
# 28945250
ris2(besty)
done()