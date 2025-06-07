f = open('17.9.txt')
a = [int(x) for x in f]
res = []
maxi = max(x for x in a if abs(x) % 10 == 7)
for i in range(len(a) - 2):
    if (sorted(a[i:i+3])[-1]  * sorted(a[i:i+ 3])[1] > min(a[i], a[i + 1], a[i + 2]) * maxi):
        res.append(a[i] + a[i + 1] + a[i + 2])
print(len(res),min(res))