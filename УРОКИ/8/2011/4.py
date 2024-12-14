from itertools import *

n = 1

for i in product(sorted('ЮПИТЕР'), repeat=5):
    w = ''.join(i)
    if n % 2 != 0 and w[0] not in 'Р' and w.count('Ю') == 2:
        print(w, n)
    n +=1