from itertools import *
c = 1
for i in product('AEY', repeat=5):
    w = ''.join(i)
    # print(w, c)
    if c == 50:
        print(c, w)
    c +=1