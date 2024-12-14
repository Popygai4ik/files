data = [int(i) for i in open('17.txt')]
maxi = max(data) % 3
mami = min(data) % 7
print(data)
res = []
for i in range(len(data) -1):
    if (data[i] % 3 == maxi or data[i+ 1] % 3 == maxi) and  (data[i] %7 == mami or data[i+ 1] % 7 == mami):
        res.append(data[i] + data[i +1])
print(len(res ), max(res))