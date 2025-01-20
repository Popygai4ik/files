for n in range(10001, 3, -1):
    s = '7'+'8'*n
    while '788' in s or '988' in s or '798' in s:
        if '788' in s:
            s = s.replace('788', '79', 1)
        if '988' in s:
            s = s.replace('988', '78', 1)
        if '798' in s:
            s = s.replace('798', '98', 1)
    su = sum(int(i) for i in str(s))
    if su == 17:
        print(s, su, n)