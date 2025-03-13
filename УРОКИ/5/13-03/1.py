for n in range(1,1000):
    bini = bin(n)[2:]
    if n % 2 == 0:
        bini = '1' + bini+ '10'
    else:
        bini = '10'+ bini
    r = int(bini, 2)
    if r > 697:
        print(n)