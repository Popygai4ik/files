c= []
for n in range(1, 1000):
    n_b = bin(n)[2:]
    t = ''
    for k in n_b:
        if k == '0':
            t += "10"
        else:
            t += '11'

    res = int(t, 2)
    if res<= 777 and res % 2 == 0:
        c.append(res)

print(max(c))
