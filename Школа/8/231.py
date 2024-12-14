from itertools import *
c = 0
for i in product('012345678', repeat=7):
    w = ''.join(i)
    if w[0] in '0':
        continue
    if w[-1]not in '347':
        if '000' not in w and  '111' not in w and '222' not in w and  '333' not in w and '444' not in w and  '555' not in w and '666' not in w and  '777' not in w and '888' not in w :
            # print(w)
            c +=1
print(c)
