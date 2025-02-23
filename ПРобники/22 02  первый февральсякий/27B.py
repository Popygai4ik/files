f = open('27B.txt')
# from turtle import *
f.readline()
ponts = [list(map(float, s.replace(',', '.').split())) for s in f]
# print(ponts)
# screensize(2000, 2000)
k = 100
clas = [[], [], []]
for x, y in ponts:
    if y > 1.9:
        clas[0].append([x,y])

    if y<0.2 and x > 3.7:
        clas[2].append([x, y])
    else:
        clas[1].append([x,y])
# # print(clas)
# tracer(0)
# color = ['blue', 'green', 'black']
# for i in range(3):
#     # print(i)
#
#     for x,y in clas[i]:
#         print(color[i])
#         setpos(x*k,y*k)
#         dot(4, color[i])
# done()
nahe = [[], [], []]
for i in range(len(clas)):
    min_rast = 1432341342341234
    for x_c, y_c in clas[i]:
        R = 0
        for x_t, y_t in clas[i]:
            r = ((x_c - x_t) ** 2 + (y_c - y_t)**2 )**0.5
            R += r
        if R < min_rast:
            min_rast = R
            nahe[i] = [x_c, y_c]
print(nahe)
p_x = int(10000*(sum([x for x,y in nahe])/len(nahe)))
p_y = int(10000*(sum([y for x,y in nahe])/len(nahe)))
print(p_x, p_y)
