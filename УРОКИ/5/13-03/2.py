for n in range(1,1000):
    bini = bin(n)[2:]
    if bini.count('1')% 2 == 0:
        bini = bini + '10'
        bini = '10'+bini[2:]
    else:
        bini = bini + '01'
        bini = '11' + bini[2:]
    r = int(bini, 2)
    if r <= 390:
        print(n)