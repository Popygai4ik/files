f = open('task4.txt')
s = f.readline()
# # byfer = ''
# # for i in range(len(s)):
# #     if byfer.count('AC')  < 25 and (s[i] + s[i + 1]) == "AC":
# #         byfer += s[i]+s[i + 1]
# #     if byfer.count('AC') == 25 and
ind_ac = []
for i in range(len(s)):
    if s[i:i + 2] == "AC":
        ind_ac.append(i)
res= []
for i in range(len(ind_ac) - 24):
    res.append(ind_ac[i + 24] + 1  - ind_ac[i] + 1)
print(min(res))

# f = open('t')
# s = f.readline()
# i_d = []
# for i in range(len(s)):
#     if s[i:i+3] == 'RSQ':
#         i_d.append(i)
# # print(i_d)
# res = []
# for i in range(len(i_d) - 129):
#     res.append(i_d[i+ 129] + 1 - i_d[i]   + 1 + 2)
# print(min(res) )