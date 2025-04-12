import math

f= open('27B.txt')
from main import *
from turtle import *
f.readline()
points = [list(map(float,s.replace(',','.').split())) for s in f]
eps = 0.5
claters = []
while points:
    claters.append([points[0]])
    del points[0]
    for p1 in claters[-1]:
        for p2 in points[:]:
            if math.dist(p1,p2) < eps:
                claters[-1].append(p2)
                points.remove(p2)
    if len(claters[-1])<10:
        del claters[-1]

best = [[] for i in range(len(claters))]
for i in range(len(claters)):
    mini = 10**10
    for t1 in claters[i]:
        R = 0
        for t2 in claters[i]:
            R += math.dist(t1,t2)

        if R < mini:
            mini = R
            best[i] = [t1[0], t1[1]]
px = sum(x for x, y in best) / len(best)
py = sum(y for x, y in best) / len(best)
ris(claters)
ris2(best)
# Суммарная плотность
density_sum = sum(len(cluster) / 20 for cluster in claters)

# Финальный ответ
print(f"{int((px + py) * 10000)}{int(density_sum * 1000)}")
p_x = (sum(x for x, y in best)/ len(best))
p_y = (sum(y for x, y in best)/ len(best))
print((p_y + p_x) * 10000)
s = 0
for i in range(len(claters)):
    s += len(claters[i]) / 20
print(s*1000)
done()
#-29184215019502488849