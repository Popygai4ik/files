from  itertools import *

c = 0

for i in product('ABCD123', repeat=4):
    w = ''.join(i)
    w = w.replace('1', '*')
    w = w.replace('2', '*')
    w = w.replace('3', '*')
    if w.count('*') == 2:
        c  = c + 1

print(c)