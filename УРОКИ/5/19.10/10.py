def to4(n):
    res = ''
    while n >0:
        res += str(n% 4)
        n = n // 4
    return res[::-1]
c= []
for n in range(1, 1000):
    n_b = to4(n)
    if n % 3 == 0:
        n_b = n_b + n_b[-3:]
    else:
        n_b = to4((n % 3) * 4) + n_b
    res = int(n_b, 4)
    if res < 1166:
        c.append(n)

print(max(c))
