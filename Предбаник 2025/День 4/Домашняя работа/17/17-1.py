f = open('17_1.txt')
a = [int(x) for x in f ]
maxi = max(x for x in a if x % 3 == 0)
res = []
for i in range(len(a) - 1):
    if (a[i] + a[i + 1]) == maxi:
        res.append((a[i] + a[i + 1]) ** 2)
print(len(res),max(res))