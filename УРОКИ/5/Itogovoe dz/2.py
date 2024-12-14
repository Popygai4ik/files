c = []
for n in range(1, 1000):
    b_n = bin(n)[2:]
    if n % 2 ==0:
        b_n = '1'+b_n+'10'
    else:
        b_n = '10'+b_n
    R = int(b_n, 2)
    if R > 697:
        c.append(n)
print(min(c))