# # 19
# def f(a, n):
#     if a >=70 or n > 2:
#         return  n == 2
#     if n % 2 == 0:
#         r = []
#         r.append(f(a -1, n +1))
#         if a % 3 == 0:
#             r.append(f(a //3, n +1))
#         else:
#             r.append(f(a -2, n +1))
#         if a % 5 == 0:
#             r.append(f(a //5, n +1))
#         else:
#             r.append(f(a -3, n +1))
#         return all(r)
#     else:
#         r = []
#         r.append(f(a - 1, n + 1))
#         if a % 3 == 0:
#             r.append(f(a // 3, n + 1))
#         else:
#             r.append(f(a - 2, n + 1))
#         if a % 5 == 0:
#             r.append(f(a // 5, n + 1))
#         else:
#             r.append(f(a - 3, n + 1))
#         return any(r)
# for s in range(70, 15, -1):
#     if f(s, 0):
#         print("19", s)
# # 20
# def f(a, n):
#     if a >=129 or n > 3:
#         return  n == 3
#     if n % 2 == 1:
#         return all([f(a +1, n +1),f(a*2, n +1)])
#     return any([f(a + 1, n + 1), f(a * 2, n + 1)])
# for s in range(1,129):
#     if f(s, 0):
#         print("20", s)
# # 21
# def f(a, n):
#     if a >=129 or n > 4:
#         return  n == 2 or n == 4
#     if n % 2 == 0:
#         return all([f(a +1, n +1),f(a*2, n +1)])
#     return any([f(a + 1, n + 1), f(a * 2, n + 1)])
# for s in range(1,129):
#     if f(s, 0):
#         print("21", s)
# 19
def f(a, n):
    if a >=100 or n > 4:
        return  n == 2 or n == 4
    if n % 2 == 0:
        return all([f(a +2, n +1),f(a*3, n +1)])
    return any([f(a + 2, n + 1), f(a * 3, n + 1)])
for s in range(1,100):
    if f(s, 0):
        print("19", s)
# 20
# def f(a, n):
#     if a >=71 or n > 3:
#         return  n == 3
#     if n % 2 == 1:
#         return all([f(a +1, n +1),f(a*2, n +1)])
#     return any([f(a + 1, n + 1), f(a * 2, n + 1)])
# for s in range(1,71):
#     if f(s, 0):
#         print("20", s)
# 21
# def f(a, n):
#     if a >=71 or n > 4:
#         return  n == 2 or n == 4
#     if n % 2 == 0:
#         return all([f(a +1, n +1),f(a*2, n +1)])
#     return any([f(a + 1, n + 1), f(a * 2, n + 1)])
# for s in range(1,71):
#     if f(s, 0):
#         print("21", s)