ans = []
for n in range(0, 1000):
    bn = bin(n)[2:]
    if n%2== 0:
        bn = bn + bn[:2]
    else:
        bn = '1'+bn+'1'
    res = int(bn, 2)
    if res > 700:
        ans.append(res)
print(min(ans))