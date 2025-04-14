f = open('24.2dz.txt')
s = f.readline()
res = ''
s = s.replace('+','*')
# print(s)
a = s.split('*')

max_res = ''
for i in a:
    if len(i) > 0 and i[0] != "0":
        res += i + '*'
    elif len(i) > 1 and i[0] == '0':
        res = str(int(i))+'*'
    else:
        res = ''
    max_res = max(max_res, res, key=len)

# max_res.sort(key=len,reverse=True)
print(max_res,len(max_res)- 1)
import re
res = re.findall(r'[456][0456]*(?:[+*][456][0456]*)*', s)
print(len(max(res,key=len)))