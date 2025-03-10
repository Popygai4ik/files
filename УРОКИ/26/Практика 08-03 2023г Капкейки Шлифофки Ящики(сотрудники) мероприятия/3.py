f = open('test')
n = int(f.readline())
data = []
for s in f:
    start_mer, kon_mer = map(int, s.split())
    data.append([kon_mer, start_mer])
data.sort()
print(data)
zal_svododen = 0
res = []
for end, start in data:
    if start >= zal_svododen:
        zal_svododen = end
        res.append([start, end])
    # if start >= 1359:
    #     print(start, end)
print(len(res))
print(res)