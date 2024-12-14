f = open('3.txt')
n= int(f.readline())
a = [int(s) for s in f]
a.sort(reverse=True)
s1 = sum(a[:(n//3)])
s2 = 0
for k in range(len(a)):
    if (k+1) % 3 == 0:
        s2 += a[k]
print(sum(a) - s1, sum(a) - s2)