def tre(n, m, k ):
    l = sorted([n,m,k])
    return l[0]+l[1] > l[2]
for a in range(1, 1000):
    for x in range(1, 1000):
        if (not((tre(x, 11, 24) == (not(max(x, 7) > 32))) and (tre(x, a, 7)))) == False:
            break
    else:
        print(a)