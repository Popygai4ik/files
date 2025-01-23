res = []
for n in range(1000):
    bini = bin(n)[2:]
    bini += bini[-1]
    if bini.count('1') % 2 == 0:
        bini += '0'
    else:
        bini += '1'
    if bini.count('1') % 2 == 0:
        bini += '0'
    else:
        bini += '1'
    r = int(bini, 2)
    if r > 177:
        res.append(n)
print(min(res))