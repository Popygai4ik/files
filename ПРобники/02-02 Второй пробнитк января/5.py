res = []
for n in range(1000):
    bini = bin(n)[2:]
    if bini.count('1') % 2 == 0:
        bini = '10'+bini[2:] + '0'
    else:
        bini = '11' + bini[2:] + '1'
    R = int(bini, 2)
    print(n, R)
    if R < 235:
        res.append(n)
print(max(res))