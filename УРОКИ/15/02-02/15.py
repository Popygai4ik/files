import math

# print(math.gcd(12,6))
def nod(n,m):
    nn = math.gcd(n,m)
    kv1,kv2 = n**0.5, m**0.5
    return ((nn > kv1)and(nn > kv2))
def f(a,x):
    return ((not(nod(x,a))) <= (nod(x,21) <= (not(nod(x,14)))))
for A in range(1,30000):
    for x in range(1,1000):
        if f(A,x) == False:
            break

    else:
        print(A)
