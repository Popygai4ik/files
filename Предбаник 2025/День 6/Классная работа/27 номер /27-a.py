import math
from main import *
f= open('27A.txt')
points = [list(map(float, s.split())) for s in f]
# print(points)
classters = []
eps = 0.5
while points:
    classters.append([points[0]])
    del points[0]
    for p1 in classters[-1]:
        for p2 in points[:]:
            if math.dist(p1, p2) < eps:
                classters[-1].append(p2)
                points.remove(p2)
ani = [[] for _ in range(len(classters))]
besty =[[] for _ in range(len(classters))]
for i in range(len(classters)):
    minu = 10**10
    maxi = 0
    for p1 in classters[i]:
        r = 0
        for p2 in classters[i]:
            r += math.dist(p1,p2)
        if r < minu:
            minu = r
            besty[i] = p1
        if r > maxi:
            maxi = r
            ani[i] = p1
p_x = sum(x for x,y in besty)/len(besty)
s_y = sum(y for x,y in ani)/len(ani)
print(int(p_x* 10000),int(s_y * 10000))
# 95064 126836
# ris(classters)
# ris2(besty)
# ris2(ani)
# done()