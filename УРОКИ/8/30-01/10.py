from itertools import *
c = 0
for s in set(permutations('ЕРЕТИК', r=6)):
    w = ''.join(s)

    if 'ЕЕ' not in w:
        c +=1
print(c)