from itertools import *
c = 0
for i in set(permutations('АКАРИДА', r=7)):
    w = ''.join(i)
    if w.count('А') == 3 and w.count('К') == 1 and w.count('Р') == 1 and w.count('И') == 1 and w.count('Д') == 1:
        print(w)
        for x in 'АИ':
            w = w.replace(x, 'Г')
        for z in 'КРД':
            w = w.replace(z, 'С')
        if 'ССГГ' not in w and  'ГГСС' not in w and 'ГГ' not in w and  'СС':
            print(w)
            c +=1
print(c)
