import math
c = 0
f = open('164.txt')
for s in f:
    stroka = list(map(int,s.split()))
    stroka.sort()
    maxi = max(stroka)
    mini = 2 *(min(stroka) ** 2)
    if stroka[1] != maxi and stroka[2] != maxi:
        pr = stroka[1]*stroka[2]
    if mini >=pr and len(set(stroka)) <= 3:
        c += 1
print(c)

