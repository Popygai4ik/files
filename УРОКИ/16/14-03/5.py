f = [0]*200
for n in range(0, 200):
    if n == 0:
        f[n] = 1
    elif n > 1 and n % 2 == 0:
        f[n] = 7 + int(3 * (f[n - 2]/2))
    elif n > 1 and n % 2!= 0:
        f[n] = 6*n + int((f[n -2] + f[n - 1] + 8)/5)
    elif n == 1:
        f[n] = 2
print(f[71])