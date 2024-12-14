c= []
for n in range(1, 1000):
    n1 = (n - (n % 8))



    n_b = bin(n1)[2:]
    n_b += str((n_b.count('1')% 2))
    n_b += str((n_b.count('1') % 2))
    res = int(n_b, 2)
    if res<= 86:
        c.append(n)

print(bin(max(c)))
