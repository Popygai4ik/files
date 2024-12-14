c= []
for n in range(1010, 10000):
    n_b = bin(n)[2:]
    n_b = n_b[::-1]
    res = int(n_b, 2)
    if res == 109:
        c.append(n)

print(min(c))
