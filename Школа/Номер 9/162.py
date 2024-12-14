import math
c = 0
f = open('162.txt')
for s in f:
    stroka = list(map(int,s.split()))
    stroka.sort()
    maxi = max(stroka)** 3
    pr = 2 *stroka[0]*stroka[1]*stroka[2]
    f = True
    for k in stroka:
        if k <= 10:
            f = False
    if maxi >=pr and f:
        c += 1
print(c)

