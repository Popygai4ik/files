# c= []
# for n in range(8, 10000):
#     bini = bin(n)[2:]
#     if (int(bini[-1]) + int(bini[-2]) + int(bini[-3]) ) %  2== 0:
#         bini += '10'
#     else:
#         bini = '1'+bini+'0'
#     r = int(bini, 2)
#     if r > 880:
#         c.append(r)
# print(min(c))
# def to4(n):
#     rs = ''
#     while n > 0:
#         rs += str(n % 4)
#         n = n // 4
#     return rs[::-1]
# for n in range(1, 10000):
#     bini = to4(n)
#     if bini.count('3') > 2:
#         bini += '0'
#     else:
#         bini += str(bini.count('3') % 4)
#     r = int(bini, 4)
#     if r > 461:
#         print(n)
# import sys
# sys.setrecursionlimit(100000)
# def f(n):
#     if n == 122:
#         return 156
#     if n > 1:
#         return 2 * f(n -1) + 4
# print(f(2017) - 4*f(2015))
#
# print(f(2017) - 4 * f(2015))
# def f(n):
#     if n == 0 or n == 1:
#         return 2
#     if n % 2 == 0 and n > 1:
#         return 7 * f(n - 1) *(n  +3) - 11
#     if n % 2 != 0 and n > 1:
#         return g(n - 1) + f(n - 2)*(n + 2)
# def g(n):
#     if n == 0:
#         return 2
#     if n == 1 or n == 2:
#         return 4
#     if n > 2:
#         return 4 * g(n - 3) + n + 1 + f(n - 2)
# print(f(15) - g(f(3)))

# def f(a, n):
#     if a  <  20 or n > 4:
#         return  n == 2 or n == 4
#     if n % 2 == 0:
#         c = [[f(a - 1, n +1),f(a - 2, n +1)]]
#         if a % 2 == 0:
#             c.append(f(0.5*a,  n +1))
#         return all(c)
#     else:
#         c = [[f(a - 1, n + 1), f(a - 2, n + 1)]]
#         if a % 2 == 0:
#             c.append(f(0.5 * a, n + 1))
#         return any(c)
# for s in range(1,100):
#     if f(s, 0):
#         print("19", s)
# def to23(stert, stop):
#     if stert > stop or stert == 15:
#         return 0
#     if stert == stop:
#         return 1
#     if stert < stop:
#         return to23(stert + 2, stop) + to23(stert * 2, stop)+ to23(stert*3, stop)
# print(to23(5, 10)*to23(10, 76))
def to23(start, stop):
    if start > stop:
        return 0
    if start == stop:
        return 1
    if start < stop:
        return to23(start +1, stop) + to23(start + 3, stop) + to23(start* 2, stop)
k = 0
for i in range(40, 46):
    k += to23(10, i)
print(k)