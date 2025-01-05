data = [int(s) for s in open('2.txt')]
res  = []
for i in range(len(data) -1):
    if( (data[i] % 10 == 6 and data[i  + 1] % 10 != 6) or (data[i] % 10 != 6 and data[i  + 1] % 10 == 6) ) and ((data[i] ** 2 + data[i + 1] ** 2) < max(data) ** 2):
        res.append(data[i] ** 2 + data[i + 1] ** 2)
print(len(res), max(res))