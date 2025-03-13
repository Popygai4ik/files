from itertools import *
c = 0
for i in product('ABCDE', repeat=4):
    w = ''.join(i)
    # gl = ''
    # for k in w:
    #     if k in 'AE':
    #         gl += k
    cog = ''
    for k in w:
        if k not in 'AE':
            cog += k
    # if gl == sorted(gl) and cog == sorted(cog,reverse=True):
    #     print(w, gl, cog)
    #     c += 1

    if ('AA' == w[:2] or 'EE' == w[:2] or 'AE' == w[:2]) and ('DD' == w[2:] or 'CC' == w[2:] or 'BB' == w[2:] or 'DC' == w[2:] or 'DB' == w[2:]or 'CB' == w[2:]):
        c+= 1
print(c)