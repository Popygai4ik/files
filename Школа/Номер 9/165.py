import math
c = 0
f = open('162.txt')
for s in f:
    stroka = list(map(int,s.split()))
    stroka.sort()
    maxi = max(stroka)
    mini = min(stroka)

    if (maxi * mini) == (stroka[1]* stroka[2]) and stroka[-2] ** 2 > mini * maxi:
        c += 1
print(c)

