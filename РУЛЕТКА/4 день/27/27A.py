import math
from turtle import done

from main import ris, ris2

f = open('27A.txt')
f.readline()
points = [list(map(float, s.replace(',', '.').split())) for s in f]
classters = [[],[]]
for x,y in points:
    if x > 0:
        classters[0].append([x,y])
    else:
        classters[1].append([x,y])
# eps = 100
# while points:
#     classters.append([points[0]])
#     del points[0]
#     for p1 in classters[-1]:
#         for p2 in points[:]:
#             if math.dist(p1,p2) < eps:
#                 classters[-1].append(p2)
#                 points.remove(p2)
best = [[] for i in range(len(classters))]
for i in range(len(classters)):
    mini = 10**10
    for p1 in classters[i]:
        R= 0
        for p2 in classters[i]:
            R += math.dist(p1,p2)
        if R < mini:
            mini = R
            best[i] = [p1[0],p1[1]]
ris(classters)
ris2(best)
done()
p_x = int((sum(x for x, y in best) / len(best))*10_000)
p_y = int((sum(y for x, y in best) / len(best))*10_000)
print(p_x, p_y)

#-185529 -270785