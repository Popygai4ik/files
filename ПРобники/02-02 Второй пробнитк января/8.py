from itertools import *
k1 = 0
k2 = 0
n = 1
for s in product(sorted("HEART"), repeat=5):
    w = ''.join(s)
    if w == 'AHAHA':
        k1 = n
    elif w == 'HEHEH':
        k2 = n
    print(w, n)
    n += 1
print('i', k2 - k1)