a = [int(i) for i in open('4.txt')]
res = []
werwer = [i for i in a if abs(i) % 100 == 17]
msx_17 = max(werwer)
print(msx_17)
for i in range(len(a)-2):
    su = a[i] + a[i + 1] + a[i + 2]
    if ((len(str(abs(a[i]))) == 5) + (len(str(abs(a[i+1]))) == 5) + (len(str(abs(a[i+2]))) == 5) ) == 2:
        if su <= msx_17:
            res.append(su)
print(len(res),max(res))
