# f = open('1.txt')
# f.readline()
# points = [list(map(float, s.replace(",", ".").split())) for s in f]
# mn = 10**10
# cls = [[], []]
# for x, y in points:
#     if y > 0:
#         cls[0].append([x,y])
#     else:
#         cls[1].append([x, y])
# lytsii_sente = [[], []]
# for i in range(len(cls)):
#     mini = 10**10
#     for x_n, y_n in cls[i]:
#         sumi_rast =0
#         for x_t, y_t in cls[i]:
#             d1 = ((x_n - x_t) ** 2 + (y_n - y_t)** 2)**0.5
#             sumi_rast += d1
#         if sumi_rast < mini:
#             mini = sumi_rast
#             lytsii_sente[i] = [x_n, y_n]
# p_x = int((sum([x for x, y in lytsii_sente]) / len(lytsii_sente))* 10000)
# p_y = int((sum([y for x, y in lytsii_sente]) / len(lytsii_sente))* 10000)
# print(p_x, p_y)
# # 39966 10266
f = open('1.txt')
f.readline()
points = [list(map(float, s.replace(',', '.').split())) for s in f]
# print(points)
clasters = [[], []]
for x, y in points:
    if y > 0:
        clasters[0].append([x, y])
    else:
        clasters[1].append([x, y])
Nahe_lystii_centri = [[], []]
for i in range(len(clasters)):
    min_rastoin = 654654646546564
    for x_xentra, y_centra in clasters[i]:
        rastoin = 0
        for x_toshki, y_toshki in clasters[i]:
            R = ((x_xentra - x_toshki) ** 2 + (y_centra - y_toshki) ** 2) ** 0.5
            rastoin += R
        if rastoin < min_rastoin:
            min_rastoin = rastoin
            Nahe_lystii_centri[i] = [x_xentra, y_centra]
# print(Nahe_lystii_centri)
p_x = int(10000*(sum([x for x, y in Nahe_lystii_centri]) / len(Nahe_lystii_centri)))
p_y = int(10000*(sum([y for x, y in Nahe_lystii_centri]) / len(Nahe_lystii_centri)))
print(p_x, p_y)