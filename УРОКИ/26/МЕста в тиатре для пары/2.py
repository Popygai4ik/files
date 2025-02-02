f = open('2.txt')
n, m, k = map(int, f.readline().split())
mesta = [[] for i in range(k + 1)]
for s in f:
    ryad, plase = map(int, s.split())
    mesta[plase].append(ryad)
# print(mesta)
res = []
for i in range(1, len(mesta) - 1):
    mesta[i] = sorted([0] + mesta[i]+ [m + 1], reverse=True)
    for j in range(len(mesta[i])  - 1):
        up, down = mesta[i][j], mesta[i][j + 1]
        res.append([up - down - 1 - 1, up - 1])
res.sort(reverse=True)
print(res)