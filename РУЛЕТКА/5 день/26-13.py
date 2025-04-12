f = open('t')
n = int(f.readline())
s = [int(s) for s in f]
s.sort(reverse=True)
mas_want = 0
for i in range(n):
    if (i + 1)% 5 != 0:
        mas_want += s[i]
print(mas_want)
print(sum(s[(int((1/5)*n)):]))

# res = []
# for i in range(0, n, 3):
#     res.append((s[i: i + 3]))
# s1 = 0
# for stroka in res:
#     for k in stroka[:-1]:
#         s1 += k
#     print(stroka)
# print(s1)