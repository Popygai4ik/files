f = open('24.1_OBzavDP.txt')
s = f.readline()
i_d = []
# s = 'aaaKaaaKaaaaaKaaa'
for i in range(len(s)):
    if s[i] == "K":
        i_d.append(i)
res = []
for i in range(len(i_d) - 309):
    res.append(i_d[i + 309] - i_d[i] + 1)
print(min(res))
print(res)