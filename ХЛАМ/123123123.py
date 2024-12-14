# print("x,y,z,w f")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0,1:
#             for w in 0, 1:
#                 f = ((not(not(x) or y) or z) or not(w))
#                 if not(f):
#                     print(x,y,z,w, f)
#
# for N in range(1, 1000):
#     bin_N = str(bin(N))[2:]
#     suma = sum([int(i) for i in bin_N])
#     if suma % 2 == 0:
#         bin_N = "10" + bin_N[2:] + "0"
#     else:
#         bin_N = "11" + bin_N[2:] + "1"
#     R = int(bin_N, 2)
#     if R < 20:
#         print(N)
# N = 4
# bin_N = str(bin(N))[2:]
# suma = sum([int(i) for i in bin_N])
# if suma % 2 == 0:
#     bin_N = "10" + bin_N[2:] + "0"
# else:
#     bin_N = "11" + bin_N[2:] + "1"
# R = int(bin_N, 2)
# print(R)
# for N_S in range(1, 1000):
#     i = 13
#     k = 1280 * 720
#     I = i * k * N_S
#     if I / 1_474_560 <= 280:
#         print(N_S)
# f = open("test.txt")
# c = 0
# for i in f:
#     i = i.split()
#     i.sort()
#     print(i)
#     print(i)
#     if int(i[-1]) < int(i[0]) + int(i[1]) + int(i[2]) and len(set(i)) == len(i):
#         c += 1
# print(c)
# s = '7' * 108
# while '33333' in s or '777' in s:
#     if '33333' in s:
#         s = s.replace('33333', '7', 1)
#     else:
#         s = s.replace('777', '3', 1)
# print(s)
# import sys
# sys.setrecursionlimit(100000)
# def f(n):
#     if n == 1:
#         return 1
#     else:
#         return n * f(n -1)
# print((2026 * f(2029) +f(2028))/f(2027))
f = open("17.3.txt")
data = [int(i) for i in f]
mini = min(data)
t = []
c = 0
for i in range(len(data) - 1):
    if data[i] % 123 == mini or data[i + 1] % 123 == mini:
      c += 1
      t.append(data[i] + data[i +1])
print(c, max(t))