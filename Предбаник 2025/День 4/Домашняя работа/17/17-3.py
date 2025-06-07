f = open('17.3.txt')
res = []
a = [int(x) for x in f]
for i in range(len(a) - 1):
    if (abs(a[i]) % 10 == abs(a[i + 1]) % 10) and ((abs(a[i]) % 10 ) % 2 == 0):
        res.append(abs(a[i]*a[i + 1]))
print(len(res),max(res))
