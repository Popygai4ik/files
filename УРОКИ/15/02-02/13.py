def inf(n,m):
    return n % m == 8
def f(a,x):
    return (inf(x,a) <= (((x % 270) == 0) and (x % 180 != 0)))


for A in range(1, 1000):
    for x in range(1, 1000):
        if f(A, x) == False:
            break
    else:
        print(A)