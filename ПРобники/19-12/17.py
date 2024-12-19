f = open('17.txt')
data = [int(i) for i in f]
# print(data)
c = []
for i in range(len(data) - 1):
    if (data[i] > 500 or data[i + 1] > 500):
        kv = data[i] ** 2 +  data[i + 1 ] ** 2
        # print(kv)
        c.append(kv)
print(len(c), max(c))