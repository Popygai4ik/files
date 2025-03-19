def to_7(s):
    res = ''
    while s > 0:
        res += str(s % 7)
        s = s // 7
    return res[::-1]
res = []
for x in range(1, 2071):
    sem = to_7(7**230+7**130+7**30 - x)
    if sem.count('0') == 199:
        res.append(x)
print(max(res))