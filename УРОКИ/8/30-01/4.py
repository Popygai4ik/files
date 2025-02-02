from itertools import *
c = 0
for s in product('0123456', repeat=5):
    w = ''.join(s)
    if w[0]!= '0':
        if w[0] in '135':
            if w[-1] not in '15':
                if w.count('3') <= 1:
                    c += 1
print(c)