c= []
for n in range(1, 1000):
    n_b = bin(n)[2:]
    if n % 2 == 0:
        n_b = n_b + bin(n_b.count('1'))[2:]
    else:
        n_b = '1' +n_b+'00'
    res = int(n_b, 2)
    if res > 843:
        c.append(n)

print(min(c))
