f = open('t')
f.readline()
res_do = 0
a = list(reversed(sorted(int(i) for i in f)))
for i in range(len(a)):
    if (i + 1) % 3 != 0:
        res_do += a[i]
res_pos = a[:]
for i in range(4):
    if (i + 1) % 3 == 0:
        if res_pos[i] >= 50:
            res_pos[i] = 0
    else:
        if res_pos[i] <= 50:
            pass
        else:
            res_pos[i] = 0
print(sum(res_pos))
print(sum(res_pos), res_do)
# 4975743 3317498
