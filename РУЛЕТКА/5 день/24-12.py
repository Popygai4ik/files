# f = open('24_55.txt')
# stroki = [s for s in f]
res = []
stroki = open('t').readline()
# for h in range(len(stroki)):
#     res.append([stroki[h].count('W'), h])
# print(min(res))
# print(res)
connter = []
import string
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    connter.append([stroki.count(i),i])
print(max(connter))
