from itertools import *
c = 0
for s in permutations('ТАВРИЯ', r=5):
    w = ''.join(s)
    if w[0] != 'В' and 'ИЯ' not in w:
        print(w)
        c +=1
print(c )