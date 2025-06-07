s = open('24.2_OBzavDP.txt').readline()
i_d= []
# s = s
# print(s)
for i in range(len(s) - 1):
    if s[i] == 'O':
        i_d.append(i)
res = []
# print(i_d)
for i in range(len(i_d) - 151):
    # print(i_d[i + 3] - i_d[i]  - 1)
    res.append(i_d[i + 151] - i_d[i] - 1)
print(res)
print(max(res))