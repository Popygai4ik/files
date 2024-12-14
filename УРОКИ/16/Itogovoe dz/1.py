f = [0]* 5000
for n in range(0, 5000):
    if n == 1:
        f[n] = 1
    if n > 1:
        f[n] = (2*n-2)*f[n-1]
print(f[3029]/f[3027])