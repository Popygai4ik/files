a = [int(i) for i in open('8')]

res = []
for i in range(len(a)-1):
   if abs(a[i])% 10 == abs(a[i+1])% 10 and str(abs(a[i])%10) in '02468':
       res.append(abs(a[i])*abs(a[i+1]))
print(len(res),max(res))