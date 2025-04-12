f = [0]*250
for n in range(250):
    if n < 100:
        f[n] = 1
    elif n > 200:
        f[n] = f[n - 2] + 3 * f[n - 1] + 9
    else:
        f[n] = -f[n - 5]
print(f[213])
