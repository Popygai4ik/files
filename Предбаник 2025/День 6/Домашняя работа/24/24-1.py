f = open('24.1.txt')
s = f.readline()
s = s.replace('A', 'B')
s = s.replace('C', 'B')
s = s.replace('8', '9')
# print(s)
res = []
buff = ''
for x in s:
    if len(buff) == 0:
        buff += x
    elif len(buff) > 0 and buff[-1] != x:
        buff += x
    else:
        res.append(buff)
        buff = ''
for i in range(1,100):
    if 'B9' * i in s:
        print(i)
print(len(max(res, key=len)))