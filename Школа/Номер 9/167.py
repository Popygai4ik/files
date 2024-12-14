import math
c = 0
f = open('167.txt')
for s in f:
    stroka = list(map(int,s.split()))
    x1 = stroka[0]
    x2 = stroka[2]
    x3 = stroka[4]
    y1 = stroka[1]
    y2 = stroka[3]
    y3 = stroka[5]
    # print((y2 - y1)/ (x2 - x1))
    # print((y3 - y1)/ (x3 - x1))
    if (y2 - y1)/ (x2 - x1) == (y3 - y1)/ (x3 - x1):
        c += 1
print(c)

