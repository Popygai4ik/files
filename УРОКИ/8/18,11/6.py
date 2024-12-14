from itertools import *
c = 0
for s in permutations('БАВЛЫ', r=4):
    w = ''.join(s)
    if w[0] != 'В' and 'АЫ' not in w:
        print(w)
        c +=1
print(c )