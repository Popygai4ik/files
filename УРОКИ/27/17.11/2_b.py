f = open('27B_2.txt')
f.readline()
points = [list(map(float, s.replace(',', '.').split())) for s in f]
lutsii_centrii = [[], [], []]
singylar = [[], [], []]
for x, y in points:
    if x < -2:
        singylar[0].append([x, y])
    elif y > 2:
        singylar[2].append([x, y])
    else:
        singylar[1].append([x, y])
for i in range(len(singylar)):
    mini = 1342174565741674551
    for x_cen, y_cen in singylar[i]:
        rast = 0
        for x_tosh, y_tosh in singylar[i]:
            d1 = ((x_cen - x_tosh) ** 2 + (y_cen - y_tosh) ** 2) ** 0.5
            rast += d1
        if rast < mini:
            mini = rast
            lutsii_centrii[i] = [x_cen, y_cen]
print(lutsii_centrii)
px = int(10000*(sum([x for x, y in lutsii_centrii]) / len(lutsii_centrii)))
py = int(10000*(sum([y for x, y in lutsii_centrii]) / len(lutsii_centrii)))
print(px, py)