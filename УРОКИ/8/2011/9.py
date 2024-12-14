from itertools import *
c = 0
for i in product('0123456', repeat=6):
    shisl = ''.join(i)
    if shisl[0] not  in '0':
        for k in '0246':
            shisl = shisl.replace(k, '*')
        if shisl.count('5') == 2 and '*5' not in shisl and '5*' not in shisl and'*5*' not in shisl:
            c += 1
print(c)
