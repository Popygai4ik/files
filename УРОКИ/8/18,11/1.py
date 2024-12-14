from itertools import *
c  = 1
for s in product('ACDNY', repeat=4):
    word = ''.join(s)
    print(c, word)
    if word == 'ANDY':
        print(c)
    c += 1