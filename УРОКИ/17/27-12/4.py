from math import sqrt

a = [int(i) for i in open('4.txt')]

rs = []
for i in range(len(a) - 1):
    if a[i] > 0 and sqrt(a[i]) % 1 == 0 or a[ i+ 1] > 0 and sqrt(a[i + 1]) % 1 == 0:
        rs.append(a[i] + a[i  + 1])
print(len(rs), max(rs))