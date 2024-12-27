data = [int(i) for i in open('1.txt')]
# print(data)
res = []
for index in range(len(data) - 1):
    if data[index] % 8 == 0 and data[index + 1] % 8 == 0:
        res.append(abs(data[index] - data[index + 1]))
print(len(res), min(res ))