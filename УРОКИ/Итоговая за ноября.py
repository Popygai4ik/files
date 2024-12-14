# # 10 - 16
# def f(i):
#     if i == 0:
#         return 5
#     elif i == 1:
#         return 5
#     elif i % 5 == 0:
#         return ((f(i - 5)) // 3) + 9
#     elif i % 5 > 0:
#         return f(i - (i %  5)) + i * 2
# f = [[] for i in range(100)]
# for i in range(100):
#     if i == 0:
#         f[i] == 5
#     elif i == 1:
#         f[i] = 5
#     elif i % 5 == 0:
#         f[i] = ((f[i - 5]) // 3) + 9
#     elif i % 5 > 0:
#         f[i] = f[int(i - (int(i% 5)))] + i * 2
# print(f(42))
# 11 - 16
# f = [[0] for i in range(100)]
# for n in range(100):
#     if n == 0:
#         f[n] = 1
#     elif n == 1:
#         f[n] = 2
#     if n % 2 != 0 and n > 1:
#         f[n] = 6* n + ((3  * (f[n-2]+ f[n-1]+8))/ 5) // 1
#     elif n % 2 == 0  and n > 1:
#         f[n] = 7 + (3*f[n - 2]/ 2)//1
# print(f[71])
# Код:
#
# def F(n):
#
#     if n == 0:
#
#         return 1
#
#     if n == 1:
#
#         return 2
#
#     if n > 1 and n % 2 == 0:
#
#         return 7 + int(3 * F(n - 2) / 2)
#
#     if n > 1 and n % 2 != 0:
#
#         return 6 * n + int((F(n - 2) + F(n - 1) + 8) / 5)
#
# print(F(71))
# def f(n):
#     if n == 1:
#         return 1
#     if n >= 2:
#         return f(n -1 ) + 3*g(n - 1) + n
# def g(n):
#     if n == 1:
#         return 1
#     if n >= 2:
#         return 11 * f(n - 1) + g(n - 1)* 2 - n * n
# print(f(28)/g(14))
# from itertools import *
# n = 1
# c = 0
# for i in product(sorted('МОНТАЖЕР'), repeat=6):
#     w = ''.join(i)
#
#     if w[0] == 'О':
#         if 2 <= w.count('Ж') <= 3:
#             if n % 3 == 0:
#                 c +=1
#
#     n += 1
# print(c)
# n1 = 0
# n2 = 0
# c = 1
# from itertools import *
# for i in product('ГЕЭ024', repeat=7):
#     w = ''.join(i)
#     if w == 'ЕГЭ2024':
#         n1= c
#     elif w == '2024ЕГЭ':
#         n2 = c
#     c += 1
# print(n2 - n1)
# from itertools import *
# c = 0
# for i in product('ЗУБР', repeat=8):
#     w= ''.join(i)
#     if w.count('Б') == 4:
#         c += 1
#
# # print(c)
# from fnmatch import fnmatch
# #
# # for i in range(0, 10**9, 222):
# #     if fnmatch(str(i), '2?269?8*3?'):
# #         print(i, i // 222)
# c = 0
# for i in range(146, 10**8, 146):
#     if fnmatch(str(i), '17?575*'):
#         c += 1
#         print(i, i / 146)
# print(c)
# s = []
# for i in range(84052, 84131):
#     d = []
#     for x in range(2, i):
#         if i % x == 0:
#             d.append(x)
#     s.append([i ,len(d)])
# s.sort(key=lambda x: x[1])
# print(s)
# 70
# for i in range(400001, 600001 +1000):
#     m = 0
#     d = []
#     for x in range(2, i):
#         if i % x == 0:
#             d.append(x)
#     if len(d) > 0:
#         if (min(d) + max(d)) % 10 == 8:
#             print(i)
f = open('брутфорс/26_3_03ekCDB.txt')
p = []*10000*10000
n = f.readline()
for i in f:
    k = list(map(str, i.split()))
    c = 0
    if k[2] == '#00FF00':
        c = 1
    if k[2]  ==   '#0000FF':
        c = 2
    p[int(k[0] - 1) * 10000 + int(k[1]) - 1] = c
_p = [0]* 10000
for i in range(10000):
    for j in range(1, 9999):
        if p[i * 10000 + j] == 1:
            if