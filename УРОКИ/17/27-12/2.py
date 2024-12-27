a = [int(i) for i in open('2.txt')]
res = []
for i in range(len(a) - 1):
    if a[i]> 500 or a[i + 1] > 500:
        res.append(a[i] ** 2 + a[i + 1] ** 2)
print(len(res), max(res ))