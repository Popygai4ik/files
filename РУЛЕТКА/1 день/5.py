from itertools import *
c = 0
for i in product('ЕКЛМНОПС', repeat=12):
    w = ''.join(i)
    if w.count('СОНЕК') == 2:
        print(w)
        c += 1
print(c)#432