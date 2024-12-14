from  itertools import *
c = 0
n = 1
for s in product(sorted('МОНТАЖЕР'), repeat=6):
    w = ''.join(s)
    # sp = []
    s = w
    if w[0] in 'О'and 2 <= w.count('Ж') <= 3 and n % 3 == 0:
        c += 1

    n += 1
print(c)
