def Del(n, m ):
    return n % m == 0

for A in range(1, 10000):
    res = True
    for x in range(1, 10000):
        if (Del(x, A) <= (Del(x, 24) or (not(Del(x, 3))))) == False:
            res =False
            break
    if res:
        print(A)

