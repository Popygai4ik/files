a = [int(s) for s in open('10-17')]
res = []

for i in range(len(a) - 1):
    if ((((len(str(a[i])) == 3) + (len(str(a[i + 1])) == 3)) == 1) and
            (sum(int(j) for j in str(a[i] + a[i + 1])) % 26 == 0)):
        res.append(a[i] + a[i + 1])
print(len(res), max(res))
