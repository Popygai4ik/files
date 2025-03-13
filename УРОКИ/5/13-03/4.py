c = []
for n in range(1,1000):
    bini = bin(n)[2:]
    bini = bini + str(bini.count('1')% 2 )
    bini = bini + str(bini.count('1') % 2)
    r = int(bini, 2)
    if r > 680:
        c.append(r)
print(min(c))