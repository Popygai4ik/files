from  itertools import *
c = 0
s = 'АЙЛИН'
for i in product('МАЛЙИНК',repeat=5):
    w = ''.join(i)
    matsh = 0
    for k in range(5):
        if w[k] == s[k]:
            matsh += 1
    if matsh == 3:
        c +=1
print(c)
