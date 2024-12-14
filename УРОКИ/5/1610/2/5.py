ans = []
for n in range(0, 1000):
    bn = bin(n)[2:]
    if bin(n)[2:].count('1') % 2 == 0:
        bn = bn + '0'
        bn = '10' + bn[2:]
    else:
        bn = bn  + '11'
        bn = '11' + bn[2:]
    res = int(bn, 2)
    if res < 99:
        ans.append(n)
print(max(ans))