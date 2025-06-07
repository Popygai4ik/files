f = open('17.2.txt')
a = [int(x) for x in f]
minin = min(a)
res = []
for i in range(len(a) - 1):
    if (a[i] % 176 == minin) or (a[i + 1] % 176 == minin):
        res.append(a[i] + a[i + 1])
print(len(res), min(res))