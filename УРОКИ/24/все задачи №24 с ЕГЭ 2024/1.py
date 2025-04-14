f = open('24.1.txt')
res = ''
s = f.readline()
max_res = []
for i in s:
    # print(i)
    if len(res) == 0 and i in '123456789AB':
        res+= i
    elif len(res) > 0 and i in '0123456789AB':
        res += i
    else:

        res = ''
    max_res.append(res)
max_res.sort(key=len,reverse=True)
print(max_res[:10])
for i in max_res:


    if int(i, 12) % int("3", 12) == 0:
        print(i, len(i))
        break
import  re
is_ok = re.findall(r'[123456789AB][0123456789AB]*', s)
is_ok.sort(key=len,reverse=True)
for i in is_ok:
    if int(i, 12) % int("3", 12) == 0:
        print(i, len(i))
        break