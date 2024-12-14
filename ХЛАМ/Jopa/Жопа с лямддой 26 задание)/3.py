f = open('test.txt')
n, k = map(int, f.readline().split())
# print(n, k)
posilka = []
for s in f:
    ves, stoum = map(int, s.split())
    posilka.append([ves, stoum, stoum/ves])
# print(posilka)
posilka.sort(key=lambda x:[x[-1]])
otp = posilka[:k]
res = 0
# for i in otp:
#     res += i[0]
# print(res)
print(max(otp, key=lambda x: x[2], ))
print(otp)
# 381