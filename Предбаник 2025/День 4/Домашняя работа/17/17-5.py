f = open('17.5.txt')
a = [int(x) for x in f]
sumi = sum(x for x in a if x > 0)
res = []
for i in range(len(a) - 2):
    if max(a[i],a[i + 1], a[i + 2]) * min(a[i], a[i + 1], a[i + 2]) > sumi:
        res.append(a[i] + a[i + 1] + a[i + 2])
print(len(res), min(res))