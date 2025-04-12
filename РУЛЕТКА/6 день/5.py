f  = [0]*20000

for n in range(20000):
    if n < 5:
        f[n] = n
    elif n >= 5:
        f[n] = 2 * n * f[n - 4]
print((f[13768] - 9*f[13762])/ f[13758])
f = [0] * 20000

for n in range(20000):
    if n < 5:
        f[n] = n
    else:
        f[n] = 2 * n * f[n - 4]

result = (f[13768] - 9 * f[13762]) // f[13758]
print(result)
