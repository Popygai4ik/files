from itertools import *
c = 0
for i in product('012345678', repeat=7):
    w = ''.join(i)
    if w[0] in '0':
        continue
    if w[0] not in '37':
        if '00' not in w and  '11' not in w and '22' not in w and  '33' not in w and '44' not in w and  '55' not in w and '66' not in w and  '77' not in w and '88' not in w :
            # print(w)
            c +=1
print(c)
