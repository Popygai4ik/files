import string
f= open('24_1.txt')
s = f.readline()
for k in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    while k in s:
        s = s.replace(k, '*')
s = s.split('*')
ans = []
for i in s:
    if len(i) == 6:
        ans.append(i)
ans.sort()
print(ans)