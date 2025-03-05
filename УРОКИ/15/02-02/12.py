def CELL(n,m):
    return n // m
def f(a,x):
    return ((CELL(x, 50) > 3) or (not(CELL(x, 13) > 3)) or (CELL(x, A) > 6))



for A in range(1, 1000):
    for x in range(1, 1000):
        if f(A, x) == False:
            break
    else:
        print(A)