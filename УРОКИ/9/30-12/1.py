f= open('1.txt')
c = 0
for s in f:
    data = sorted(map(int, s.split()))
    # print(data)
    if (data[-1] + data[0]) == (data[2]+data[1]):
        c += 1
print(c)