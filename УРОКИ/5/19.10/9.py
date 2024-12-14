def to3(n):
    res = ''
    while n >0:
        res += str(n% 3)
        n = n // 3
    return res[::-1]
c= []
for n in range(1, 1000):
    n_b = to3(n)
    if n % 3 == 0:
        n_b =  n_b[:2] + n_b
    else:
        n_b = n_b + to3((n % 3) * 2)
    res = int(n_b, 3)
    if res > 455:
        c.append(n)

print(min(c))
