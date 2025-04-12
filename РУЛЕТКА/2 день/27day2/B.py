import math

f = open('27B.txt')
from main import ris,ris2
from turtle import *
f.readline()
points = [list(map(float, s.replace(',','.').split())) for  s in f]
# print(points)
k = 5
eps = 0.2
classters = []
while points:
    classters.append([points[0]])
    del points[0]
    for p1 in classters[-1]:
        for p2 in points[:]:
            if math.dist(p1,p2) < eps:
                classters[-1].append(p2)
                points.remove(p2)

best = [[]for i in range(k)]
for i in range(k):
    mini = 10**10
    for p1 in classters[i]:
        R = 0
        for p2 in classters[i]:
            R += math.dist(p1,p2)
        if R < mini:
            mini = R
            best[i] = [p1[0],p1[1]]
p_x=int((sum(x for x,y in best)/len(best)) * 10000)
p_y=int((sum(y for x,y in best)/len(best)) * 10000)
print(p_x, p_y)
# -11985-4477-7695-3049
ris(classters)
ris2(best)
done()