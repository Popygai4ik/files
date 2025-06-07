# def per(n):
#     res = ''
#     while n > 0:
#         res += str(n % 6)
#         n = n // 6
#     return res[::-1]
# s = 1296**53*216**16+36**101-6
# print(per(s).count('5'))
# from string import *
# alf= '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:16]
# for x in alf:
#     s = int(f'DB24{x}FCD', 16) + int(f'7FC{x}A8', 16)
#     if s % 3 == 0:
#         print(x,s/3)
# alf= '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:18]
# for x in alf:
#     s = int(f'AB5{x}3',18)+int(f'EF{x}13',18)
#     if s % 17 == 0:
#         print(x,s/ 17)
# def per(n,base):
#     res = 0
#     alf = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     n = str(n)
#     for i in range(len(str(n)), 0, -1):
#         # print(f'{alf.index(n[len(n)-i])}*{base}**{i-1}')
#         res += eval(f'{alf.index(n[len(n)-i])}*{base}**{i-1}')
#     return res
# for x in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#     s = per(f'32{x}4',37) + per(f'5{x}29', 37)
#     if s % 63 == 0:
#         print(x, s / 63)
# for x in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:23]:
#     for y in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:23]:
#         s = int(f'13{y}{x}9',23) + int(f'22{y}22',23)
#         if s % 2 != 0:
#             break
#     else:
#         y = 6
#         s = int(f'13{y}{x}9', 23) + int(f'22{y}22', 23)
#         print(x,s//18)
# def per(n):
#     res = ''
#     while n > 0:
#         res += str(n % 6)
#         n = n//6
#     return res[::-1]
# for x in range(1,2030+1):
#     s = 6**260+6**160+6**60-x
#     if per(s).count('0') == 202:
#         print(x)
from itertools import *
# c = 0
# for i in product('ШОКЛАД', repeat=5):
#     w = ''.join(i)
#     if w[0] not in 'ШКЛД' and w[-1] not in 'ОА':
#         c+= 1
# print(c)
# c= 0
# for i in product('АБВГДЕ', repeat=4):
#     w = ''.join(i)
#     if w[0] not in 'БВГД' or w[-1] not in 'АЕ':
#         c+= 1
# print(c)
# c = 0
# for i in permutations('БАЛДЁЖ',r=6):
#     w = ''.join(i)
#     if w.count('АЁ') == 0 and w.count('ЁА') == 0:
#         c+= 1
# print(c)
# c = 0
# for n,e in enumerate(product(sorted('МОНТАЖЕР'), repeat=6), 1):
#     w = ''.join(e)
#     # print(n,w)
#     if w[0] == 'О' and 2 <= w.count('Ж')<= 3 and n % 3 == 0:
#         c+=1
# print(c)
# c= 0
# for i in product('012345', repeat=5):
#     w = ''.join(i)
#     if w[0] == '0':
#         continue
#     if w.count('1') == 1 and '21' not in w and '12' not in w:
#         c+=1
# print(c)
# c= 0
# for i in set(permutations('ДИАНА', r=5)):
#     w = ''.join(i)
#     # for gl in 'АИ':
#     #     w = w.replace(gl,'А')
#     # for gl in 'ДН':
#     #     w = w.replace(gl,'Д')
#     if w.count('АА') == 0:
#         c+=1
# print(c)
def per(n, base):
    alf = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    while n > 0:
        res += str(alf[n % base])
        n = n // base
    return res[::-1]
# print(per(29,18))
res = []
s = 49 * 52 ** 32 + 33**123 + 74 * 43 ** 121 - 751235
for base in range(2,37):
    # print(base)
    # print(base,per(s,base).count('4'))
    res.append([per(s,base).count('4'),base])
print(sorted(res,reverse=True))