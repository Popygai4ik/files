from itertools import *

n = 1
for i in product(sorted('ЛАСТ'), repeat=5):
    w = ''.join(i)
    w = w.replace('Л', '*')
    w = w.replace('Т', '*')
    if w.count('С') == 2 and '**' not in w:
        print(w, n)
    n +=1