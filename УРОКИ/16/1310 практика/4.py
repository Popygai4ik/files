f = [0]*401
for n in range(1, 401):
    if n <= 4:
        f[n] = n
    if n % 2 == 0 and n > 4:
        f[n] = n + 4* f[n - 1]
    if n % 2 != 0 and n > 4:
        f[n] = 2 * n*n*n + f[n - 1]
c = 0
for i in f[1:]:
    if i % 8 == 0:
        c+=1
print(c)