# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = (x and (not(w)) and (y or (not(z))))
#                 if f:
#                     print(x, y, z, w, f)
# from itertools import *
# import string
# c = 0
# for i in permutations('0123456789ABCDEF', r=3):
#     w = ''.join(i)
#     if w[0] in '0':
#         continue
#     else:
#         for y in '02468ACE':
#             w = w.replace(y, 'Ч')
#         for x in '13579BDF':
#             w = w.replace(x, 'Н')
#         if 'НН' not in w and 'ЧЧ' not in w:
#             c += 1
#             print(w)
# print(c)
# print('x y z w f')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = (((z <= y) == (x <= (not(w)))) and (x or y))
#                 if  f and x == 0 and z == 1:
#                     print(x, y, z, w, f)

for a in range(10000):
    f = True
    for x in range(1000):
        for y in range(1, 1000):
            if (((x >= 17) or (3*x < y)) or (y*x < a)) == False:
                f = False
                break
        if f == False:
            break
    else:
        print(a)