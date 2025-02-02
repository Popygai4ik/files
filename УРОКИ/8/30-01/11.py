from itertools import *

c = 0
for s in product('WXYZ', repeat=6):
    w = ''.join(s)
    if w.count('YY'):
        c+=1
print(c)