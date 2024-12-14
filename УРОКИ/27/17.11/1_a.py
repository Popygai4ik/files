f = open('27A_1.txt')
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
print(Nahe_lystii_centri)
# p_x = int(10000*(sum([x for x, y in Nahe_lystii_centri]) / len(Nahe_lystii_centri)))
# p_y = int(10000*(sum([y for x, y in Nahe_lystii_centri]) / len(Nahe_lystii_centri)))
print(p_x, p_y)
# -16233 18943