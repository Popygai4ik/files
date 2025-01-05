a = [int(s) for s in open('3.txt')]
mini = min(a)
res = []
for i in range(len(a) - 1):
    if (a[i] %  123 == mini) or (a[i  + 1] %  123 == mini):
        res.append(a[i] + a[i + 1])
print(len(res), max(res))