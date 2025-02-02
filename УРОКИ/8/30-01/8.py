from itertools import *


c = 0
for s in set(permutations('БАЛАГАНИЩЕ',r=4)):
    w = ''.join(s)
    if len(set(s)) != len(w):
        continue
    if w[0] in 'БЛГНЩ':
        for k in 'БЛГНЩ':
            w = w.replace(k, 'C')
        for k in 'АИЕ':
            w = w.replace(k, 'G')
        if w == 'CGCG':
             c+=1
print(c)
