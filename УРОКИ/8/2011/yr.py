from itertools import *
c = 0
c1 = 0
for i in product(sorted('ИНФОРМАТ'), repeat=5):
    c += 1
    w = ''.join(i)
    if w[0] not in 'О'and c % 2 != 0 and 1 <= w.count('Н') <= 2:
      c1 += 1
print(c1)
# for i in product('АЕКНРС', repeat=6):
#     c += 1
#     w = ''.join(i)
#     if w.count('А') <= 3 and w.count('Н') == 2:
#         print(c)
#         break