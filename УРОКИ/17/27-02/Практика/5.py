a = [int(i) for i in open('5.txt')]
mini = min(a)

res = []
for i in range(len(a)-1):
    if (a[i]% 176 == mini or a[i + 1]% 176 == mini):
        res.append(a[i]+a[i+1])
print(len(res),min(res))