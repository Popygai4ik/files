s = 25**125 - 125**10 * 25**20+5**5-5
res = ''
while s > 0:
    res += str(s % 5)
    s = s // 5
print(res.count('0'))