from math import sqrt

a = [int(s) for s in open('6.txt')]
res = []
for i in range(len(a) - 1):
    y1 = a[i] + a[i + 1]
    if (sqrt(a[i]) % 1 == 0 or sqrt(a[i + 1]) % 1 == 0) and len(str(y1)) == 6:
        res.append(a[i] + a[i + 1])
print(len(res), max(res))