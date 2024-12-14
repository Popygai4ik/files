c= []
for n in range(1, 100000):
    n_b = bin(n)[2:]
    t = ''
    for k in n_b:
        if k == '0':
            t += "1"
        else:
            t += '1'

    res = int(t, 2)
    if (n - res) == 817:
        print(n)
        # c.append(n)

print(min(c))
# def R(n):
#
#     n2 = bin(n)[2:]
#
#     n2 = n2.replace('0', '2')
#
#     n2 = n2.replace('1', '0')
#
#     n2 = n2.replace('2', '0')
#
#     return int(n2, 2)
#
# for n in range(1, 10000):
#
#     if R(n) == 817:
#
#             print(R(n))