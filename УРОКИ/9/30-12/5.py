f = open('5.txt')
c = 0
for s in f:
    data = list(map(int, s.split()))
    y1 = all([x % 2 == 0 for x in data])
    # print(data, y1)
    if y1 and (min(data) ** 2 <= sum(data) - min(data)):
        c += 1
print(c)