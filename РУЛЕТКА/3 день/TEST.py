from itertools import *
c = 0
for i in set(permutations('113', r=3)):
    c += 1
print(c)