from itertools import *
c = 0

for i in product('01234567', repeat=5):
    w = ''.join(i)
    if w[0] not in '0':
        if w[0] not in '0246' and w[-1] not in '15' and w.count('7') <= 1:
            c += 1
print(c)
#10094