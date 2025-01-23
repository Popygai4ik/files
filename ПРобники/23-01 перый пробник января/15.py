def Del(n,m):
    return n % m == 0

for A in range(1, 1000):
    for x in range(10000):
        if (Del(x, A) <= ((not (Del(x, 28))) or Del(x, 42))) == False:            break
    else:
        print(A)