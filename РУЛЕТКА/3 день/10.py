a = [int(s) for s in open('10-17')]
res= []
e = min(a)
for i in range(len(a)-1):
    if (a[i] % 152 == e) or (a[i + 1] % 152 == e):
        res.append(a[i]+a[i+1])
print(len(res),max(res))