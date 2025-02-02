a = [int(i) for i in open('17.txt')]
sr_zn = sum(a)/len(a)
res =[]
for i in range(len(a)-1):
    if (a[i] > sr_zn or a[i + 1] >sr_zn) and (str(a[i]).count('3')>=2 or str(a[i + 1]).count('3')>=2):
        res.append(a[i] + a[i  + 1])

print(len(res), max(res))