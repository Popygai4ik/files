c = []
for n in range(1, 1000):
    n_b = bin(n)[2:]
    n_b = n_b + n_b[-1:]
    if (bin(n)[2:].count('1') % 2 == 0):
        n_b+= '0'
    else:
        n_b += '1'
    if (n_b.count('1') % 2 == 0):
        n_b+= '1'
    else:
        n_b += '0'
    res = int(n_b, 2)
    if res>55:
        c.append(n)
print(min(c))