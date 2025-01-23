from itertools import *
c = 0
for s in product('01234567', repeat=5):
    w = ''.join(s)
    if w[0] != '0':
        if w.count('4') == 2:
            for j in '1357':
                w = w.replace(j, 'H')
            if 'H4' not in w and '4H' not in w:
                print(w)
                c += 1
print(c)