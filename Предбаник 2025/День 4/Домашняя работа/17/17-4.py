f =  open('17.4.txt')
a = [int(x) for x in f]
res = []
maxi = max(x for x in a if abs(x) % 100 == 13)
for i in range(len(a) - 2):

    if (((len(str(abs(a[i]))) == 5) + (len(str(abs(a[i + 1]))) == 5)+ (len(str(abs(a[i + 2]))) == 5)) == 2 and ((a[i] + a[i + 1] + a[i + 2]) <= maxi)):
        res.append(a[i] +a[i + 1] + a[i + 2])
print(len(res), max(res))