# f = open('17_32.txt')
# a = [int(s) for s in f]
# res = []
# mixa = max(a)
# for i in range(len(a) - 1):
#     if (a[i + 1] + a[i]) == mixa:
#         res.append(a[i + 1] ** 2 + a[i] ** 2)
# print(len(res), max(res) )
# f = open('17_33.txt')
# a = [int(s) for s in f]
# minn = min(a)
# res = []
# for i in range(len(a) - 1):
#     if a[i] % 111 == minn or a[i + 1] % 111 == minn:
#         res.append(a[i] + a[i + 1])
# print(len(res), max(res))
# f = open('17_34.txt')
# a = [int(s) for s in f]
# res = []
# mini = min(x for x in a  if  x % 7 == 0)
# for i in range(len(a) - 1 ):
#     if (a[i] % mini == 0) and (a[i + 1] % mini == 0):
#         res.append(a[i] + a[i + 1])
#
# print(len(res), max(res))
# res= []
# f = open('17_35.txt')
# a = [int(s) for s in f]
# miini = min(x for x in a if len(str(x)) == 3 and x % 10 == 5)
# for i in range(len(a) - 1):
#     if ((len(str(a[i])) == 3) +(len(str(a[i + 1])) == 3) >= 1 and (a[i]+a[i+ 1])% miini == 0 ):
#         res.append(a[i] + a[i+ 1])
# print(len(res),max(res))
# f= open('17_36.txt')
# res = []
# a = [int(s) for s in f]
# mini = min(x for x in a if abs(x) % 41 == 0 and x > 0)
# for i in range(len(a) - 1):
#     if (a[i] != a[i+ 1]) and((abs(a[i+ 1]- a[i ])) % mini == 0):
#         res.append(a[i] + a[i + 1])
# print(len(res), max(res ))
# f = open('17_37.txt')
# a = [int(s) for s in f]
# kol = len(list(x for x in a if abs(x) % 32 == 0))
# res = []
# for i in range(len(a) - 1):
#     # print(type(a[i]))
#     print((a[i] + a[i + 1]) < kol)
#     if (((a[i] < 0) + (a[i + 1] < 0)) >= 1) and ((a[i] + a[i + 1]) < kol):
#         res.append(a[i] + a[i + 1])
# print(len(res), max(res))
# f = open('17_38.txt')
# a = [int(s) for s in f]
# res = []
# mixi = min(x for x in a if abs(x) % 100 == 15 and len(str(abs(x))) == 3)
# for i in range(len(a) - 2):
#     if (((a[i] > 0) and(a[i + 1] > 0) and (a[i + 2] > 0) )or(a[i] < 0) and(a[i + 1] < 0) and (a[i + 2] < 0)    ) and (max(a[i], a[i + 1], a[i + 2]) * min(a[i], a[i + 1], a[i + 2]) > mixi**2):
#         res.append(max(a[i], a[i + 1], a[i + 2]) * min(a[i], a[i + 1], a[i + 2]))
# print(len(res), min(res))
f = open('17_39.txt')
a = [int(s) for s in f]
res = []
mini = min(x for x in a if x > 0 and len(str(x)) == 4 and x % 10 == 6)
# print(mini)
# for i in range(len(a) - 2):
#     prov = [x for x in a[i:i+3] if len(str(abs(x))) == 4 and abs(x) % 10 == 6]
#     if ((len(prov) == 1 and            (a[i] + a[i + 1] + a[i + 2])<= mini)):
#         res.append(a[i] +a[i + 1] +a[i + 2])
#
# print(len(res), max(res))
f = open('17_40.txt')
a = [int(s) for s in f]
maxi = max(x for x in a if x > 0 and len(str(x)) == 5 and x % 100 == 43)
res= []
for i in range(len(a) - 2):
    prov = [x for x in a[i:i + 3] if len(str(abs(x))) == 5 and abs(x) % 100 == 43]
    if  (len(prov)>= 1 and (a[i] ** 2 + a[i + 1] ** 2 + a[i + 2]**2) <= maxi**2):
        res.append(a[i]**2 + a[i + 1]**2 + a[i + 2]**2)
print(len(res),min(res))
# f = open('17_41.txt')
# a = [int(x) for x in f]
# res = []
# simi = sum(x for x in a if x < 0)
# for i in range(len(a) - 2):
#     if ((max(a[i], a[i + 1], a[i + 2]) * min(a[i], a[i + 1], a[i + 2])) > simi):
#         res.append(a[i] + a[i + 1] + a[i + 2])
# print(len(res), max(res))