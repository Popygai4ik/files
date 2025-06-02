f = open('edacffe2-f3c1-4f1e-9e8d-fc9e5b6a36ec_26.1.txt')
f.readline()
corgi = [int(s) for s in f]
corgi.sort(reverse=True)
res = []
res.append(corgi[0])
del corgi[0]
for cor in corgi:
    if abs(cor - res[-1]) >= 15:
        res.append(cor)
print(res[-1])
print(len(res))