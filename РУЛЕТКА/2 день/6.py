f = [0]*3000
for n in range(0,3000):
    if n <= 3:
        f[n] = 1
    elif n > 3:
        print(n)
        f[n] = (n + 3)*f[n - 2]
print(f[2030]/f[2024])