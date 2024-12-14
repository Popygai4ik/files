c = 0
for n in range(600_001, 600_001 + 1000):
    for i in range(8, n):
        if i % 10 == 7 and n % i == 0:
            print(n, i)
            c += 1
            break
    if c == 5:
        break