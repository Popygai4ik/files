import math
c = 0
f = open('162.txt')
for s in f:
    stroka = list(map(int,s.split()))
    stroka.sort()
    maxi = max(stroka)
    mini = min(stroka)

    if (maxi - mini) >= 50 and stroka[1] * stroka[2]<= 1000:
        c += 1
print(c)

