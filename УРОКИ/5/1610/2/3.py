ans = []
for n in range(0, 1000):
    bn = bin(n)[2:]
    bn += str(bin(bn.count('1') % 2)[2:])
    bn += str(bin(bn.count('1') % 2)[2:])
    res = int(bn, 2)
    if res > 720:
        ans.append(res)
print(min(ans))