# s = "1721x"
#
#
# print(per(s,37))
# from itertools import *
# c=0
# for ver in product('ЧЕТО', repeat=5):
#     w = ''.join(ver)
#     if w.count('Е') >=1:
#         c+= 1
# print(c)
from itertools import *
c=0
for ver in product('АВГУСТ', repeat=5):
    w = ''.join(ver)
    if w[0] not in 'АУ' or w[-1] not in 'ВГСТ':
        c += 1
print(c)