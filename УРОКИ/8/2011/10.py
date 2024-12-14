from itertools import *
c = 0
for i in permutations('0123456789', 4):
    shisl = ''.join(i)
    if shisl[0] not  in '0':
        for k in '02468':
            shisl = shisl.replace(k, 'Ч')
        for j in '13579':
            shisl = shisl.replace(j, 'Н')
        if 'НЧ' not in shisl and 'ЧН' not in shisl:
            c += 1
print(c)
