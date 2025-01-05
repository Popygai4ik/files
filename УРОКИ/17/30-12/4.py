a = [int(s) for s in open('4.txt')]
mini = min(x for x in a if len(str(abs(x))) == 2)
# print(mini)
res =[]
for i in range(len(a) - 1):
    if (len(str(a[i])) == 2 and len(str(a[i  + 1])) == 2) and (a[i] + a[i  + 1]) % mini == 0:
        res.append(a[i]  +a[ i +1])
print(len(res), max(res))