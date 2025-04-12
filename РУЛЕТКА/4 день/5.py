def deli(n,m):
    return n % m == 0
for A in range(1,1000):
    for x in range(1,1000):
        if (((x * A) > 529) or (deli(x,5) <= (not(deli(x,13)))) or (deli(x,25))) == False:
            break
    else:
        print(A)