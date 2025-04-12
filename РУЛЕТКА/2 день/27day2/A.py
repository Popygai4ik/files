import math

f = open('27A.txt')
from main import ris,ris2
from turtle import *
f.readline()
points = [list(map(float, s.replace(',','.').split())) for  s in f]
# print(points)
k = 3
classters = [[]for i in range(k)]
for x, y in points:
    if y > 1.5:
        classters[0].append([x,y])
    elif y < -2: classters[1].append([x,y])
    else: classters[-1].append([x,y])
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