from itertools import *
c = 0
for i in product('БЛАНК', repeat=6):
    w = ''.join(i)
    if w[0] == 'К' and w.count('Н') == 2:
        c += 1
        print(w)
print(c)