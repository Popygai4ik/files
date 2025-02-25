import math
from turtle import *
f = open('27A.txt')
f.readline()
points = [list(map(float, s.replace(',', '.').split()))for s in f]
clusters = []
eps = 0.5
def visila(clas):
    left(90)
    penup()
    tracer(0)
    k = 50
    clo = ['green', 'black', 'red', 'blue']
    for gi in range(len(clas)):
        for x, y in clas[gi]:
            goto(x * k, y * k)
            dot(4, clo[gi])
def visila2(best):
    left(90)
    penup()
    tracer(0)
    k = 50
    clo = ['red', 'blue', 'black']
    for i in range(len(best)):
        # print(best[i])
        x, y= best[i][0], best[i][1]
        goto(x * k, y * k)
        dot(10, clo[i])
while points:
    clusters.append([points[0]])
    del points[0]
    for t1 in clusters[-1]:
        for t2 in points[:]:
            if math.dist(t1, t2) < eps:
                clusters[-1].append(t2)
                points.remove(t2)
    if len(clusters[-1])<= 10:
        del clusters[-1]
best = [[] for i in range(len(clusters))]
for i in range(len(clusters)):
    min_d = 68798779879878
    for x_c,y_c in clusters[i]:
        R = 0
        for x_t,y_t in clusters[i]:
            R+= math.dist([x_c,y_c],[x_t,y_t])
        if R < min_d:
            min_d = R
            best[i] = [x_c,y_c]

p_x = sum([x for x, y in best])/len(best)

p_y = sum([y for x, y in best])/len(best)
y1 = int((p_x+p_y)*10000)
p_s = int(sum([len(cl)/16 for cl in clusters])*1000)
print(y1, p_s)
# 28945 61375