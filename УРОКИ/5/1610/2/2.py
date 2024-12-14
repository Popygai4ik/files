ans = []
for n in range(0, 1000):
    bn = bin(n)[2:]
    bn += bn[-1:]
    if bin(n)[2:].count('1') % 2 == 0:
        bn = bn + '0'
    else:
        bn = bn  + '1'
    if bn.count('1')% 2 == 0:
        bn = bn + '0'
    else:
        bn = bn + '1'
    res = int(bn, 2)
    if res > 144:
        ans.append(n)
print(min(ans))