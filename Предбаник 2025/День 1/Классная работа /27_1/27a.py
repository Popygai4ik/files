import math

from main import *
from turtle import *

f = open('27A.txt')
f.readline()
poits = [list(map(float,s.replace(',','.').split())) for s in f]
# print(poits)
classters = []
eps = 0.5
while poits:
    classters.append([poits[0]])
    del poits[0]
    for t1 in classters[-1]:
        for t2 in poits[:]:
            if math.dist(t1,t2)<eps:
                classters[-1].append(t2)
                poits.remove(t2)
best = [[] for i in range(len(classters))]
for i in range(len(classters)):
    miim = 100000
    for t1 in classters[i]:
        r = 0
        for t2 in classters[i]:
            r += math.dist(t2,t1)
        if r < miim:
            miim = r
            best[i] = t1
p_x = int((sum(x for x,y in best)/ len(best))*10000)
# 249 -15002
p_y = int((sum(y for x,y in best)/ len(best))*10000)
print(p_x,p_y)
ris(classters)
ris2(best)
done()