def tre(n):
    res = ''
    while n > 0:
        res += str(n % 3)
        n = n // 3
    return res[::-1]

c = []
for n in range(5001,10000):
    bini = bin(n)[2:]
    tri = tre(n)
    if int(tri[0]) % 2 != 0:
        bini = bini + '00'
        bini = '110' + bini[2:]
    elif int(tri[1]) % 2 == 0 :
        bini ='101' + bini
        bini = bini[:-2] + '1' + bini[-1]
    else:
        bini = '100' + bini
        bini = bini[:1] + '0' + bini[2:]
    R = int(bini,2)
    c.append(R)
print(min(c))
