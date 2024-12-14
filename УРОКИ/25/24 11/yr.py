# from fnmatch import *
#
# for i in range(0, 10**9, 4323):
#     if fnmatch(str(i), '1?7344*3'):
#         print(i, i // 4323)

# for i in range(100356, 100368):
#     d = []
#     for k in range(1, i+1):
#         if i % k == 0:
#             d.append(k)
#     if len(d) == 4:
#         print(i, ' = ', *d)
# for k in range(1000):
#     m = k + 7_000_000
#     d = []
#     for i in range(2, int(m**0.5)):
#         if m % i == 0:
#             d.append(i)
#             d.append(m // i)
#         if len(d) != 3:
#              print(d)