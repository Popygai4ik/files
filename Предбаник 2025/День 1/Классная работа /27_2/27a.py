import math

from main import *
from turtle import *

f = open('27A.txt')
f.readline()
points = [list(map(float,s.replace(',','.').split())) for s in f]
# print(points)
k = 2
classters = [[] for i in range(k)]
for x,y in points:
    if y>1:
        classters[0].append([x,y])
    else:
        classters[1].append([x,y])
best = [[] for i in range(len(classters))]
for i in range(len(classters)):
    mimi = 10*12312312312
    for t1 in classters[i]:
        r = 0
        for t2 in classters[i]:
            r += math.dist(t1,t2)
        if r < mimi:
            mimi = r
            best[i] = t1
p_x = int((sum(x for x,y in best)/len(best))*10000)
p_y = int((sum(y for x,y in best)/len(best))*10000)
print(p_x,p_y) #16845 6643
ris(classters)
ris2(best)
done()