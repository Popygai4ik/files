a = [int(i) for i in open('3.txt')]
res = []
for i in range(len(a)-2):
    su = a[i]+a[i+1]+a[i+2]
    sr = su//3
    if sr %  6 == 0:
        if (a[i]% 5 == 0 or a[i] % 4 == 0) and \
            (a[i+1] % 5 == 0 or a[i+1] % 4 == 0)\
            and (a[i+2]% 5 == 0 or a[i+2] % 4 == 0):
            res.append(su)
print(len(res),min(res))