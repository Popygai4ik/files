def tre(n):
    res = ''
    while n > 0:
        res += str(n % 3)
        n = n // 3
    return res[::-1]
# print(tre(3))
res = []
for n in range(1,1000):
    tri = tre(n)
    if n % 2 == 0:
        tri = tri + '1'
    else:
        tri = '1'+tri+'0'
    R = int(tri,3)
    if R > 430:
        res.append(R)
print(min(res))
