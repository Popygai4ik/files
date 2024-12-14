from itertools import *
c = 0
for i in product('01234567', repeat=5):
    s = ''.join(i)
    if s[0] != '0' and s[0] not in '02468' and (s[-1] not in '15') and s.count('7') <= 1:
        c +=1
print(c)