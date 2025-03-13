a = []
def to4(n):
    res = ''
    while n > 0:
        res += str(n % 4)
        n = n // 4
    return res[::-1]
# print(to4(4))
for n in range(1,1000):
    bini = to4(n)
    if n % 2 == 0:
        bini = bini + '02'
    else:
        bini = '2'+bini+'31'
    r = int(bini, 4)
    if  r > 256:
        print(n)