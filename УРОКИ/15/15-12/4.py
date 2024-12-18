def Del(n, m):
    return n  % m == 0

for a in range(1, 10000):
    for x in range(1, 10000):
        if ((Del(x, a) and (not(Del(x, 12)))) <= (not(Del(x, 18)))) == False:
            break
    else:
        print(a)