def to4(n):
    r = ''
    while n > 0:
        r += str(n % 4)
        n //= 4
    return r[::-1]
c = []
for n in range(1, 10000):
    che = to4(n)

    if n % 4 == 0:
        che = che + che[-2:]
    else:
        che = che + to4((n % 4) * 2)
    r = int(che, 4)
    if r < 479:
        c.append(n)
print(c)