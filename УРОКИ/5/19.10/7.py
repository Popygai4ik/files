c= []
for n in range(1, 1000):
    n_b = bin(n)[2:]
    if sum(map(int, str(n))) % 2 == 0:
        n_b = n_b + '0'
    else:
        n_b = n_b + '1'
    n1 = int(n_b, 2)
    if sum(map(int, str(n1))) % 2 == 0:
        n_b = n_b + '0'
    else:
        n_b = n_b + '1'
    n2 = int(n_b, 2)
    if sum(map(int, str(n2))) % 2 == 0:
        n_b = n_b + '0'
    else:
        n_b = n_b + '1'
    res = int(n_b, 2)
    if res > 522:
        c.append(res)

print(min(c))
