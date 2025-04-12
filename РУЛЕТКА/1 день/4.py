from itertools import *
for n, eval in enumerate(product('АВЕНР', repeat=5), 1):
    w = ''.join(eval)
    if w[-1] != 'Н' and w.count('В') == 2:
        print(w,n)
