from math import *

# for k in range(1,10000):
#     v = math.ceil((11*k)/8)
#     if v < 361:
#         print(k)
# for N in range(1, 10000):
#     i = 13
#
#     V1 = ceil((N * i) / 8)
#
#     V385 = 949 * V1
#
#     if V385 > 727 * 1024:
#
#         print(N)
from itertools import *
c = 1
for i in product(sorted('ПЕЙЗАЖ'), repeat=5):
    w = ''.join(i)
    if w[0] != 'П' and w.count('Ж') == 3 and w.count('А') <= 2:
        print(w,c)
    c +=1