def Del(n, m):
    return n % m == 0

for a in range(1, 10000):
    for x in range(1, 10000):
        if  ((Del(x, 2) <= (not(Del(x, 5)))) or (x + a >= 70)) == False:
            break
    else:
        print(a)
