for n in range(0, 1000):
    bn = bin(n)[2:]
    if n % 2 == 0:
        bn = str(bn) + '01'
    else:
        bn = str(bn) + '10'
    res = int(bn, 2)
    if res > 101:
        print(res)