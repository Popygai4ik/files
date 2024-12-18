def Del(n, m):
    return n % m == 0

for a in range(1, 10000):
    for x in range(1, 10000):
        if (((Del(x, 24) and Del(x, 36)) <= Del(x, a)) and (a ** 2 - a - 5000 < 112)) == False:
            break
    else:
        print(a)