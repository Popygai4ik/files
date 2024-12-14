import sys
from functools import lru_cache
# sys.setrecursionlimit(10000)
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n * F(n - 1)
# print(F(2023) / F(2021))
# f = [0] * 10000
# for n in range(10000):
#     if n == 1:
#         f[n] == 1
#     if n > 1:
#        f[n] = n * f[n - 1]
# print(f[2023] / f[2021])
@lru_cache(maxsize=None)
def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return (n - 1) * (n -2) + F(n -1) + F(n -2)
print(F(2021) - F(2019) - 2 * F(2018) - F(2017))
# f = [0] * 10000
# for n in range(10000):
#     if n == 1:
#         f[n] = 1
#     if n == 2:
#         f[n] =2
#     if n  >2:
#         f[n] = (n - 1) * (n -2) + f[n -1] + f[n -2]
# print(f[2021] - f[2019] - 2 * f[2018] - f[2017])