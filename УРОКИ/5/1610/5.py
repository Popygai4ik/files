for n in range(0, 1000):
    bn = bin(n)[2:]
    bn1= bin(n)[2:]
    suma1 = sum(int(k) for k in bin(n)[2:])
    if suma1 % 2 == 0:
        delen = suma1 % 2
        bn = str(bn) + str(bin(delen)[2:])
    else:
        delen = suma1 % 2
        bn = str(bn) + str(bin(delen)[2:])
    suma2 = sum(int(k) for k in bin(int(bn))[2:])
    if suma2 % 2 == 0:
        delen = suma2 % 2
        bn = str(bn) + str(bin(delen)[2:])
    else:
        delen = suma2 % 2
        bn = str(bn) + str(bin(delen)[2:])
    res = int(bn, 2)
    if res > 630:
        print(n)
        break