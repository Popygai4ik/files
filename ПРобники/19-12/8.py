from itertools import *
c = 0
# for i in product('малина', repeat=5):
#     w = ''.join(i)
#     f = True
#     for j in range(len(w) -1):
#         # print(w[j])
#         if w[j] == w[j +1]:
#             f = False
#     if f:
#         c += 1
#         print(w)
# print(c)
for i in set(permutations('МАЛИНА', r=5)):
    w = ''.join(i)
    if w.count('АА')!= 0:
        continue
    c+= 1
print(c)