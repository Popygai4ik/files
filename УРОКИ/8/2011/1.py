from itertools import *

c = 1
for s in product(sorted('РУМБА'), repeat=5):
    w = ''.join(s)
    if w[0] in 'Р':
        print(c, w)
    c +=1