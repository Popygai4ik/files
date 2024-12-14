c= []
for n in range(1, 1000):
    n_b = bin(n)[2:]
    if n % 5 == 0:
        n_b = n_b + n_b[-3:]
    else:
        n_b = n_b + bin((n % 5) * 5)[2:]
    res = int(n_b, 2)
    if res > 150:
        c.append(n)

print(min(c))
