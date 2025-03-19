def to_6(s):
    res = ''
    while s > 0:
        res += str(s % 6)
        s = s // 6
    return res[::-1]
res = []
for x in range(1, 5031):
    sem = to_6(6**260 + 6**160 + 6**60 - x)
    if sem.count('2') == sem.count('3'):
        res.append(x)
print(max(res))