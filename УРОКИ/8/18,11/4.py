from itertools import *
c = 0
for s in product('FORK', repeat=6):
    w = ''.join(s)
    if w.count('R') >= 1:
        c +=1
print(c)