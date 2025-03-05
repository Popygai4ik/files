def f(a,x,y):
    return (((a ^ 30 > 14) and (a ^ 45 != 0)) <= (x ^ y < 100))
for A in range(1, 1000):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if f(A,x,y) == False:
                break
        if f(A, x, y) == False:
            break
    else:
        print(A)