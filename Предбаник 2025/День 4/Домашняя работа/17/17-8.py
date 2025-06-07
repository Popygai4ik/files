f = open('17.8.txt')
a = [int(x) for x in f]
res = []

maxi = max(x for x in a if x % 100 == 11)
for i in range(len(a) - 1):
    if (oct(a[i])[-1] == oct(a[i + 1])[-1]) and ((a[i] % 5 == 0 and a[i + 1] % 7 == 0  and a[i] % 35 != 0 and a[i + 1] % 35 != 0) or(a[i + 1] % 5 == 0 and a[i ] % 7 == 0  and a[i] % 35 != 0 and a[i + 1] % 35 != 0) ) and ((a[i] ** 2 + a[i + 1] ** 2) <= maxi ** 2):
        res.append(a[i] + a[i + 1])
print(len(res), min(res))