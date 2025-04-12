def dell(n, m):
    return n % m == 0
for a in range(1,1000):
    for x in range(1,1000):
        if ((dell(x,a) <= ((not(dell(x,78))) or (dell(x,52))))) == False:
            break
    else:
        print(a)
def dell(n, m):
    return n % m == 0

for a in range(1, 1000):
    ok = True
    for x in range(1, 1000):
        if dell(x, a) and not (not dell(x, 78) or dell(x, 52)):
            ok = False
            break
    if ok:
        print(a)
        break
