a = [int(i) for i in open('7.txt')]
mini = max(i for i in a if i % 100 == 32)
print(mini)
res = []
for i in range(len(a)-2):
    if( (len(str(a[i])) == 5) +(len(str(a[i+1])) == 5) + (len(str(a[i +2])) == 5))  == 1:
        if  (a[i]+a[i+1]+a[i+2])>= mini:
            res.append(a[i]+a[i+1]+a[i+2])

print(len(res),max(res))