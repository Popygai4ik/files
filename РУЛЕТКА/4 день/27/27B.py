import math
from turtle import done

from main import ris, ris2

f = open('27B.txt')
f.readline()
points = [list(map(float, s.replace(',', '.').split())) for s in f]
classters = [[], [], []]
for x, y in points:
    if y > 86.5:
        classters[0].append([x,y])
    elif y < 84:
        classters[1].append([x,y])
    else:
        classters[2].append([x,y])
# eps = 0.7
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

p_x = int((sum(x for x, y in best) / len(best))*10_000)
p_y = int((sum(y for x, y in best) / len(best))*10_000)
print(p_x, p_y)
done()
#-185529 -270785 232218 853474