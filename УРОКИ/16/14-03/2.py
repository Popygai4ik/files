f = [0]*3500

for n in range(3000, 0, -1):
    if n >= 2025:
        f[n] = n
    elif n < 2025:
        f[n] = (n // 2) + f[n + 3]

print(f[2020] - f[2023])
