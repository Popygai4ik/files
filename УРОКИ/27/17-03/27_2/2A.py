import math
from turtle import *
def visila(clas):
    left(90)
    penup()
    screensize(2000, 2000)
    tracer(0)
    k = 50
    clo = ['green', 'black', 'red', 'blue']
    for gi in range(len(clas)):
        for x, y in clas[gi]:
            goto(x * k, y * k)
            dot(4, clo[gi])
f = open('27B.txt')
f.readline()
points = [list(map(float, s.replace(',', '.').split())) for s in f]
# print(points)
k = 3
eps = 0.25
claters = []
def visila2(best):
    left(90)
    penup()
    tracer(0)
    k = 50
    clo = ['red', 'blue', 'black']
    for i in range(len(best)):
        # print(best[i])
        x, y = best[i][0], best[i][1]
        goto(x * k, y * k)
        dot(10, clo[i])

while points:
    claters.append([points[0]])
    del points[0]
    for p1 in claters[-1]:
        for t1 in points[:]:
            if math.dist(p1, t1) < eps:
                claters[-1].append(t1)
                points.remove(t1)
    if len(claters[-1]) <= 5:
        del claters[-1]
# print(claters)
# visila(claters)
# done()
# print(claters)
best = [[] for i in range(k)]
for i in range(k):
    min_ras = 10**10
    for x_c, y_c in claters[i]:
        R = 0
        for x_t, y_t in claters[i]:
            R += math.dist([x_c, y_c], [x_t, y_t])
        if R < min_ras:
            min_ras = R
            best[i] = [x_c, y_c]
# print(best )
visila(claters)
# visila2(best)

p_x = int((sum(x for x, y in best)/len(best) * 10000))
p_y = int((sum(y for x, y in best)/len(best) * 10000))
print(p_x,p_y)
done()
#4150241042227589