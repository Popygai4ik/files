c = 0
for n in range(700001,700001 + 1000):
    f = 0
    for i in range(2, n):
        if n % i == 0:
            f = n // i - i
            break
    if f != 0 and f %9 == 0:
        print(n, f)
        c += 1
    if c == 5:
        break