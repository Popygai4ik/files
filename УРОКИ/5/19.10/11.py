c= []
for n in range(1, 1000):
    n_b = bin(n)[2:]
    n_b1 = n_b + n_b[-1:]
    if (n_b.count('1')) % 2 == 0:
        n_b1 += '0'
    else:
        n_b1 += '1'
    if (n_b1.count('1')) % 2 == 0:
        n_b1 += '0'
    else:
        n_b1 += '1'
    res = int(n_b1, 2)
    if res > 82:
        c.append(res)

print(min(c))
