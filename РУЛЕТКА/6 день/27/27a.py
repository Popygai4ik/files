import math

f= open('27A.txt')
from main import *
from turtle import *
f.readline()
points = [list(map(float,s.replace(',','.').split())) for s in f]
eps = 0.25
claters = []
while points:
    claters.append([points[0]])
    del points[0]
    for p1 in claters[-1]:
        for p2 in points[:]:
            if math.dist(p1,p2) < eps:
                claters[-1].append(p2)
                points.remove(p2)
    if len(claters[-1])<=10:
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

# Суммарная плотность
density_sum = sum(len(cluster) / 20 for cluster in claters)
for i in range(2):
    print(len(claters[i]))
# Финальный ответ
print(f"{int((px + py) * 10000)}{int(density_sum * 1000)}")

#-291842150
import math


def centroid(cluster):

    c = []

    for x1, y1 in cluster:

        c += [[sum(math.dist((x1, y1), (x2, y2)) for x2, y2 in cluster), (x1, y1)]]

    return min(c)[1]



f = open('27A.txt')

f.readline()

points = [list(map(float, s.replace(",", ".").split())) for s in f]

clusters, epsilon = [], 0.25

while points:

    clusters.append([points[0]])

    del points[0]

    for p1 in clusters[-1]:

        for p2 in points[:]:

            if math.dist(p1, p2) < epsilon:

                clusters[-1].append(p2)

                points.remove(p2)

    if len(clusters[-1]) <= 10:

        del clusters[-1]



best_centroids = [[] for i in range (len(clusters))]

for i in range (len(clusters)):

    min_dist = 10**10

    for x1, y1 in clusters[i]:

        dist = 0

        for x2, y2 in clusters[i]:

            euclidian_dist = math.dist([x1, y1], [x2, y2])

            dist += euclidian_dist

        if dist < min_dist:

            min_dist = dist

            best_centroids[i] = [x1, y1]




P_x = sum([x for x, y in best_centroids]) / len(clusters)

P_y = sum([y for x, y in best_centroids]) / len(clusters)
print()
P_s = sum([len(cluster) / (4 * 5) for cluster in clusters])

for i in range(2):
    print(len(clusters[i]))

print(int((P_x + P_y) * 10000), int(P_s * 1000))