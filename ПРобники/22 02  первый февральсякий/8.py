k = 0
from itertools import *

for i in product(sorted('МАРТ'), repeat=3):
    w = ''.join(i)
    k += 1
    if w.count('А')== 0:
        print(k, w)