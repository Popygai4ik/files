f = [0]*4000
for n in range(1, 4000):
    if n ==1:
        f[n] = 1
    elif n > 1:
        f[n] = n * f[n-1]*2
print((f[2025]//32 - f[2024]) / f[2023])
