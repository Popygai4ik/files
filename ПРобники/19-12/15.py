def Del(n, m):
    return n % m == 0
for a in range(1, 10000):
    for x in range(1,10000):
        if ((Del(x, a) and Del(x, 8)) <= ((not(x, 8)) or Del(x, 240))) == False:
            break
    else:
        print(a)