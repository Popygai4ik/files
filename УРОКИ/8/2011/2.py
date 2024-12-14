from  itertools import *

c = 1

for i in product(sorted('ФУТБОЛКА'), repeat=6):
    w = ''.join(i)
    if w[0] not in 'У' and w.count('Ф') == 2 and w.count('А') <= 1:
        print(c, w)
    c +=1