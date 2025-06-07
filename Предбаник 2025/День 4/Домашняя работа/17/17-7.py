f = open('17.7.txt')
a = [int(x) for x in f]
t25 = [x for x in a if abs(x) % 100 == 25]
sr = sum(t25)/len(t25)
res = []
for i in range(len(a) - 2):
    if ((len(str(abs(a[i]))) == 4) +(len(str(abs(a[i + 1]))) == 4) + (len(str(abs(a[i + 2]))) == 4)) >= 1 and ((abs(a[i]) % 100  == 13) + (abs(a[i + 1] ) % 100  == 13) + (abs(a[i + 2]) % 100  == 13)) == 2 and a[i]>sr and a[i + 1] > sr and a[i + 2] > sr:
        res.append(a[i] + a[i + 1] + a[i + 2])
print(len(res),min(res))