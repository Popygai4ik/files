f = [0]*500
for n in range(1,500):
    if n <= 19:
        f[n] = n*n*n + 22
    elif n > 19 and n % 3 == 0:
        f[n] = f[n - 4] + f[n - 8]
    elif n > 19 and n % 3 != 0:
        f[n] = f[n - 9] + n + 7
c = 0
for i in range(1,101):
    if sum(str(f[i]).count(s) for s in str(f[i]) if s in '13579') == 0:
        c += 1
print(c)
