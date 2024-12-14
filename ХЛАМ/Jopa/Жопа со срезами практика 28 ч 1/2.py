f = open('2.txt')
n = int(f.readline())
data = [int(s) for s in f]

v = []
for i in range(n):
    for j in range(i, n):
        st = ''
        for k in data[i: j + 1]:
            st += str(k)
        if st != '' and st == st[::-1]:
            v.append(int(st))
v.sort(reverse=True)
print(v)
print(sum(v[0]))
print(7+8+7+7+8+7)