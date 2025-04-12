from  itertools import *
c = 0

for l in product('ABCDE',repeat=4):
    w = ''.join(l)

    i = 0
    while i < len(w) and w[i] in 'AE':
        i += 1
    gls = w[:i]
    sogl = w[i:]
    if ((''.join(sorted(gls)) == str(gls)) and ((''.join(sorted(sogl,reverse=True)) == str(sogl)))):
        c += 1
print(c)
