# f = [0]*100
# for n in range(1,100):
#     if n == 1:
#         f[n] = 1
#     elif n > 1:
#         f[n] = f[n - 1]  * (n + 1) + 5
# print(f[7])
# f = [0]*100
# for n in range(1,100):
#     if n == 1:
#         f[n] = 1
#     elif n % 2 != 0 and n > 1:
#         f[n] = n + 5 * f[n - 2]
#     elif n % 2 == 0 and n > 1:
#         f[n] = 2 * n * f[n - 1]
# print(f[9])

# f= [0]*3000
# for n in range(1,3000):
#     if n == 1:
#         f[n] = 1
#     elif n > 1:
#         f[n] = 2  * n * f[n - 1] - 1
# print(f[2000]/f[1997])

# f = [0]* 3001
# for n in range(3000, 0,-1):
#     if n >= 2025:
#         f[n] = n
#     elif n < 2025:
#         f[n] = n//2 + f[n + 3]
# print(f[2020] - f[2023])

# f= [0]*3000
# for n in range(2999,0,-1):
#     if n >= 2023:
#         f[n] = n
#     elif n < 2023:
#         f[n] = n // 3 + f[n + 2]
# print(f[2015]-f[2018])
# f = [0] * 3000
# for n in range(1,3000):
#     if n == 1:
#         f[n] = 1
#     elif  n > 1:
#         f[n] = n * f[n - 1]
# print((f[2024]//15 - f[2023]) // f[2021])

# f = [0]* 100
# for n in range(0,100):
#     if n == 1:
#         f[n] = 2
#     elif n == 2:
#         f[n] = 3
#     elif n % 2 != 0 and n > 2:
#         f[n] = int((((f[n - 2] + f[n - 2])/7)))
#     elif n % 2 == 0 and n > 2:
#         f[n] = 7 * n - int(f[n - 1]/2 + 5)
# print(f[40])

# def f(n):
#     if n < 2:
#         return n
#     if n >= 2 and n % 2 == 0:
#         return f(n / 2)  + 1
#     if n >= 2 and n % 2 != 0:
#         return f(3 * n + 1) + 1
# c = 0
# for i in range(1,10000+1):
#     if f(i) > 200:
#         c += 1
# print(c)
#
# def t23(start, stop):
#     if start > stop:
#         return 0
#     if start  == stop:
#         return 1
#     if start < stop:
#         return t23(start ** 2, stop) + t23(start * 2, stop)+t23(start + 1, stop)
# print(t23(2,28))
# def t23(start, stop):
#     if start > stop or start == 26:
#         return 0
#     if start  == stop:
#         return 1
#     if start < stop:
#         return t23(start * 2, stop)+t23(start + 2, stop)
# print(t23(2,14)*t23(14,56))
# def per(n):
#     alf = '0123456789AB'
#     res = ''
#     while n > 0:
#         res += str(alf[n % 12])
#         n = n // 12
#     return res[::-1]
# def t23(start,stop):
#     if start< stop:
#         return 0
#     if start == stop:
#         return 1
#     if start > stop:
#         return t23(start//2, stop) + t23(start - 3, stop) + t23(start - 1, stop)
# print(per(t23(22,2)))
import sys
# from functools import lru_cache
# sys.setrecursionlimit(50000)
# @lru_cache(None)
# def t23(start, stop,pyti):
#     if start > stop or '****' in pyti or  '--' in pyti or start - 1 > stop:
#         return 0
#     if start == stop and pyti.count('****') == 0 and pyti.count('--') == 0:
#         return 1
#     if start < stop:
#         return t23(start - 1, stop, pyti+'-')+ t23(start * 2, stop, pyti+'*') + t23(start * 3, stop, pyti+'*')
# print(t23(4,116,''))
# def t23(start,stop,last_dep):
#     if start > stop:
#         return 0
#     if start == stop:
#         return 1
#     if start < stop:
#         if last_dep == '+1':
#              return  (t23(start + 3,stop,'+3')) + t23(start *2,stop,'*2')
#         elif last_dep == '+3':
#             return  (t23(start + 1,stop,'+1')) + t23(start *2,stop,'*2')
#         elif last_dep == '*2':
#             return (t23(start + 1, stop, '+1')) + t23(start + 3, stop, '+3')
#     return (t23(start + 1, stop, '+1')) + t23(start + 3, stop, '+3')+ t23(start *2,stop,'*2')
# print(t23(3,56,''))
sys.setrecursionlimit(20000)

def f(m,n):
    if m==0:
        return n + 1
    if n == 0 and m > 0:
        return f(m - 1, 1)
    if m >0 and n > 0:
        return f(m - 1,f(m,n-1))
print(f(4,1))