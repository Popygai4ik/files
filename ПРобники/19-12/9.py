c= 0
f = open('9.txt')
for s in f:
    data = s.split()
    if len(set(data)) != 4:
        continue
    a = []
    for j in data:
        a.append([j, data.count(j)])
    # print(a)
    s_p = 0
    s_n = 0
    for shuslo, por in a:
        if por > 1:
            print(shuslo)
            s_p += int(shuslo)
        else:
            s_n += int(shuslo)
    if s_p > s_n:
        c+= 1
print(c)