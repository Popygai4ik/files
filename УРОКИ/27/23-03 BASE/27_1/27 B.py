from turtle import *
import math
def ris(a):
    tracer(0)
    screensize(2000,2000)
    penup()
    left(90)
    k = 50
    colors = ['red','black','pink','orange']
    for i in range(len(a)):
        for x,y in a[i]:
            goto(x*k,y*k)
            dot(5,colors[i])
def ris2(a):
    tracer(0)
    screensize(2000,2000)
    penup()
    left(90)
    k = 50
    colors = ['pink','orange', 'black']
    for i in range(len(a)):
        x,y = a[i]
        goto(x * k, y * k)
        dot(10, colors[i])

f = open('27B.txt')
f.readline()
points = [list(map(float,s.replace(',','.').split()))for s in f]
k = 3
clasters = [[] for _ in range(k)]
for x,y in points:
    if x > 2: clasters[0].append([x,y])
    elif x < 1 and y > -1:
        clasters[2].append([x, y])
    else: clasters[1].append([x,y])
best = [[] for _ in range(k)]
for i in range(k):
    min_c = 10**10
    for x_c, y_c in clasters[i]:
        R = 0
        for x_t,y_t in clasters[i]:
            R += math.dist([x_t,y_t], [x_c,y_c])
        if R < min_c:
            min_c = R
            best[i] = [x_c,y_c]
print(best)

p_x = int((sum(x for x, y in best)/ len(best))*10000)
p_y = int((sum(y for x, y in best)/ len(best))*10000)
ris(clasters)
print(p_x,p_y)
ris2(best)
done()