# c = 0
# from itertools import *
#
# for i in product('LOCK', repeat=7):
#     w = ''.join(i)
#     if w.count('O') >= 2:
#         c += 1
# print(c)
# c = 0
# from itertools import *
#
# for i in product('ПИТОН', repeat=7):
#     w = ''.join(i)
#     if w[0] == 'П':
#         if w.count('И') == 1:
#             c += 1
#
# print(c)
# c = 0
# from itertools import *
#
# for i in set(permutations('ПРОЦЕССОР', r=9)):
#     w = ''.join(i)
#     if 'ПРО' not in w and 'ЦЕС' not in w and 'СОР' not in w:
#         c += 1
# print(c)
# from itertools import *
# c = 0
# for i in product(set("КАБАЧОК"), repeat=4):
#     w = ''.join(i)
#     # print(w)
#     for j in 'КБЧ':
#         w = w.replace(j,'S')
#     for j in 'АО':
#         w = w.replace(j, 'G')
#     # print(w)
#     if w[0] == 'S'and w[-1] == 'G' and 'SS' not in w:
#         print(w)
#         c+= 1
#
# print(c)
# from itertools import *
# c = 0
# for i in product('ЗАРЯ', repeat=5):
#     w = ''.join(i)
#     if w.count('Р') <= 1 and w[0] != 'Р' and  w[-1] != 'Р' and 'РЯ' not in w and 'ЯР' not in w:
#         c += 1
# print(c)
# 13
# from itertools import *
# c = 0
# for i in product('0123456', repeat=4):
#     w = ''.join(i)
#     if w[0] == '0':
#         continue
#     # print(w)
#     for j in '13':
#         w = w.replace(j, 'N')
#     for j in '5':
#         w = w.replace(j, 'P')
#     print(w)
#     if w.count('P') == 1 and 'N2' not in w and '2N' not in w and 'P2' not in w and '2P' not in w:
#         print(w)
#         c += 1
# print(c)
# 14
# from itertools import *
# c = 0
# for i in product('01234567', repeat=5):
#     w = ''.join(i)
#     if w[0] == '0':
#         continue
#     # print(w)
#     if w[0] not in '1357' and w[-1] not in '34' and w.count('5')<= 1:
#         c += 1
# print(c)
# from itertools import *
# c = 0
# for i in product('01234567', repeat=6):
#     w = ''.join(i)
#     if w[0] == '0':
#         continue
#     for j in '1357':
#        w = w.replace(j,'N')
#     for j in '0246':
#        w = w.replace(j,'S')
#     if 'SS' not in w and 'NN' not in w:
#         print(w)
#         c += 1
# print(c)
import string
from itertools import *
c = 0
for i in product('0123456789ABCDEFGHIJK', repeat=6):
    w = ''.join(i)
    if w[0] == '0':
        continue
    if w.count('6') == 1 and (sum(w.count(i) for i in 'CDEFGHIJK' )>= 3):
        # print(w)
        c += 1
print(c)
