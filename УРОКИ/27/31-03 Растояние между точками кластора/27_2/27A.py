import math

from main import rs
from main import rs2
from turtle import *

f = open('27A.txt')
f.readline()
ponins = [list(map(float,s.replace(',','.').split()))for s in f]
k = 2
mos = [[],[],[]]
classters = [[]for _ in range(k)]
for x,y in ponins:
    if -1.8 < x < -0.2 and -1 < y < 2:
        classters[0].append([x,y])
    elif -0.8 < y <1.5 and -0.1 <x < 1.1:
        classters[1].append([x,y])
    else:
        mos[2].append([x,y])
min_d = 10**10
max_d = 0
for i in range(k):
    for p1 in classters[i]:
        for j in range(i+1,k):
            for p2 in classters[j]:
                max_d  =max(max_d,math.dist(p1,p2))
                min_d = min(min_d, math.dist(p1, p2))
print(int(max_d*10000),int(min_d*10000))
# 33592 8451
# rs(classters)
# rs2(bset)
# done()