f =[0]*100
for n in range(1, 100):
    if n == 1:
        f[n] = 2
    if n == 2:
        f[n] = 3
    if n % 2 != 0 and n > 2:
        f[n] = int((((f[n-2]) + f[n-2])) / 7)
    if n % 2 == 0 and n > 2:
        f[n] = 7 * n - int(f[n -1] / 2 + 5)
print(f[40])