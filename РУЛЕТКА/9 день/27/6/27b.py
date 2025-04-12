import math
from main import  *
f = open('27BB.txt')
f.readline()
from turtle import *
points = [list(map(float, s.replace(',','.').split())) for s in f]
clasters = []
eps = 0.5
while points:
    clasters.append([points[0]])
    del points[0]
    for p1 in clasters[-1]:
        for p2 in points[:]:
            if math.dist(p1,p2) < eps:
                clasters[-1].append(p2)
                points.remove(p2)
best = [[] for i in range(len(clasters))]
for i in range(len(clasters)):
    mini = 10**10
    for t1 in clasters[i]:
        R= 0
        for t2 in clasters[i]:
            R += math.dist(t1,t2)
        if R < mini:
            mini = R
            best[i] = t1
p_x = abs(int((sum(x for x,y in best) / len(best))*100))
p_y = abs(int((sum(y for x,y in best) / len(best))*100))

ris(clasters)
ris2(best)
done()
print(p_x, p_y)
# 955 478 389 460