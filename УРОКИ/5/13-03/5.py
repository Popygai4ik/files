a = []
for n in range(1,1000):
    bini = bin(n)[2:]
    if n % 11 == 0:
        bini = bini+ '0'*bini.count('0')
    else:
        bini =  '1' * bini.count('1') + bini
    r = int(bini, 2)
    print(n,r)
    if r % 317 == 0:
        a.append(r)
print('OTV - ', min(a))