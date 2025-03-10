f = open('5')
n = int(f.readline())
data = []
for s in f:
    star, end = map(int,s.split())
    data.append([end,star])
data.sort()
vrash_soboden = 0
res = []
for end,star  in data:
    if star >= vrash_soboden:
        vrash_soboden = end
        res.append([star, end])
    # if star <= 37:
    #     print(star, end)
print(len(res))
print(data)