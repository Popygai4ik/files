a = [int(i) for i in open('6.txt')]
mini = max(i for i in a if i % 3 == 0)
print(mini)
res = []
for i in range(len(a)-1):
    if (a[i]+a[i+1]) == mini:
        res.append((a[i]+a[i+1])**2)
print(len(res),max(res))