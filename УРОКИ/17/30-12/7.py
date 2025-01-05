a = [int(s) for s in open('7.txt')]
res = []
for i in range(len(a) - 1):
    if str(len(str(a[i]))) == str(a[i])[0] and str(len(str(a[i  +1]))) == str(a[i +1])[0]:
        res.append(a[i] + a[i + 1])
print(len(res), min(res))