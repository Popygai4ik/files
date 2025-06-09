import math
from fnmatch import *
# for i in range(222,10**9, 222):
#     if fnmatch(str(i),'2?269?8*3?') and i % 222 == 0:
#         print(i,i/222)

# for i in range(5943,10**10,5943):
#     if fnmatch(str(i), '73*?859?'):
#         print(i,i/5943)
# res = []
# for i in range(2025,10**10,2025):
#     if fnmatch(str(i), '1*2342?5') and sum(str(i).count(g) for g in '02468') == 5:
#         res.append(i)
# print(sum(res))
def deliters(n):
    res = []
    for x in range(2,int(n ** (0.5) + 1)):
        # print(n,x)
        if n % x == 0:
            res.append(n // x)
            res.append(x)
    return list(set(res))
# # print(deliters(36))
# for i in range(23456,78954+1):
#     if len(deliters(i)) == 3:
#         print(i,max(deliters(i)))
# for n in range(800_000, 800_000 + 100):
#     for x in range(13,n,10):
#         if n % x == 0:
#             print(n,x)
#             800001  863 800002 57143
# for i in range(350670,350670 + 100):
#     deliter = deliters(i)
#     if len(deliter) > 0:
#         m = max(deliter)+ min(deliter)
#     else:
#         m = 0
#     if m % 8 == 4:
#         print(i,m)
# for i in range(600_000, 600_000+100):
#     deler = deliters(i)
#     if any((u % 10 == 7 and u != 7) for u in deler):
#         print(i,sorted(deler))
# for i in range(100000, 100000+ 100):
#     deliter = deliters(i)
#     if len(deliter) > 0:
#         r = max(deliter) + min(deliter)
#     else:
#         r = 0
#     if  r % 11 == 0:
#         print(i,r)
# for i in range(400_000,400_000+100):
#     m = 0
#     for x in range(2,i):
#         if i % x == 0:
#             m = x + i//x
#             break
#     if m % 10 == 8:
#         print(i,end=' ')
# for i in range(123,int('ffffff', 16), 123):
#     if fnmatch(hex(i)[2:], 'f5*1?4'):
#         print(hex(i)[2:], i/123)
# def pros(n):
#     for x in range(2,n):
#         if n % x == 0:
#             return False
#     return True
# def chec(n):
#     for i in range(2,int(n ** (0.5) + 1)):
#         if n % i == 0:
#             if pros(i) and pros(n // i):
#                 return True
#     return False
# for i in range(1597,10**8,1597):
#     if fnmatch(str(i), '132?5*5??') and chec(i):
#         print(i,i/1597)
for i in range(400000001, 400_000_000 + 100):
    dell = sorted(deliters(i))
    if len(dell) >= 5:
        m = math.prod(dell[:5])
    else:
        m = 0
    if 0 < m < i:
        print(m,i)