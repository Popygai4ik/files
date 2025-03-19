def to_6(s):
    res = ''
    while s > 0:
        res += str(s % 6)
        s = s // 6
    return res[::-1]
res = []
for x in range(1, 2030):
    sem = to_6(6**260 + 6**160 + 6**60 - x)
    if sem.count('0') == 202:
        res.append(x)
print(max(res))