def per(n,base):
    res = 0
    n = str(n)
    for i in range(len(str(n)), 0, -1):
        print(f'{n[len(n)-i]}*{base}**{i-1}')
        res += eval(f'{n[len(n)-i]}*{base}**{i-1}')
    return res