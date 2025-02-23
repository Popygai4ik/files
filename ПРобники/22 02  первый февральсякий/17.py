a = [int(i) for i in open('17.txt')]
# print(a)
s = []
for i in range(len(a)- 1):
    if ((a[i] + a[i+ 1])% 4 == 0) and (a[i] + a[i+ 1])% 7 != 0:
        # print(1123213)
        if abs(a[i]*a[i +1 ])% 10 == 3:
            s.append(a[i]+a[i+1])
# s.sort()
print(len(s), min(s))