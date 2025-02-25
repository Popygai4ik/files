import math
from turtle import *
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
f= open('27A.txt')
f.readline()
points = [list(map(float, s.replace(',', '.').split())) for s in f]
clusters = []
eps = 0.5
while points:
    clusters.append([points[0]])
    del points[0]
    for toshka_1 in clusters[-1]:
        for toshka_2 in points[:]:
            if math.dist(toshka_1, toshka_2) < eps:
                clusters[-1].append(toshka_2)
                points.remove(toshka_2)
# visila(clusters)
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

best = [[]for _ in range(len(clusters))]
for i in range(len(clusters)):
    main_dis = 100000000000000000
    for x_c, y_c in clusters[i]:
        R = 0
        for x_t, y_t in clusters[i]:
            R+= math.dist([x_c, y_c], [x_t, y_t])
        if R < main_dis:
            main_dis = R
            best[i] = [x_c, y_c]
# visila2(best)
# done()
p_x = int((sum(x for x, y in best)/len(best) * 10000))

p_y = int((sum(y for x, y in best)/len(best) * 10000))
print(p_x, p_y)
# 8445 14977