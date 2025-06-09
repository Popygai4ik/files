import math
from main import *
f = open('27B.txt')
f.readline()
points = [list(map(float,s.replace(',','.').split())) for s in f]
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
    if len(classters[-1]) < 5:
        del classters[-1]
besty = [[] for _ in range(len(classters))]
for i in range(len(classters)):
    mwdimsidfi = 123123123
    for p1 in classters[i]:
        r = 0
        for p2 in classters[i]:
            r += math.dist(p1,p2)
        if r < mwdimsidfi:
            mwdimsidfi = r
            besty[i] = p1

p_x = sum(x for x,y in besty)/len(besty)
p_y = sum(y for x,y in besty)/len(besty)
print(p_x*10000,p_y*10000)
# 41502410342227589
ris(classters)
ris2(besty)
done()