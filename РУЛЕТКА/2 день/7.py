f = [0] * 11000
for n in range(11000):
    if n == 0:
        f[n] = 0
    elif n > 0 and n % 2 == 0:
        print(n)
        f[n] = f[n // 2]
    elif n % 2 != 0:
        f[n] = 3 + f[n - 1]
c = 0
for sh in range(265, 10000 + 1):
    if f[sh] % 3 == 0 and str(f[sh])[-1] != '3':
        c += 1
print(c)
