def per(n):
    res = ''
    while n > 0:
        res += str(n % 4)
        n = n // 4
    return res[::-1]
for x in range(1,5870 + 1):
    n = 4**420+4**310+4**20-x
    r = per(n)
    if r.count('2') == 7:
        print(x,r)
