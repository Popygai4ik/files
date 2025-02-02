from  itertools import *

c =0
for s in product('ЗАРЯ', repeat=5):
    w = ''.join(s)
    if w.count('Р') <= 1:
        if w[0] != 'Р' and w[-1] != 'Р' and 'РЯ' not in w and 'ЯР' not in w:
            c += 1
print(c)