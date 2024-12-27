a = [int(i) for i in open('3.txt')]
rs = []
for i in range(len(a) - 2):
    if a[i]< 0 or a[i + 1]< 0 or a[i + 2]< 0:
        rs.append(a[i]+a[i + 1]+a[i + 2])
print(len(rs), min(rs))