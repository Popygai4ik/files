a = [int(i) for i in open('13')]
res = []


for i in range(len(a)- 2):
    if ((len(str(abs(a[i]))) == 4) +(len(str(abs(a[i + 1]))) == 4) + (len(str(abs(a[i + 2]))) == 4)) == 2:
        if ((abs(a[i]) % 100 == 29) + (abs(a[i + 1]) % 100 == 29)  + (abs(a[i + 2]) % 100 == 29)) == 1:
            if a[i] > sr and a[i +1] > sr and a[i +2] > sr:
                res.append(a[i]+a[i + 1]+a[i+2])
print(len(res), min(res))