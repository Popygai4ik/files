for n in range(0, 200):
    bn = bin(n)[2:]
    bn1 = bin(n)[2:]
    bn = str(bn) + str(bn[-1])
    if bn1.count('1') % 2 == 0:
        bn = str(bn) + '0'
    else:
        bn = str(bn) + '1'
    if bn.count('1') % 2 == 0:
        bn = str(bn) + '0'
    else:
        bn = str(bn) + '1'
    res = int(bn, 2)
    if res > 40:
        print(res)
        break
