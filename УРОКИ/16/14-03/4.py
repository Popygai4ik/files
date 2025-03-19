f = [0]*3000

for n in range(1, 3000):
    if n == 1:
        f[n] = 1
    if n > 1:
        f[n] = n ** 2 *f[n - 1]
print((f[2024] + f[2023]) / f[2022])