import math
from turtle import *
def ris(a):
    tracer(0)
    screensize(2000,2000)
    penup()
    left(90)
    k = 30
    colors = ['red','black','pink','orange', 'blue']
    for i in range(len(a)):
        for x,y in a[i]:
            goto(x*k,y*k)
            dot(5,colors[i])
def ris2(a):
    tracer(0)
    screensize(2000,2000)
    penup()
    left(90)
    k = 30
    colors = ['blue','pink', 'black','red','orange']
    for i in range(len(a)):
        x,y = a[i]
        # print(i)
        goto(x * k, y * k)
        dot(10, colors[i])


f = open('27B.txt')
f.readline()
points = [list(map(float, s.replace(',','.').split()))for s in f ]
k = 4
clasters = [[] for _ in range(k)]
for x,y in  points:
    if y > 4:
        clasters[0].append([x,y])
    elif x > 2:
        clasters[1].append([x,y])
    elif x < -4:
        clasters[3].append([x,y])
    else:
        clasters[2].append([x,y])
#3715
# ris(clasters)
for i in clasters:
    print(len(i))
del clasters[clasters.index(max(clasters,key=len))]
print('------')
# for i in clasters:
#     print(len(i))
# for i in clasters:
#     print(len(i))
k = k -1
best = [[] for i in range(k)]
for i in range(k):
    min_r = 10**10
    for x_c, y_c in clasters[i]:
        R = 0
        for x_t,y_t in clasters[i]:
            R+= math.dist([x_t,y_t],[x_c,y_c])
        if R < min_r:
            min_r = R
            best[i] = [x_c,y_c]
p_x = int((sum(x for x,y in best) / k)*10000)
print(best)
p_y = int((sum(y for x,y in best) / k)*10000)
ris(clasters)
print(p_x,p_y)
ris2(best)
done()
#848528642494325939
