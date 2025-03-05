def dell(n,m):
    return n % m == 0
def f(a,x):
    return ((((x + 40) < a) or ((x + a) < 40)) <= (dell(x,a)))
for A in range(1, 1000):
    for x in range(1, 1000):
        if f(A, x) == False:
            break
    else:
        print(A)