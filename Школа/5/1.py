def f(n):
    bini = bin(n)[2:]
    sum = bini.count('1')
    if sum % 2 == 0:
        bini = '10' + bini[2:] + '0'
    else:
        bini = '11' + bini[2:] + '1'


    r = int(bini, 2)
    return r

for i in range(1000):
    if f(i) > 35:
        print(i)
