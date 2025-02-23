def ddel(n, m):
    return n % m == 0
for A in range(1, 1000):
    for x in range(1000):
        if (((not(ddel(x, A))) and (ddel(x, 8))) <= (not(ddel(x, 36)))) == False:
            break
    else:
        print(A)