def koldel(n):
    res = []
    for i in range(1,n+1):
        if n % i ==0:
            res.append(i)
    return len(res)
it = []
for k in range(70000, 75001):
    # print(k)
    it.append([koldel(k), k])
it.sort(reverse=True)
print(it[:19])