import math

from main import rs
from main import rs2
from turtle import *

f = open('27B.txt')
f.readline()
ponins = [list(map(float,s.replace(',','.').split()))for s in f]
k = 3
classters = []
eps = 0.1
while ponins:
    classters.append([ponins[0]])
    del ponins[0]
    for p1 in classters[-1]:
        for p2 in ponins[:]:
            if math.dist(p1,p2) < eps:
                classters[-1].append(p2)
                ponins.remove(p2)
    if len(classters[-1]) <= 5:
        del classters[-1]

print(len(classters))
min_d = 10**10
max_d = 0
for i in range(k):
    for p1 in classters[i]:
        for j in range(i+1,k):

            for p2 in classters[j]:
                max_d  =max(max_d,math.dist(p1,p2))
                min_d = min(min_d, math.dist(p1, p2))
print(int(max_d*10000),int(min_d*10000))
# done()