from itertools import *
a = '123456789ABCDEF'
k = 0
for i in product(a, repeat=7):
    s = ''.join(i)
    if (s.count("A") + s.count("B")+ s.count("C")+ s.count("D")+ s.count("E")+ s.count("F")) <= 4:
        k += 1
print(k)