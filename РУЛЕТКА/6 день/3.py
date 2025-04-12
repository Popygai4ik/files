def dell(n,m):
    return n % m == 0
d = list(range(30, 45+1))
def f(a,x):
    return ((not(dell(x, 6))) and (x not in {45, 50, 55, 60})) <= (((abs(x - 15) <= 5) <= (x in d)) and ((x & a) != 0))

for a in range(1,1000):
    for x in range(1,1000):
        if f(a,x) == False:
            break
    else:
        print(a)
def dell(n, m):
    return n % m == 0

D = list(range(30, 46))  # [30; 45]

def f(a, x):
    left = (not dell(x, 6)) and (x not in {45, 50, 55, 60})
    right = ((abs(x - 15) <= 5) <= (x in D)) or ((x & a) != 0)
    return (not left) or right  # эквивалент импликации

for a in range(1, 1000):
    ok = True
    for x in range(1, 1000):
        if not f(a, x):
            ok = False
            break
    if ok:
        print(a)
        break

