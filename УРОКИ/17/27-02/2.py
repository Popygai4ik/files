a = [int(i) for i in open('2.txt')]
res= []
maini = min(a)
for i in range(len(a)- 1):
    if (a[i])% 43 == maini or (a[i + 1])% 43 == maini:
        res.append(a[i]+a[i+1])
print(len(res), min(res))