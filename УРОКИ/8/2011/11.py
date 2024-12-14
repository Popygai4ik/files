from itertools import *

c = 0
for  i in product('01234', repeat=4):
    w = ''.join(i)
    if w[0]not  in '0':
        if w[0]>w[1]>w[2]>w[3]:
            c += 1
print(c)