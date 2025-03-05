a = [int(i) for i in open('5.txt')]
res = []
for i in range(len(a)-1):
    su = a[i]+a[i+1]
    if (a[i]**2 +a[i+1]**2)% 2 != 0 and (a[i]**2 +a[i+1]**2) > 100:
        res.append([su, a[i], a[i+1]])
print(len(res), min(res))
