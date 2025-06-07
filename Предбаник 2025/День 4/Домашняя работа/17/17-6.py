f = open('17.6.txt')
a = [int(x) for x in f]
maxi = max(x for x in a if x < 0 and abs(x) % 29 == 0)
res = []
for i in range(len(a) - 1):
    if (a[i] != a[i + 1]) and (abs(a[i + 1] - a[i] ) % abs(maxi) == 0):
        res.append(a[i + 1] +a[i])
print(len(res), max(res))