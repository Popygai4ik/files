import math
from turtle import *

f = open('27B.txt')
f.readline()
points = [list(map(float, s.replace(',', '.').split())) for s in f]
# print(points)
k = 3
klaster = [[] for i in range(k)]
for x, y, brigt in points:
    if y >0:
        klaster[0].append([x, y, brigt])
    elif y<0 and x > 0.4:
        klaster[2].append([x,y,brigt])
    else:
        klaster[1].append([x, y, brigt])
def sre(cls):
    s1 = sum([br for x,y,br in cls])
    return s1/len(cls)

def visila(clas):
    left(90)
    penup()
    tracer(0)
    k = 50
    clo = ['green', 'black', 'red', 'blue']
    for gi in range(len(clas)):
        for x, y, brig in clas[gi]:
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
        # x, y, b = best[i][0], best[i][1], best[i][2]
        x, y = best[i][0], best[i][1]

        goto(x * k, y * k)

        dot(10, clo[i])


# print(points)
visila(klaster)
# print(klaster)
best = [[] for i in range(k)]
best = [[1.7601308570569991, 1.461977482582558], [-1.0184262923422773, -1.3782777114609166], [1.7033816173408503, -2.0558201027130805]]

# for i in range(k):
#     mini= 100000000000000000
#     for C_X, Y_C,b in klaster[i]:
#         sumi_dist = 0
#         for x1, y1,b in klaster[i]:
#             sumi_dist += math.dist([C_X, Y_C], [x1,y1])
#         if sumi_dist < mini:
#             mini = sumi_dist
#             best[i] = [C_X, Y_C]

# print(best)
visila2(best)
P_yx = int(sum([x+y for x,y in best])*10000)
print(P_yx)
res = []
for popa in klaster:
    # print(popa)
    res.append(sre(popa))
print(int(sum(res)*1000))
done()
# [[1.7601308570569991, 1.461977482582558], [-1.0184262923422773, -1.3782777114609166], [1.7033816173408503, -2.0558201027130805]]