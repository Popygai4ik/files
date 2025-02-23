f = open('27A.txt')
f.readline()
ponts = [list(map(float, s.replace(',', '.').split())) for s in f]
# print(ponts)
clas = [[], []]
for x, y in ponts:
    if y > 0.9:
        clas[0].append([x,y])
    else:
        clas[1].append([x,y])
nahe = [[], []]
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
# print(nahe)
p_x = int(10000*(sum([x for x,y in nahe])/len(nahe)))
p_y = int(10000*(sum([y for x,y in nahe])/len(nahe)))
print(p_x, p_y)
