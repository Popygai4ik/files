f = open('27B.txt')
f.readline()
from turtle import *
points = [list(map(float, s.replace(',', '.').split())) for s in f]
# print(points)
penup()
left(90)
tracer(0)
k =40
for x, y in points:
    setpos(x*k, y*k)
    dot()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x*k, y*k)
        if x == 0 or y == 0:
            dot(10, 'blue')
        else:
            dot()
# clasters = [[], [], []]
# for x, y in points:
#     if y< 4:
#         clasters[0].append([x, y])
#     elif x > 0.7 and y > 6:
#         clasters[2].append([x, y])
#     else:
#         clasters[1].append([x, y])
# Nahe_lystii_centri = [[], [], []]
# for i in range(len(clasters)):
#     min_rastoin = 654654646546564
#     for x_xentra, y_centra in clasters[i]:
#         rastoin = 0
#         for x_toshki, y_toshki in clasters[i]:
#             R = ((x_xentra - x_toshki) ** 2 + (y_centra - y_toshki) ** 2) ** 0.5
#             rastoin += R
#         if rastoin < min_rastoin:
#             min_rastoin = rastoin
#             Nahe_lystii_centri[i] = [x_xentra, y_centra]
# print(Nahe_lystii_centri)

# p_x = int(10000*(sum([x for x, y in Nahe_lystii_centri]) / len(Nahe_lystii_centri)))
# p_y = int(10000*(sum([y for x, y in Nahe_lystii_centri]) / len(Nahe_lystii_centri)))
# print(p_x, p_y)
goto(0.5504833199275398 * k,2.6606237952177576 * k)
dot(10,'green')
goto(-0.8831384039401575 * k,5.818087472256059 * k)
dot(10,'red')
goto(1.873426708787207 * k,7.507980569821834 * k)
dot(10,'blue')

# [[0.5504833199275398, 2.6606237952177576], [-0.8831384039401575, 5.818087472256059], [1.873426708787207, 7.507980569821834]]
done()
