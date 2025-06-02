f = open('ac815024-b45e-4da7-9eec-31d60342f3b9_24.txt')
import string
s = f.readline()
alf = '0123456789ABCDE'
byf = ''
res = []
for i in s:
    if len(byf) == 0 and i in alf[1:]:
        byf += i
    elif len(byf) > 0 and i in alf:
        byf += i
    else:
        res.append(byf)
        byf = ''
print(len(max(res,key=len)))