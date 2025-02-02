from itertools import *
c = 0
for s in permutations('NORTHE', r=4):
    w = ''.join(s)
    if len(set(s)) != len(w):
        continue
    if w[0] != 'O':
        if 'TH' not in w:
            c += 1
            print(w)
print(c)