res = []
for n in range(1,1000):
    bini = bin(n)[2:]
    if sum(int(i) for i in str(bini)[-2:]) %  2 == 0:
        bini = bini + '100'
    else:
        bini = '10' + bini + '01'
    R = int(bini,2)
    if R > 472:
        res.append(R)
print(min(res))

