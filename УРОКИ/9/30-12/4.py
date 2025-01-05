f = open('4.txt')
c = 0
for s in f:
    data = sorted(map(int, s.split()))
    if ((data[1] * data[3] == data[0] * data[2]) or(data[2] * data[3] == data[1] * data[0]) or (data[0] * data[3] == data[1] * data[2]) )and max(data)** 2 <= max(data) * min(data):
        c += 1
print(c)