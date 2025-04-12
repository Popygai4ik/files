# def to4(n):
#     res = ''
#     while n > 0:
#         res += str(n % 5)
#         n = n // 5
#     return res[::-1]
# c = []
#
# for n in range(0,1000):
#
#     bib = to4(n)
#     sumi = sum(int(i) for i in str(n))
#     if sumi % 2 == 0:
#         bib += '0'
#     else:
#         bib = bib+'4'
#     R = int(bib, 5)
#     # print(to4(n), R, bib)
#     sumi = sum(int(i) for i in str(R))
#     if sumi % 2 == 0:
#         bib = bib + '0'
#     else:
#         bib = bib+'4'
#     R = int(bib, 5)
#     # print(to4(n), R, bib)
#     sumi = sum(int(i) for i in str(R))
#     if sumi % 2 == 0:
#         bib = bib + '0'
#     else:
#         bib = bib+'4'
#
#     R = int(bib, 5)
#     # print(to4(n), R, bib)
#     sumi = sum(int(i) for i in str(R))
#     if sumi % 2 == 0:
#         bib = bib + '0'
#     else:
#         bib = bib + '4'
# 1249
#     R = int(bib, 5)
#     if R > 600:
#         c.append(R)
# print(min(c))
#     # print(to4(n), R, bib)

from itertools import *
# n = 1
# for eval in permutations('103579'):
#     w = ''.join(eval)
#     if w[0] == '0':
#         continue
#
#
#     print(n,w)
#     n += 1
# res = []
# for i in range(2,7):
#     for ev in permutations(sorted('РљРћР”Р РђРќ'),r=i):
#         w = ''.join(ev)
#         res.append(w)
# res.sort()
# print(res.index("РљРћР”Р РђРќ") +     1)
# from ipaddress import *
# c =0
# ip_net = ip_network('242.52.23.67/255.255.128.0', 0)
# for id in ip_net:
#     ids = str(id).split('.')
#     ids_bi = [bin(int(i))[2:] for i in ids]
#     levi = ''.join(ids_bi[0])+''.join(ids_bi[1])
#     pravi = ''.join(ids_bi[2]) + ''.join(ids_bi[3])
#     if (pravi.count('1') * 2) < levi.count('1'):
#         c +=1
# print(c)
import string
# for i in range(16,37):
#     s = int('AC267D', i) + int('A04A9F', i)
#     if s % i == 0:
#         print(i)
# a = [int(i) for i in open('t')]
# res = []
# for i in range(len(a) - 1):
#     if (a[i] % 6 == 0) or (a[i + 1] % 6 == 0):
#         res.append(a[i]+a[i+1])
# print(len(res),min(res))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_non_decreasing(num):
    s = str(num)
    return s == ''.join(sorted(s))

a = [int(i) for i in open('t')]
min_prime = min(i for i in a if is_prime(i))

res = []
middle_numbers = []

for i in range(len(a) - 2):
    n1, n2, n3 = a[i], a[i+1], a[i+2]
    cond1 = is_non_decreasing(n1) and is_non_decreasing(n2) and is_non_decreasing(n3)
    cond2 = (len(str(n1)) == 4) + (len(str(n2)) == 4) + (len(str(n3)) == 4) <= 2
    cond3 = (n1 + n2 + n3) % min_prime == 0
    if cond1 and cond2 and cond3:
        res.append((n1, n2, n3))
        middle_numbers.append(n2)

print(len(res), max(middle_numbers))