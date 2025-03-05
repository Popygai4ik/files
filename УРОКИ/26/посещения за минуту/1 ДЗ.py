f = open('1.txt')
n = int(f.readline())
day = [0] * 1442
izm = [0] * 1442
for s in f:
    vhod, vihod = map(int, s.split())
    izm[vhod] += 1
    izm[vihod] -= 1
c = 0
for t in range(1440):
    c += izm[t]
    day[t] = c

print(max(day))

