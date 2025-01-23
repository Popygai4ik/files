def per(n):
    af = '0123456789AB'
    res = ''
    while n > 0:
        res += af[n%12]
        n = n // 12
    return res[::-1]

for n in range(4, 10000):
    s = '0' + '6' * n

    while '06' in s or '566' in s or '666' in s:

        if '06' in s:
            s = s.replace('06', '6', 1)

        if '566' in s:
            s = s.replace('566', '60', 1)

        if '666' in s:
            s = s.replace('666', '5', 1)
    if '3' in per(sum(int(i) for i in s)):
        print(per(int(s)))
        print(n)
        break