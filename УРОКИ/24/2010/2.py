import string
f= open('24_2.txt')
s = f.readline()
for k in 'QWERTYUIOPASDFGHJKLZXCVBNM24680':
    while k in s:
        s = s.replace(k, '*')
s = s.split('*')
# print(s)

ans = []
for i in s:
    if i != '':
        ans.append(i)
ans.sort()
# print(ans)
print(max(ans))
f = open('24_2.txt')

s = f.readline()

for x in 'QWERTYUIOPASDFGHJKLZXCVBNM24680':

    s = s.replace(x, ' ')

a = s.split(' ')

max_str = 0

for i in range(len(a)):

    if len(a[i]) > 0:

        max_str = max(max_str, int(a[i]))

print(max_str)