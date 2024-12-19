f = open('27B.txt')
f.readline()
point = [list(map(float, s.replace(',', '.').split())) for s in f]
# print(point)
cent = [[], [], []]
for x, y in point:
    if y < 6:
        cent[0].append([x, y])
    elif y > 6 and x < -4:
        cent[1].append([x, y])
    else:
        cent[2].append([x, y])
lytsi = [[], [], []]
for i in range(len(cent)):
    min_r = 10000000000000
    for x_cenr, y_cent in cent[i]:
        r = 0
        for x_t, y_t in cent[i]:
            R = ((x_cenr - x_t) **2 + (y_cent - y_t) ** 2) ** 0.5
            r += R
        if r < min_r:
            min_r = r
            lytsi[i] = [x_cenr, y_cent]
print(lytsi)
px = int(10000*(sum(x for x, y in lytsi))/len(lytsi))
py = int(10000*(sum(y for x, y in lytsi))/len(lytsi))
print(px, py)
# -56308 66238