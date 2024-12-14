from itertools import *
c = 0
for i in product('0123456', repeat=5):
    w = ''.join(i)
    if w[0] in '0':
        continue
    c +=1
print(c)
