from itertools import *
for n, eval in enumerate(product(sorted('МАШИН'),repeat=5), 1):
    w = ''.join(eval)
    if w.count('А') == 3 and w.count('Ш') == 0 and w.count('ММ') == 0:
        print(w,n)
