c = []
def to3(n):
    res = ''
    while n > 0:
        res += str(n % 3)
        n = n // 3
    return res[::-1]
for n in range(1, 1000):
    t_n = to3(n)
    if n % 3 == 0:
        t_n += t_n[-3:]
    else:
        t_n += to3((n % 3)*3)
    R = int(t_n, 3)
    if R> 340:
        c.append(n)
print(min(c))