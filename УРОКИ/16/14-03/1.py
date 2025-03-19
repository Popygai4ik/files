f = [0]*4000
for n in range(1,4000):
    if n == 1:
        f[n] = 1
    elif n > 1:
        f[n] = (2 * n - 2)* f[n - 1]
print(f[3029]/f[3027])