a = []
def to4(n):
    res = ''
    while n > 0:
        res += str(n % 3)
        n = n // 3
    return res[::-1]
# print(to4(4))
for n in range(1,1000):
    bini = to4(n)
    if n % 3 == 0:
        bini = bini + bini[:2]
    else:
        bini =bini +  to4((n % 3) * 7 )
    r = int(bini, 3)
    print(n , r)
    if  r > 260:
        a.append(r)
print('1jn ',min(a))