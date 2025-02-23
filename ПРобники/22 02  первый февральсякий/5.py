for n in range(2, 1000):
    bini = bin(n)[2:]
    bini += bini[1]
    if bini.count('1') % 2 == 0:
        bini += '1'
    else:
        bini += '0'
    if bini.count('1') % 2 == 0:
        bini += '1'
    else:
        bini += '0'
    r = int(bini, 2)
    print(n,r)