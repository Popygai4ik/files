from itertools import *
#
c = 0
for i in product('АЛГОРИТМ', repeat=7):
    w = ''.join(i)
    for k in 'ЛГРТМ':
        w = w.replace(k, 'с')
    for k in 'АОИ':
        w = w.replace(k, 'г')
    # print(w)
    if w.count('с') > w.count('г'):
        c +=1
print(c)
# w = 'АЛГОРИТМ'
# for k in 'ЛГРТМ':
#     w = w.replace(k, 'с')
# for k in 'АОИ':
#     w = w.replace(k, 'г')
# print(w)
# print(w.count('с'))
# print(w.count('г'))
# print(w.count('с') >= w.count('г'))
