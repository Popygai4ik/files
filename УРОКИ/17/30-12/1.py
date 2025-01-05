data = [int(s) for s in open('1.txt')]
# print(data)
m14 = max([x for x in data if x % 14 == 0])
sym_troek = []
for i in range(len(data) - 2):
    if (((len(str(abs(data[i]))) == 4)  +(len(str(abs(data[i  + 1]))) == 4) + (len(str(abs(data[i  + 2]))) == 4)) == 1) and (data[i] + data[i + 1] + data[i +2]) <= m14:
        sym_troek.append(data[i] + data[i + 1] + data[i +2])
print(len(sym_troek), max(sym_troek))