f = open('24.3dz.txt')
s = f.readline()
import re
is_poka = re.findall(r'(?:0|[1234][01234]*)(?:[+*](?:0|[1234][01234]*))*', s)
print(len(max(is_poka,key=len)))
print(max(is_poka,key=len))
s = s.replace('+', '*')
a = s.split('*')
res = ''
max_res = ''
for i in a:
    if len(i)>0 and i[0] != '0':
        res += i+'*'
    elif len(i) == 1 and i[0] == '0':
        res += i + '*'
    else:
        res = ''
    max_res = max(max_res,res,key=len)
print(max_res)